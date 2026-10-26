/* CodingTrainer – Python-Laufzeit (Pyodide). Läuft als Web Worker oder, falls Worker nicht erlaubt sind, im Hauptthread. */
(function () {
  "use strict";
  var IS_WORKER = typeof WorkerGlobalScope !== "undefined" && self instanceof WorkerGlobalScope;
  var BASE = IS_WORKER ? self.location.href : document.baseURI;
  var HARNESS = /*HARNESS*/"";
  var pyodide = null;
  var loading = null;

  // Der Artefakt-Host liefert keine .zip/.whl-Dateien aus. Sie liegen deshalb als Base64-Text
  // unter <name>.b64.txt und werden hier beim Abruf durch Pyodide transparent dekodiert.
  var G = IS_WORKER ? self : window;
  var REMAP = /\/py\/([^\/?#]+\.(?:zip|whl))(?:[?#].*)?$/;
  var origFetch = G.fetch.bind(G);
  function b64ToBytes(txt) {
    txt = txt.replace(/\s+/g, "");
    if (Uint8Array.fromBase64) return Uint8Array.fromBase64(txt);
    var bin = atob(txt), out = new Uint8Array(bin.length);
    for (var i = 0; i < bin.length; i++) out[i] = bin.charCodeAt(i);
    return out;
  }
  if (/*B64*/true) G.fetch = function (input, init) {
    var url = typeof input === "string" ? input : (input && input.url) || String(input);
    var m = REMAP.exec(url);
    if (!m) return origFetch(input, init);
    var target = url.replace(REMAP, "/py/" + m[1] + ".b64.txt");
    return origFetch(target).then(function (r) {
      if (!r.ok) return r;
      return r.text().then(function (txt) {
        return new Response(b64ToBytes(txt), { status: 200, headers: { "Content-Type": "application/octet-stream" } });
      });
    });
  };

  function loadScript(url) {
    return new Promise(function (resolve, reject) {
      var s = document.createElement("script");
      s.src = url;
      s.onload = resolve;
      s.onerror = function () { reject(new Error("script load failed: " + url)); };
      document.head.appendChild(s);
    });
  }

  function boot(status) {
    if (loading) return loading;
    loading = (async function () {
      var pyUrl = new URL("py/pyodide.js", BASE).href;
      if (IS_WORKER) importScripts(pyUrl);
      else await loadScript(pyUrl);
      pyodide = await loadPyodide({ indexURL: new URL("py/", BASE).href });
      pyodide.runPython(HARNESS);
      return pyodide;
    })();
    return loading;
  }

  async function ensurePackages(code, status) {
    if (/\b(numpy|pandas)\b/.test(code)) {
      status("packages");
      await pyodide.loadPackagesFromImports(code, { messageCallback: function () {}, errorCallback: function () {} });
    }
  }

  function callApi(fn, args) {
    pyodide.globals.set("_ct_args", pyodide.toPy(args));
    try {
      return JSON.parse(pyodide.runPython(fn + "(*_ct_args)"));
    } finally {
      pyodide.globals.delete("_ct_args");
    }
  }

  async function handle(msg, reply) {
    var id = msg.id;
    var status = function (s) { reply({ id: id, status: s }); };
    try {
      if (msg.type === "init") {
        await boot();
        reply({ id: id, ok: true, result: { version: pyodide.runPython("import sys; sys.version.split()[0]") } });
        return;
      }
      await boot();
      var r;
      if (msg.type === "run") {
        await ensurePackages(msg.code, status);
        r = callApi("api_run", [msg.code, msg.stdin || "", msg.lang || "de", msg.files || null]);
      } else if (msg.type === "check") {
        await ensurePackages(msg.code + "\n" + msg.tests, status);
        r = callApi("api_check", [msg.code, msg.tests, msg.chapter, msg.require || [], msg.forbid || [], msg.lang || "de", msg.off || []]);
      } else if (msg.type === "constructs") {
        r = callApi("api_constructs", [msg.code, msg.chapter, msg.lang || "de", msg.off || []]);
      } else {
        throw new Error("unknown message " + msg.type);
      }
      reply({ id: id, ok: true, result: r });
    } catch (e) {
      reply({ id: id, ok: false, error: String((e && e.message) || e) });
    }
  }

  if (IS_WORKER) {
    self.onmessage = function (e) { handle(e.data, function (r) { self.postMessage(r); }); };
  } else {
    window.CTLocalEngine = { handle: handle };
  }
})();
