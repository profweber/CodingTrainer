from exlib import ex

# Kapitel 10, zweiter Satz: Klassen, Attribute, Methoden, Vererbung, super(), protected/private,
# Getter/Setter, Magic Methods, abc.

# ------------------------------------------------------------------ Stufe 1
ex(id="k10-gear", ch="10", lvl=1,
   title={"de": "Klasse Zahnrad", "en": "Class Gear"},
   task={"de": "Schreiben Sie die Klasse `Gear(teeth, module)` für ein Stirnrad (Modul in mm). Der Konstruktor speichert beide Werte als Attribute gleichen Namens.\n- `pitch_diameter()`: Teilkreisdurchmesser $d = m \\cdot z$ (mm)\n- `tip_diameter()`: Kopfkreisdurchmesser $d + 2m$\n- `ratio_to(other)`: die Übersetzung zu einem anderen Zahnrad `other` (Zähnezahl von other / eigene Zähnezahl)\n- `center_distance(other)`: der Achsabstand zweier kämmender Räder $(d_1 + d_2)/2$",
         "en": "Write the class `Gear(teeth, module)` for a spur gear (module in mm). The constructor stores both values as attributes of the same name.\n- `pitch_diameter()`: pitch diameter $d = m \\cdot z$ (mm)\n- `tip_diameter()`: tip diameter $d + 2m$\n- `ratio_to(other)`: the ratio to another gear `other` (tooth count of other / own tooth count)\n- `center_distance(other)`: the centre distance of two meshing gears $(d_1 + d_2)/2$"},
   starter={"de": "class Gear:\n    def __init__(self, teeth, module):\n        ...\n", "en": "class Gear:\n    def __init__(self, teeth, module):\n        ...\n"},
   solution='class Gear:\n    def __init__(self, teeth, module):\n        self.teeth = teeth\n        self.module = module\n\n    def pitch_diameter(self):\n        return self.module * self.teeth\n\n    def tip_diameter(self):\n        return self.pitch_diameter() + 2 * self.module\n\n    def ratio_to(self, other):\n        return other.teeth / self.teeth\n\n    def center_distance(self, other):\n        return (self.pitch_diameter() + other.pitch_diameter()) / 2\n\npinion = Gear(17, 2.0)\nwheel = Gear(51, 2.0)\nprint(pinion.ratio_to(wheel), pinion.center_distance(wheel))\n',
   tests='''
ns, out = run()
for (z1, m1), (z2, m2) in [((17, 2.0), (51, 2.0)), ((20, 1.5), (35, 1.5)), ((12, 4.0), (12, 4.0))]:
    a = call(ns, "Gear", z1, m1); b = call(ns, "Gear", z2, m2)
    check(getattr(a, "teeth", None) == z1 and getattr(a, "module", None) == m1, f"Gear({z1}, {m1}) speichert teeth und module", f"Gear({z1}, {m1}) stores teeth and module")
    check(approx(method(a, "pitch_diameter"), z1 * m1) and approx(method(a, "tip_diameter"), z1 * m1 + 2 * m1), f"d = {z1 * m1:g} mm, d_a = {z1 * m1 + 2 * m1:g} mm", f"d = {z1 * m1:g} mm, d_a = {z1 * m1 + 2 * m1:g} mm")
    check(approx(method(a, "ratio_to", b), z2 / z1) and approx(method(a, "center_distance", b), (z1 * m1 + z2 * m2) / 2), f"i = {z2 / z1:.3f}, Achsabstand {(z1 * m1 + z2 * m2) / 2:g} mm", f"i = {z2 / z1:.3f}, centre distance {(z1 * m1 + z2 * m2) / 2:g} mm")
''',
   require=["class"], refs=["10.3", "10.2"])

ex(id="k10-battery", ch="10", lvl=1,
   title={"de": "Klasse Akku", "en": "Class Battery"},
   task={"de": "Schreiben Sie die Klasse `Battery(capacity_ah, voltage)`. Ein neuer Akku ist voll geladen: Das Attribut `charge_ah` (aktuelle Ladung in Ah) startet mit der Kapazität.\n- `energy_wh()`: gespeicherte Energie = Ladung · Spannung\n- `soc()`: Ladezustand in Prozent\n- `discharge(power_w, hours)`: entnimmt die Ladung `power_w * hours / voltage`, aber höchstens bis 0. Gibt die tatsächlich gelieferte Energie in Wh zurück.\n- `runtime_h(power_w)`: wie viele Stunden die Restladung bei der Leistung power_w noch reicht",
         "en": "Write the class `Battery(capacity_ah, voltage)`. A new battery is fully charged: the attribute `charge_ah` (current charge in Ah) starts at the capacity.\n- `energy_wh()`: stored energy = charge · voltage\n- `soc()`: state of charge in percent\n- `discharge(power_w, hours)`: removes the charge `power_w * hours / voltage`, but at most down to 0. Returns the energy actually delivered in Wh.\n- `runtime_h(power_w)`: how many hours the remaining charge lasts at power power_w"},
   starter={"de": "class Battery:\n    def __init__(self, capacity_ah, voltage):\n        ...\n", "en": "class Battery:\n    def __init__(self, capacity_ah, voltage):\n        ...\n"},
   solution='class Battery:\n    def __init__(self, capacity_ah, voltage):\n        self.capacity_ah = capacity_ah\n        self.voltage = voltage\n        self.charge_ah = capacity_ah\n\n    def energy_wh(self):\n        return self.charge_ah * self.voltage\n\n    def soc(self):\n        return self.charge_ah / self.capacity_ah * 100\n\n    def discharge(self, power_w, hours):\n        needed = power_w * hours / self.voltage\n        taken = needed if needed <= self.charge_ah else self.charge_ah\n        self.charge_ah -= taken\n        return taken * self.voltage\n\n    def runtime_h(self, power_w):\n        return self.energy_wh() / power_w\n\nb = Battery(100, 12)\nprint(b.discharge(240, 2), b.soc(), b.runtime_h(120))\n',
   tests='''
ns, out = run()
b = call(ns, "Battery", 100, 12)
check(getattr(b, "charge_ah", None) == 100 and approx(method(b, "energy_wh"), 1200) and approx(method(b, "soc"), 100), "Neuer Akku: 100 Ah, 1200 Wh, 100 %", "New battery: 100 Ah, 1200 Wh, 100 %")
check(approx(method(b, "discharge", 240, 2), 480) and approx(b.charge_ah, 60) and approx(method(b, "soc"), 60), "discharge(240, 2): 480 Wh geliefert, noch 60 Ah = 60 %", "discharge(240, 2): 480 Wh delivered, 60 Ah = 60 % left")
check(approx(method(b, "runtime_h", 120), 6), "runtime_h(120) = 6 h", "runtime_h(120) = 6 h")
check(approx(method(b, "discharge", 1200, 1), 720) and approx(b.charge_ah, 0), "Mehr entnehmen als vorhanden: nur 720 Wh, Ladung 0", "Taking more than available: only 720 Wh, charge 0")
c = call(ns, "Battery", 50, 48)
check(approx(method(c, "energy_wh"), 2400) and approx(method(c, "runtime_h", 800), 3), "Battery(50, 48): 2400 Wh, 3 h bei 800 W", "Battery(50, 48): 2400 Wh, 3 h at 800 W")
''',
   require=["class"], refs=["10.3", "10.2"])

ex(id="k10-point", ch="10", lvl=1,
   title={"de": "Messpunkt mit Textdarstellung", "en": "Measuring point with text representation"},
   task={"de": "Schreiben Sie die Klasse `Point(x, y, label=\"P\")` für Messpunkte einer Koordinatenmessmaschine (mm).\n- `distance_to(other)`: Abstand zu einem anderen Punkt (Wurzel mit `** 0.5`)\n- `moved(dx, dy)`: gibt einen **neuen** Punkt mit gleichem Label zurück, der um dx, dy verschoben ist (das Original bleibt unverändert)\n- `__str__`: z.B. `P1 (12.50 | -3.00)` – Koordinaten mit zwei Nachkommastellen\n\nTesten Sie mit `print(Point(12.5, -3, \"P1\"))`.",
         "en": "Write the class `Point(x, y, label=\"P\")` for measuring points of a coordinate measuring machine (mm).\n- `distance_to(other)`: distance to another point (root with `** 0.5`)\n- `moved(dx, dy)`: returns a **new** point with the same label, shifted by dx, dy (the original stays unchanged)\n- `__str__`: e.g. `P1 (12.50 | -3.00)` – coordinates with two decimals\n\nTest with `print(Point(12.5, -3, \"P1\"))`."},
   starter={"de": "class Point:\n    def __init__(self, x, y, label=\"P\"):\n        ...\n", "en": "class Point:\n    def __init__(self, x, y, label=\"P\"):\n        ...\n"},
   solution='class Point:\n    def __init__(self, x, y, label="P"):\n        self.x = x\n        self.y = y\n        self.label = label\n\n    def distance_to(self, other):\n        return ((self.x - other.x)**2 + (self.y - other.y)**2) ** 0.5\n\n    def moved(self, dx, dy):\n        return Point(self.x + dx, self.y + dy, self.label)\n\n    def __str__(self):\n        return f"{self.label} ({self.x:.2f} | {self.y:.2f})"\n\nprint(Point(12.5, -3, "P1"))\n',
   tests='''
ns, out = run()
P = ns.get("Point")
a = call(ns, "Point", 12.5, -3, "P1"); b = call(ns, "Point", 0, 1)
check(safe(lambda: str(a)) == "P1 (12.50 | -3.00)" and safe(lambda: str(b)) == "P (0.00 | 1.00)", "str: 'P1 (12.50 | -3.00)' und 'P (0.00 | 1.00)'", "str: 'P1 (12.50 | -3.00)' and 'P (0.00 | 1.00)'")
c = call(ns, "Point", 2.5, 3)
check(approx(method(a, "distance_to", b), ((12.5)**2 + 16) ** 0.5) and approx(method(a, "distance_to", c), 136 ** 0.5) and approx(method(b, "distance_to", b), 0), "distance_to stimmt", "distance_to is correct")
m = method(a, "moved", 1.5, 2)
check(isinstance(m, P) and m is not a and approx(m.x, 14) and approx(m.y, -1) and m.label == "P1", "moved(1.5, 2) liefert einen neuen Punkt P1 (14 | -1)", "moved(1.5, 2) returns a new point P1 (14 | -1)")
check(approx(a.x, 12.5) and approx(a.y, -3), "Das Original bleibt unverändert", "The original stays unchanged")
''',
   require=["class", "magic"], refs=["10.7", "10.3"])

ex(id="k10-timer", ch="10", lvl=1,
   title={"de": "Betriebsstundenzähler", "en": "Operating-hours counter"},
   task={"de": "Schreiben Sie die Klasse `HourMeter(name)` für eine Maschine. Zeiten werden als Zahlen in Stunden übergeben (z.B. 8.5 für 8:30 Uhr). Attribute: `name`, `total` (Betriebsstunden, Start 0) und `start_time` (Start `None`, solange die Maschine steht).\n- `start(t)`: Maschine läuft ab Zeit t. Läuft sie bereits, passiert nichts.\n- `stop(t)`: Maschine stoppt; die Laufzeit seit dem Start wird zu `total` addiert. Läuft sie nicht, passiert nichts.\n- `is_running()`: ob die Maschine gerade läuft\n- `service_due(interval=500)`: ob die Betriebsstunden mindestens das Wartungsintervall erreicht haben",
         "en": "Write the class `HourMeter(name)` for a machine. Times are passed as numbers in hours (e.g. 8.5 for 8:30). Attributes: `name`, `total` (operating hours, starting at 0) and `start_time` (`None` as long as the machine is stopped).\n- `start(t)`: the machine runs from time t. If it is already running, nothing happens.\n- `stop(t)`: the machine stops; the run time since the start is added to `total`. If it isn't running, nothing happens.\n- `is_running()`: whether the machine is currently running\n- `service_due(interval=500)`: whether the operating hours have reached at least the service interval"},
   starter={"de": "class HourMeter:\n    def __init__(self, name):\n        ...\n", "en": "class HourMeter:\n    def __init__(self, name):\n        ...\n"},
   solution='class HourMeter:\n    def __init__(self, name):\n        self.name = name\n        self.total = 0\n        self.start_time = None\n\n    def start(self, t):\n        if self.start_time is None:\n            self.start_time = t\n\n    def stop(self, t):\n        if self.start_time is not None:\n            self.total += t - self.start_time\n            self.start_time = None\n\n    def is_running(self):\n        return self.start_time is not None\n\n    def service_due(self, interval=500):\n        return self.total >= interval\n\nm = HourMeter("Presse 3")\nm.start(6.0)\nm.stop(14.5)\nprint(m.total, m.is_running())\n',
   tests='''
ns, out = run()
m = call(ns, "HourMeter", "Presse 3")
check(getattr(m, "name", None) == "Presse 3" and getattr(m, "total", None) == 0 and getattr(m, "start_time", 1) is None and method(m, "is_running") is False, "Neuer Zähler: total 0, steht", "New counter: total 0, stopped")
method(m, "start", 6.0)
check(method(m, "is_running") is True, "Nach start(6.0) läuft die Maschine", "After start(6.0) the machine is running")
method(m, "start", 7.0); method(m, "stop", 14.5)
check(approx(m.total, 8.5) and method(m, "is_running") is False, "Zweites start() wird ignoriert; nach stop(14.5): 8.5 h", "Second start() is ignored; after stop(14.5): 8.5 h")
method(m, "stop", 16.0)
check(approx(m.total, 8.5), "stop() bei stehender Maschine ändert nichts", "stop() on a stopped machine changes nothing")
method(m, "start", 20.0); method(m, "stop", 22.0)
check(approx(m.total, 10.5) and method(m, "service_due") is False and method(m, "service_due", 10) is True and method(m, "service_due", 10.5) is True, "Zweiter Lauf addiert 2 h; service_due(10) und service_due(10.5) = True", "Second run adds 2 h; service_due(10) and service_due(10.5) = True")
m.total = 500
check(method(m, "service_due") is True, "Bei genau 500 h ist die Wartung fällig (Standardintervall)", "At exactly 500 h the service is due (default interval)")
''',
   require=["class", "default_arg"], refs=["10.3", "5.3m"])

# ------------------------------------------------------------------ Stufe 2
ex(id="k10-vehicles", ch="10", lvl=2,
   title={"de": "Fahrzeuge und Vererbung", "en": "Vehicles and inheritance"},
   task={"de": "Basisklasse `Vehicle(name, mass_kg)` mit den Methoden\n- `total_mass()`: gibt `mass_kg` zurück\n- `kinetic_energy(v_kmh)`: Bewegungsenergie $\\frac{1}{2} m v^2$ in kJ (Geschwindigkeit in km/h umrechnen!) – mit `total_mass()`\n\nAbgeleitete Klassen (Konstruktor mit `super().__init__(…)`):\n- `Truck(name, mass_kg, payload_kg)`: überschreibt `total_mass()` (Leermasse + Zuladung)\n- `ElectricCar(name, mass_kg, battery_kwh, consumption)`: zusätzliche Methode `range_km()` = `battery_kwh / consumption * 100` (Verbrauch in kWh/100 km)\n\n`kinetic_energy` wird **nur** in der Basisklasse geschrieben und funktioniert trotzdem für den Lkw mit Zuladung – warum?",
         "en": "Base class `Vehicle(name, mass_kg)` with the methods\n- `total_mass()`: returns `mass_kg`\n- `kinetic_energy(v_kmh)`: kinetic energy $\\frac{1}{2} m v^2$ in kJ (convert the speed from km/h!) – using `total_mass()`\n\nDerived classes (constructor with `super().__init__(…)`):\n- `Truck(name, mass_kg, payload_kg)`: overrides `total_mass()` (empty mass + payload)\n- `ElectricCar(name, mass_kg, battery_kwh, consumption)`: additional method `range_km()` = `battery_kwh / consumption * 100` (consumption in kWh/100 km)\n\n`kinetic_energy` is written **only** in the base class and still works for the truck with payload – why?"},
   starter={"de": "class Vehicle:\n    def __init__(self, name, mass_kg):\n        ...\n", "en": "class Vehicle:\n    def __init__(self, name, mass_kg):\n        ...\n"},
   solution='class Vehicle:\n    def __init__(self, name, mass_kg):\n        self.name = name\n        self.mass_kg = mass_kg\n\n    def total_mass(self):\n        return self.mass_kg\n\n    def kinetic_energy(self, v_kmh):\n        v = v_kmh / 3.6\n        return 0.5 * self.total_mass() * v**2 / 1000\n\n\nclass Truck(Vehicle):\n    def __init__(self, name, mass_kg, payload_kg):\n        super().__init__(name, mass_kg)\n        self.payload_kg = payload_kg\n\n    def total_mass(self):\n        return self.mass_kg + self.payload_kg\n\n\nclass ElectricCar(Vehicle):\n    def __init__(self, name, mass_kg, battery_kwh, consumption):\n        super().__init__(name, mass_kg)\n        self.battery_kwh = battery_kwh\n        self.consumption = consumption\n\n    def range_km(self):\n        return self.battery_kwh / self.consumption * 100\n\nfor v in [Truck("LKW", 12000, 8000), ElectricCar("E-Auto", 1800, 60, 16)]:\n    print(v.name, round(v.kinetic_energy(80), 1), "kJ")\n',
   tests='''
ns, out = run()
V = ns.get("Vehicle")
t = call(ns, "Truck", "LKW", 12000, 8000)
e = call(ns, "ElectricCar", "E-Auto", 1800, 60, 16)
check(isinstance(t, V) and isinstance(e, V), "Truck und ElectricCar erben von Vehicle", "Truck and ElectricCar inherit from Vehicle")
check(getattr(t, "name", None) == "LKW" and getattr(t, "mass_kg", None) == 12000 and getattr(e, "mass_kg", None) == 1800, "name und mass_kg werden über super().__init__ gesetzt", "name and mass_kg are set via super().__init__")
check(method(t, "total_mass") == 20000 and method(e, "total_mass") == 1800, "total_mass: Lkw 20000 kg (mit Zuladung), E-Auto 1800 kg", "total_mass: truck 20000 kg (with payload), e-car 1800 kg")
check(approx(method(t, "kinetic_energy", 80), 0.5 * 20000 * (80 / 3.6)**2 / 1000) and approx(method(e, "kinetic_energy", 36), 0.5 * 1800 * 100 / 1000), "kinetic_energy nutzt total_mass (Lkw bei 80 km/h ≈ 4938 kJ)", "kinetic_energy uses total_mass (truck at 80 km/h ≈ 4938 kJ)")
check(approx(method(e, "range_km"), 375), "range_km() = 375 km", "range_km() = 375 km")
check("kinetic_energy" not in vars(ns["Truck"]) and "kinetic_energy" not in vars(ns["ElectricCar"]), "kinetic_energy steht nur in der Basisklasse", "kinetic_energy is only in the base class")
''',
   require=["class", "super"], refs=["10.5", "10.3"])

ex(id="k10-setpoint", ch="10", lvl=2,
   title={"de": "Sollwert mit privatem Attribut", "en": "Setpoint with a private attribute"},
   task={"de": "Ein Temperaturregler darf nur Sollwerte zwischen `low` und `high` annehmen. Schreiben Sie die Klasse `Setpoint(low, high, value)` mit dem **privaten** Attribut `__value` (zwei Unterstriche).\n- `get_value()`: Getter\n- `set_value(v)`: Setter mit Prüfung – liegt v außerhalb [low, high], wird der Wert auf die nächste Grenze begrenzt. Rückgabe: `True`, wenn v unverändert übernommen wurde, sonst `False`.\n- `step(delta)`: verändert den Sollwert um delta (über den Setter, also mit Begrenzung) und gibt den neuen Wert zurück.\n\nAuch der Startwert im Konstruktor soll über `set_value` begrenzt werden. Prüfen Sie: Warum funktioniert `regler.__value` von außen nicht?",
         "en": "A temperature controller may only accept setpoints between `low` and `high`. Write the class `Setpoint(low, high, value)` with the **private** attribute `__value` (two underscores).\n- `get_value()`: getter\n- `set_value(v)`: setter with a check – if v lies outside [low, high], the value is limited to the nearest limit. Returns `True` if v was taken over unchanged, otherwise `False`.\n- `step(delta)`: changes the setpoint by delta (through the setter, i.e. with limiting) and returns the new value.\n\nThe initial value in the constructor should also be limited via `set_value`. Check: why doesn't `controller.__value` work from outside?"},
   starter={"de": "class Setpoint:\n    def __init__(self, low, high, value):\n        ...\n", "en": "class Setpoint:\n    def __init__(self, low, high, value):\n        ...\n"},
   solution='class Setpoint:\n    def __init__(self, low, high, value):\n        self.low = low\n        self.high = high\n        self.__value = low\n        self.set_value(value)\n\n    def get_value(self):\n        return self.__value\n\n    def set_value(self, v):\n        if v < self.low:\n            self.__value = self.low\n            return False\n        if v > self.high:\n            self.__value = self.high\n            return False\n        self.__value = v\n        return True\n\n    def step(self, delta):\n        self.set_value(self.__value + delta)\n        return self.__value\n\nregler = Setpoint(15, 30, 21)\nprint(regler.step(5), regler.step(5), regler.get_value())\n',
   tests='''
ns, out = run()
s = call(ns, "Setpoint", 15, 30, 21)
check(method(s, "get_value") == 21 and hasattr(s, "_Setpoint__value") and not hasattr(s, "__value"), "Privates Attribut __value (Name Mangling: _Setpoint__value), Startwert 21", "Private attribute __value (name mangling: _Setpoint__value), initial value 21")
check(method(s, "set_value", 25) is True and method(s, "get_value") == 25, "set_value(25) → True", "set_value(25) → True")
check(method(s, "set_value", 40) is False and method(s, "get_value") == 30, "set_value(40) → False, begrenzt auf 30", "set_value(40) → False, limited to 30")
check(method(s, "step", -20) == 15 and method(s, "step", 3.5) == 18.5, "step(-20) → 15 (Grenze), step(3.5) → 18.5", "step(-20) → 15 (limit), step(3.5) → 18.5")
check(method(s, "set_value", 15) is True and method(s, "set_value", 30) is True, "Werte genau auf den Grenzen werden unverändert übernommen (True)", "Values exactly on the limits are taken over unchanged (True)")
t = call(ns, "Setpoint", 0, 10, -5)
check(method(t, "get_value") == 0, "Startwert außerhalb wird begrenzt (−5 → 0)", "Initial value outside is limited (−5 → 0)")
''',
   require=["class"], refs=["10.6", "10.6g"])

ex(id="k10-components", ch="10", lvl=2,
   title={"de": "Bauelemente in Reihe (Polymorphie)", "en": "Components in series (polymorphism)"},
   task={"de": "Drei Klassen beschreiben passive Bauelemente; jede hat die Methode `impedance(f)`, die die komplexe Impedanz (Ω) bei der Frequenz f (Hz) zurückgibt (`math.pi` verwenden):\n- `Resistor(name, r)`: $Z = R$\n- `Inductor(name, l)`: $Z = j \\cdot 2\\pi f L$\n- `Capacitor(name, c)`: $Z = \\dfrac{1}{j \\cdot 2\\pi f C}$\n\nGemeinsame Basisklasse ist `Component(name)` mit dem Attribut `name` und der Methode `describe(f)`, die einen Text wie `L1: |Z| = 31.4 Ohm bei 1000 Hz` zurückgibt (Betrag mit `abs()`, eine Nachkommastelle). `describe` steht nur in der Basisklasse.\n\nSchreiben Sie außerdem die Funktion `series_impedance(components, f)`, die die Summe der Impedanzen einer Liste von Bauelementen liefert – egal welcher Art.",
         "en": "Three classes describe passive components; each has the method `impedance(f)` returning the complex impedance (Ω) at frequency f (Hz) (use `math.pi`):\n- `Resistor(name, r)`: $Z = R$\n- `Inductor(name, l)`: $Z = j \\cdot 2\\pi f L$\n- `Capacitor(name, c)`: $Z = \\dfrac{1}{j \\cdot 2\\pi f C}$\n\nThe common base class is `Component(name)` with the attribute `name` and the method `describe(f)` returning a text like `L1: |Z| = 31.4 Ohm at 1000 Hz` (magnitude with `abs()`, one decimal). `describe` is only in the base class.\n\nAlso write the function `series_impedance(components, f)` that returns the sum of the impedances of a list of components – no matter of which kind."},
   starter={"de": "import math\n\nclass Component:\n    def __init__(self, name):\n        self.name = name\n", "en": "import math\n\nclass Component:\n    def __init__(self, name):\n        self.name = name\n"},
   solution='import math\n\nclass Component:\n    def __init__(self, name):\n        self.name = name\n\n    def impedance(self, f):\n        return 0\n\n    def describe(self, f):\n        return f"{self.name}: |Z| = {abs(self.impedance(f)):.1f} Ohm bei {f} Hz"\n\n\nclass Resistor(Component):\n    def __init__(self, name, r):\n        super().__init__(name)\n        self.r = r\n\n    def impedance(self, f):\n        return self.r\n\n\nclass Inductor(Component):\n    def __init__(self, name, l):\n        super().__init__(name)\n        self.l = l\n\n    def impedance(self, f):\n        return 1j * 2 * math.pi * f * self.l\n\n\nclass Capacitor(Component):\n    def __init__(self, name, c):\n        super().__init__(name)\n        self.c = c\n\n    def impedance(self, f):\n        return 1 / (1j * 2 * math.pi * f * self.c)\n\n\ndef series_impedance(components, f):\n    total = 0\n    for c in components:\n        total += c.impedance(f)\n    return total\n\nparts = [Resistor("R1", 100), Inductor("L1", 0.005), Capacitor("C1", 1e-6)]\nfor p in parts:\n    print(p.describe(1000))\nprint(series_impedance(parts, 1000))\n',
   tests='''
import math as _m
ns, out = run()
r = call(ns, "Resistor", "R1", 100); l = call(ns, "Inductor", "L1", 0.005); c = call(ns, "Capacitor", "C1", 1e-6)
C = ns.get("Component")
check(all(isinstance(x, C) for x in (r, l, c)) and r.name == "R1" and c.name == "C1", "Alle drei erben von Component und haben einen Namen", "All three inherit from Component and have a name")
for f in [50, 1000]:
    zl, zc = 1j * 2 * _m.pi * f * 0.005, 1 / (1j * 2 * _m.pi * f * 1e-6)
    ok = approx(abs(method(r, "impedance", f)), 100) and approx(abs(method(l, "impedance", f) - zl), 0) and approx(abs(method(c, "impedance", f) - zc), 0)
    check(ok, f"Impedanzen bei {f} Hz stimmen", f"Impedances at {f} Hz are correct")
    s = call(ns, "series_impedance", [r, l, c], f)
    check(approx(abs(s - (100 + zl + zc)), 0, 1e-6), f"Reihenschaltung bei {f} Hz: |Z| ≈ {abs(100 + zl + zc):.1f} Ω", f"series at {f} Hz: |Z| ≈ {abs(100 + zl + zc):.1f} Ω")
d = method(l, "describe", 1000)
check(isinstance(d, str) and "L1" in d and f"{2 * _m.pi * 1000 * 0.005:.1f}" in d and "describe" not in vars(ns["Inductor"]), "describe(1000) für L1 enthält 31.4 und steht nur in der Basisklasse", "describe(1000) for L1 contains 31.4 and is only in the base class")
''',
   require=["class", "super"], refs=["10.3", "10.5", "5.1"])

ex(id="k10-machine", ch="10", lvl=2,
   title={"de": "Maschine mit Sensoren", "en": "Machine with sensors"},
   task={"de": "Zwei Klassen arbeiten zusammen (eine Maschine *hat* mehrere Sensoren):\n- `Sensor(name, limit)`: Attribute `name`, `limit` und `value` (Start `None`); Methode `update(value)` speichert den neuen Messwert; Methode `alarm()` gibt `True` zurück, wenn ein Wert vorliegt und er über `limit` liegt.\n- `Machine(name)`: Attribut `sensors` (leere Liste); Methoden\n  - `add_sensor(sensor)`\n  - `read(values)`: `values` ist ein Dictionary Sensorname → Messwert; jeder passende Sensor wird aktualisiert, unbekannte Namen werden ignoriert\n  - `alarms()`: Liste der Namen aller Sensoren im Alarm (in der Reihenfolge des Hinzufügens)\n  - `status()`: `\"OK\"`, `\"WARNUNG\"` (ein Alarm) oder `\"STOPP\"` (zwei oder mehr Alarme)",
         "en": "Two classes work together (a machine *has* several sensors):\n- `Sensor(name, limit)`: attributes `name`, `limit` and `value` (initially `None`); method `update(value)` stores the new reading; method `alarm()` returns `True` if there is a value and it is above `limit`.\n- `Machine(name)`: attribute `sensors` (empty list); methods\n  - `add_sensor(sensor)`\n  - `read(values)`: `values` is a dictionary sensor name → reading; each matching sensor is updated, unknown names are ignored\n  - `alarms()`: list of the names of all sensors in alarm (in the order they were added)\n  - `status()`: `\"OK\"`, `\"WARNUNG\"` (one alarm) or `\"STOPP\"` (two or more alarms)"},
   starter={"de": "class Sensor:\n    def __init__(self, name, limit):\n        ...\n\nclass Machine:\n    def __init__(self, name):\n        ...\n", "en": "class Sensor:\n    def __init__(self, name, limit):\n        ...\n\nclass Machine:\n    def __init__(self, name):\n        ...\n"},
   solution='class Sensor:\n    def __init__(self, name, limit):\n        self.name = name\n        self.limit = limit\n        self.value = None\n\n    def update(self, value):\n        self.value = value\n\n    def alarm(self):\n        return self.value is not None and self.value > self.limit\n\n\nclass Machine:\n    def __init__(self, name):\n        self.name = name\n        self.sensors = []\n\n    def add_sensor(self, sensor):\n        self.sensors.append(sensor)\n\n    def read(self, values):\n        for s in self.sensors:\n            if s.name in values:\n                s.update(values[s.name])\n\n    def alarms(self):\n        return [s.name for s in self.sensors if s.alarm()]\n\n    def status(self):\n        n = len(self.alarms())\n        if n == 0:\n            return "OK"\n        elif n == 1:\n            return "WARNUNG"\n        return "STOPP"\n\nm = Machine("Fräse")\nm.add_sensor(Sensor("Temperatur", 80))\nm.add_sensor(Sensor("Vibration", 4.5))\nm.read({"Temperatur": 85, "Vibration": 2.0})\nprint(m.alarms(), m.status())\n',
   tests='''
ns, out = run()
s = call(ns, "Sensor", "T", 80)
check(getattr(s, "value", 1) is None and method(s, "alarm") is False, "Neuer Sensor: value None, kein Alarm", "New sensor: value None, no alarm")
method(s, "update", 85)
check(s.value == 85 and method(s, "alarm") is True, "update(85) bei Grenze 80 → Alarm", "update(85) with limit 80 → alarm")
method(s, "update", 80)
check(method(s, "alarm") is False, "update(80) bei Grenze 80 → kein Alarm (nur über der Grenze)", "update(80) with limit 80 → no alarm (only above the limit)")
m = call(ns, "Machine", "Fräse")
check(getattr(m, "sensors", None) == [], "Neue Maschine ohne Sensoren", "New machine without sensors")
for name, lim in [("Temperatur", 80), ("Vibration", 4.5), ("Druck", 6.0)]:
    method(m, "add_sensor", call(ns, "Sensor", name, lim))
check(method(m, "status") == "OK" and method(m, "alarms") == [], "Ohne Messwerte: OK", "Without readings: OK")
method(m, "read", {"Temperatur": 85, "Vibration": 2.0, "Strom": 99})
check(method(m, "alarms") == ["Temperatur"] and method(m, "status") == "WARNUNG", "Ein Alarm → WARNUNG; unbekannter Name 'Strom' wird ignoriert", "One alarm → WARNUNG; unknown name 'Strom' is ignored")
method(m, "read", {"Druck": 7.2})
check(method(m, "alarms") == ["Temperatur", "Druck"] and method(m, "status") == "STOPP", "Zwei Alarme → STOPP (Reihenfolge des Hinzufügens)", "Two alarms → STOPP (order of adding)")
''',
   require=["class"], refs=["10.3", "8.3"])

# ------------------------------------------------------------------ Stufe 3
ex(id="k10-fraction", ch="10", lvl=3,
   title={"de": "Exakte Übersetzungen mit Brüchen", "en": "Exact ratios with fractions"},
   task={"de": "Gleitkommazahlen sind bei Getriebeübersetzungen ungenau (z.B. 1/3). Schreiben Sie eine Klasse `Ratio(num, den)` für Brüche, die **immer gekürzt** gespeichert werden (Attribute `num`, `den`; der Nenner ist immer positiv).\n- Kürzen mit dem größten gemeinsamen Teiler – programmieren Sie ihn selbst (z.B. als Methode oder Funktion mit dem euklidischen Algorithmus).\n- `__mul__`: Produkt zweier Brüche (Gesamtübersetzung zweier Stufen) → neues `Ratio`\n- `__add__`: Summe zweier Brüche → neues `Ratio`\n- `__eq__`: Gleichheit (gekürzte Brüche vergleichen)\n- `__float__`: Wert als Gleitkommazahl\n- `__str__`: z.B. `3/1` oder `-2/5`\n\nIst der Nenner 0, soll ein `ZeroDivisionError` entstehen. Tipp: Der entsteht automatisch, wenn Sie im Konstruktor einmal `num / den` berechnen.",
         "en": "Floats are inaccurate for gear ratios (e.g. 1/3). Write a class `Ratio(num, den)` for fractions that are **always stored in lowest terms** (attributes `num`, `den`; the denominator is always positive).\n- Reduce with the greatest common divisor – program it yourself (e.g. as a method or function using the Euclidean algorithm).\n- `__mul__`: product of two fractions (overall ratio of two stages) → new `Ratio`\n- `__add__`: sum of two fractions → new `Ratio`\n- `__eq__`: equality (compare reduced fractions)\n- `__float__`: value as a float\n- `__str__`: e.g. `3/1` or `-2/5`\n\nIf the denominator is 0, a `ZeroDivisionError` should occur. Tip: it happens automatically if you compute `num / den` once in the constructor."},
   starter={"de": "class Ratio:\n    def __init__(self, num, den):\n        ...\n", "en": "class Ratio:\n    def __init__(self, num, den):\n        ...\n"},
   solution='def gcd(a, b):\n    while b != 0:\n        a, b = b, a % b\n    return abs(a)\n\n\nclass Ratio:\n    def __init__(self, num, den):\n        value = num / den  # löst bei Nenner 0 einen ZeroDivisionError aus\n        if den < 0:\n            num, den = -num, -den\n        g = gcd(num, den)\n        self.num = num // g\n        self.den = den // g\n\n    def __mul__(self, other):\n        return Ratio(self.num * other.num, self.den * other.den)\n\n    def __add__(self, other):\n        return Ratio(self.num * other.den + other.num * self.den, self.den * other.den)\n\n    def __eq__(self, other):\n        return isinstance(other, Ratio) and self.num == other.num and self.den == other.den\n\n    def __float__(self):\n        return self.num / self.den\n\n    def __str__(self):\n        return f"{self.num}/{self.den}"\n\nstage1 = Ratio(51, 17)\nstage2 = Ratio(38, 19)\nprint(stage1 * stage2, float(stage1 * stage2))\n',
   tests='''
ns, out = run()
R = ns.get("Ratio")
a = call(ns, "Ratio", 51, 17)
check(a.num == 3 and a.den == 1, "Ratio(51, 17) wird zu 3/1 gekürzt", "Ratio(51, 17) is reduced to 3/1")
b = call(ns, "Ratio", 4, -10)
check(b.num == -2 and b.den == 5 and safe(lambda: str(b)) == "-2/5", "Ratio(4, -10) = -2/5 (Nenner positiv)", "Ratio(4, -10) = -2/5 (denominator positive)")
p = safe(lambda: call(ns, "Ratio", 51, 17) * call(ns, "Ratio", 38, 19))
check(isinstance(p, R) and p.num == 6 and p.den == 1, "3/1 · 2/1 = 6/1", "3/1 · 2/1 = 6/1")
p2 = safe(lambda: call(ns, "Ratio", 1, 3) * call(ns, "Ratio", 3, 4))
check(isinstance(p2, R) and p2.num == 1 and p2.den == 4, "1/3 · 3/4 = 1/4", "1/3 · 3/4 = 1/4")
s = safe(lambda: call(ns, "Ratio", 1, 3) + call(ns, "Ratio", 1, 6))
check(isinstance(s, R) and s.num == 1 and s.den == 2, "1/3 + 1/6 = 1/2", "1/3 + 1/6 = 1/2")
check(safe(lambda: call(ns, "Ratio", 2, 4) == call(ns, "Ratio", 1, 2)) is True and safe(lambda: call(ns, "Ratio", 1, 3) == call(ns, "Ratio", 1, 2)) is False, "2/4 == 1/2, aber 1/3 != 1/2", "2/4 == 1/2, but 1/3 != 1/2")
check(approx(safe(lambda: float(call(ns, "Ratio", 1, 3))), 1 / 3) and safe(lambda: str(call(ns, "Ratio", 0, 7))) == "0/1", "float(1/3) ≈ 0.3333, Ratio(0, 7) = 0/1", "float(1/3) ≈ 0.3333, Ratio(0, 7) = 0/1")
check(raises(ZeroDivisionError, lambda: R(1, 0)), "Nenner 0 → ZeroDivisionError", "Denominator 0 → ZeroDivisionError")
check("gcd(" not in SOURCE.replace("def gcd(", "") or "math" not in SOURCE, "ggT selbst programmiert", "gcd programmed yourself")
''',
   require=["class", "magic"], refs=["10.7", "6.2a"])

ex(id="k10-matrix2", ch="10", lvl=3,
   title={"de": "Klasse für 2×2-Matrizen", "en": "Class for 2×2 matrices"},
   task={"de": "Schreiben Sie die Klasse `Matrix2(a, b, c, d)` für die Matrix $\\begin{pmatrix} a & b \\\\ c & d \\end{pmatrix}$ (Attribute `a`, `b`, `c`, `d`).\n- `det()`: Determinante $ad - bc$\n- `__add__`: Summe zweier Matrizen\n- `__mul__`: Ist `other` eine `Matrix2`, wird das Matrixprodukt berechnet; ist es eine Zahl (`int` oder `float`), wird jedes Element damit multipliziert. Prüfen Sie mit `isinstance`.\n- `inverse()`: die inverse Matrix ($\\frac{1}{\\det} \\begin{pmatrix} d & -b \\\\ -c & a \\end{pmatrix}$); bei det = 0 (singuläre Matrix) wird `None` zurückgegeben\n- `__eq__`: Gleichheit aller vier Elemente (mit einer Toleranz von 1e-9, weil Gleitkommazahlen im Spiel sind)\n- `__str__`: `[[1, 2], [3, 4]]`\n\nAlle Operationen liefern **neue** Objekte.",
         "en": "Write the class `Matrix2(a, b, c, d)` for the matrix $\\begin{pmatrix} a & b \\\\ c & d \\end{pmatrix}$ (attributes `a`, `b`, `c`, `d`).\n- `det()`: determinant $ad - bc$\n- `__add__`: sum of two matrices\n- `__mul__`: if `other` is a `Matrix2`, the matrix product is computed; if it is a number (`int` or `float`), each element is multiplied by it. Check with `isinstance`.\n- `inverse()`: the inverse matrix ($\\frac{1}{\\det} \\begin{pmatrix} d & -b \\\\ -c & a \\end{pmatrix}$); for det = 0 (singular matrix) `None` is returned\n- `__eq__`: equality of all four elements (with a tolerance of 1e-9, since floats are involved)\n- `__str__`: `[[1, 2], [3, 4]]`\n\nAll operations return **new** objects."},
   starter={"de": "class Matrix2:\n    def __init__(self, a, b, c, d):\n        self.a = a\n        self.b = b\n        self.c = c\n        self.d = d\n", "en": "class Matrix2:\n    def __init__(self, a, b, c, d):\n        self.a = a\n        self.b = b\n        self.c = c\n        self.d = d\n"},
   solution='class Matrix2:\n    def __init__(self, a, b, c, d):\n        self.a = a\n        self.b = b\n        self.c = c\n        self.d = d\n\n    def det(self):\n        return self.a * self.d - self.b * self.c\n\n    def __add__(self, other):\n        return Matrix2(self.a + other.a, self.b + other.b, self.c + other.c, self.d + other.d)\n\n    def __mul__(self, other):\n        if isinstance(other, Matrix2):\n            return Matrix2(self.a * other.a + self.b * other.c, self.a * other.b + self.b * other.d,\n                           self.c * other.a + self.d * other.c, self.c * other.b + self.d * other.d)\n        if isinstance(other, int) or isinstance(other, float):\n            return Matrix2(self.a * other, self.b * other, self.c * other, self.d * other)\n        return None\n\n    def inverse(self):\n        det = self.det()\n        if det == 0:\n            return None\n        return Matrix2(self.d / det, -self.b / det, -self.c / det, self.a / det)\n\n    def __eq__(self, other):\n        if not isinstance(other, Matrix2):\n            return False\n        return (abs(self.a - other.a) < 1e-9 and abs(self.b - other.b) < 1e-9\n                and abs(self.c - other.c) < 1e-9 and abs(self.d - other.d) < 1e-9)\n\n    def __str__(self):\n        return f"[[{self.a}, {self.b}], [{self.c}, {self.d}]]"\n\nM = Matrix2(4, 7, 2, 6)\nprint(M * M.inverse(), M * 2, M.det())\n',
   tests='''
ns, out = run()
X = ns.get("Matrix2")
M = call(ns, "Matrix2", 4, 7, 2, 6); N = call(ns, "Matrix2", 1, 2, 3, 4)
check(method(M, "det") == 10 and method(N, "det") == -2, "det: 10 bzw. −2", "det: 10 and −2")
s = safe(lambda: M + N)
check(isinstance(s, X) and (s.a, s.b, s.c, s.d) == (5, 9, 5, 10), "M + N = [[5, 9], [5, 10]]", "M + N = [[5, 9], [5, 10]]")
p = safe(lambda: M * N)
check(isinstance(p, X) and (p.a, p.b, p.c, p.d) == (25, 36, 20, 28), "M · N = [[25, 36], [20, 28]]", "M · N = [[25, 36], [20, 28]]")
k = safe(lambda: N * 2.5)
check(isinstance(k, X) and (k.a, k.b, k.c, k.d) == (2.5, 5.0, 7.5, 10.0) and (N.a, N.b) == (1, 2), "N · 2.5 skaliert alle Elemente, N bleibt unverändert", "N · 2.5 scales all elements, N stays unchanged")
I = safe(lambda: M * method(M, "inverse"))
check(safe(lambda: I == call(ns, "Matrix2", 1, 0, 0, 1)) is True, "M · M⁻¹ = Einheitsmatrix (Vergleich mit Toleranz)", "M · M⁻¹ = identity (comparison with tolerance)")
check(method(call(ns, "Matrix2", 1, 2, 2, 4), "inverse") is None, "Singuläre Matrix → None", "Singular matrix → None")
check(safe(lambda: N == call(ns, "Matrix2", 1, 2, 3, 5)) is False and safe(lambda: N == call(ns, "Matrix2", 1.5, 2, 3, 4)) is False and safe(lambda: N == call(ns, "Matrix2", 1, -2, 3, 4)) is False, "Matrizen, die sich in einem Element unterscheiden, sind ungleich", "Matrices differing in one element are not equal")
check(safe(lambda: str(N)) == "[[1, 2], [3, 4]]" and safe(lambda: N == "x") is False, "str(N) = '[[1, 2], [3, 4]]', Vergleich mit anderem Typ → False", "str(N) = '[[1, 2], [3, 4]]', comparison with another type → False")
''',
   require=["class", "magic", "isinstance"], refs=["10.7", "7.4", "6.3b"])

ex(id="k10-abstractsensor", ch="10", lvl=3,
   title={"de": "Abstrakte Sensorklasse", "en": "Abstract sensor class"},
   task={"de": "Alle Sensoren eines Prüfstands liefern Rohwerte, die in physikalische Größen umgerechnet werden. Definieren Sie die abstrakte Klasse `Sensor(ABC)`:\n- Konstruktor `__init__(self, name, unit)` speichert `name` und `unit`\n- abstrakte Methode `convert(raw)`: rechnet einen Rohwert um\n- konkrete Methode `read(raws)`: gibt die Liste der umgerechneten Werte einer Liste von Rohwerten in derselben Reihenfolge zurück (nutzt `convert`)\n- konkrete Methode `__str__`: z.B. `T1 [°C]`\n\nAbgeleitete Klassen (Konstruktor mit `super()`):\n- `LinearSensor(name, unit, gain, offset)`: convert $= \\mathit{gain} \\cdot \\mathit{raw} + \\mathit{offset}$\n- `PolySensor(name, unit, coeffs)`: convert $= \\sum_k \\mathit{coeffs}_k \\cdot \\mathit{raw}^k$ (Polynom, `coeffs` beginnt beim konstanten Glied)\n\nEine Unterklasse, die `convert` nicht implementiert, darf sich nicht instanziieren lassen.",
         "en": "All sensors of a test bench deliver raw values that are converted into physical quantities. Define the abstract class `Sensor(ABC)`:\n- constructor `__init__(self, name, unit)` stores `name` and `unit`\n- abstract method `convert(raw)`: converts one raw value\n- concrete method `read(raws)`: returns the list of converted values of a list of raw values in the same order (uses `convert`)\n- concrete method `__str__`: e.g. `T1 [°C]`\n\nDerived classes (constructor with `super()`):\n- `LinearSensor(name, unit, gain, offset)`: convert $= \\mathit{gain} \\cdot \\mathit{raw} + \\mathit{offset}$\n- `PolySensor(name, unit, coeffs)`: convert $= \\sum_k \\mathit{coeffs}_k \\cdot \\mathit{raw}^k$ (polynomial, `coeffs` starts with the constant term)\n\nA subclass that doesn't implement `convert` must not be instantiable."},
   starter={"de": "from abc import ABC, abstractmethod\n\nclass Sensor(ABC):\n    ...\n", "en": "from abc import ABC, abstractmethod\n\nclass Sensor(ABC):\n    ...\n"},
   solution='from abc import ABC, abstractmethod\n\nclass Sensor(ABC):\n    def __init__(self, name, unit):\n        self.name = name\n        self.unit = unit\n\n    @abstractmethod\n    def convert(self, raw):\n        pass\n\n    def read(self, raws):\n        return [self.convert(r) for r in raws]\n\n    def __str__(self):\n        return f"{self.name} [{self.unit}]"\n\n\nclass LinearSensor(Sensor):\n    def __init__(self, name, unit, gain, offset):\n        super().__init__(name, unit)\n        self.gain = gain\n        self.offset = offset\n\n    def convert(self, raw):\n        return self.gain * raw + self.offset\n\n\nclass PolySensor(Sensor):\n    def __init__(self, name, unit, coeffs):\n        super().__init__(name, unit)\n        self.coeffs = coeffs\n\n    def convert(self, raw):\n        total = 0\n        for k in range(len(self.coeffs)):\n            total += self.coeffs[k] * raw**k\n        return total\n\np = LinearSensor("p1", "bar", 0.01, -0.5)\nt = PolySensor("T1", "°C", [-20.0, 0.05, 1e-6])\nprint(p, p.read([50, 650]), t, t.read([1000]))\n',
   tests='''
ns, out = run()
S = ns.get("Sensor")
check(raises(TypeError, lambda: S("x", "y")), "Sensor selbst ist abstrakt", "Sensor itself is abstract")
lin = call(ns, "LinearSensor", "p1", "bar", 0.01, -0.5)
pol = call(ns, "PolySensor", "T1", "°C", [-20.0, 0.05, 1e-6])
check(isinstance(lin, S) and isinstance(pol, S) and safe(lambda: str(lin)) == "p1 [bar]" and safe(lambda: str(pol)) == "T1 [°C]", "Beide erben von Sensor; str: 'p1 [bar]', 'T1 [°C]'", "Both inherit from Sensor; str: 'p1 [bar]', 'T1 [°C]'")
r = method(lin, "read", [50, 650, 0])
check(isinstance(r, list) and all(approx(a, b) for a, b in zip(r, [0.0, 6.0, -0.5])) and len(r) == 3, "LinearSensor.read([50, 650, 0]) = [0.0, 6.0, −0.5]", "LinearSensor.read([50, 650, 0]) = [0.0, 6.0, −0.5]")
check(approx(method(pol, "convert", 1000), -20 + 50 + 1), "PolySensor.convert(1000) = 31.0", "PolySensor.convert(1000) = 31.0")
check("read" not in vars(ns["LinearSensor"]) and "read" not in vars(ns["PolySensor"]), "read() steht nur in der Basisklasse", "read() is only in the base class")
code = "class Broken(Sensor):\\n    pass\\n"
env = dict(ns); exec(code, env)
check(raises(TypeError, lambda: env["Broken"]("b", "-")), "Unterklasse ohne convert lässt sich nicht instanziieren", "A subclass without convert cannot be instantiated")
''',
   require=["class", "abc", "super"], refs=["10.8", "10.5"])

ex(id="k10-ringbuffer", ch="10", lvl=3,
   title={"de": "Ringpuffer für Messwerte", "en": "Ring buffer for readings"},
   task={"de": "Ein Mikrocontroller speichert nur die letzten `capacity` Messwerte. Schreiben Sie die Klasse `RingBuffer(capacity)`:\n- `push(value)`: fügt einen Wert hinzu; ist der Puffer voll, wird der **älteste** Wert verworfen\n- `__len__`: Anzahl der gespeicherten Werte (dann funktioniert `len(buffer)`)\n- `values()`: Liste der gespeicherten Werte vom ältesten zum neuesten (als Kopie – Änderungen an der Liste dürfen den Puffer nicht verändern)\n- `is_full()`\n- `mean()`: Mittelwert, `None` bei leerem Puffer\n- `trend()`: neuester minus ältester Wert (`None`, wenn weniger als zwei Werte gespeichert sind)\n\nSpeichern Sie die Werte intern in einem **protected** Attribut `_data`.",
         "en": "A microcontroller only keeps the last `capacity` readings. Write the class `RingBuffer(capacity)`:\n- `push(value)`: adds a value; if the buffer is full, the **oldest** value is discarded\n- `__len__`: number of stored values (then `len(buffer)` works)\n- `values()`: list of the stored values from oldest to newest (as a copy – changes to the list must not change the buffer)\n- `is_full()`\n- `mean()`: mean, `None` for an empty buffer\n- `trend()`: newest minus oldest value (`None` if fewer than two values are stored)\n\nStore the values internally in a **protected** attribute `_data`."},
   starter={"de": "class RingBuffer:\n    def __init__(self, capacity):\n        ...\n", "en": "class RingBuffer:\n    def __init__(self, capacity):\n        ...\n"},
   solution='class RingBuffer:\n    def __init__(self, capacity):\n        self.capacity = capacity\n        self._data = []\n\n    def push(self, value):\n        if len(self._data) == self.capacity:\n            self._data.pop(0)\n        self._data.append(value)\n\n    def __len__(self):\n        return len(self._data)\n\n    def values(self):\n        return self._data[:]\n\n    def is_full(self):\n        return len(self._data) == self.capacity\n\n    def mean(self):\n        if len(self._data) == 0:\n            return None\n        return sum(self._data) / len(self._data)\n\n    def trend(self):\n        if len(self._data) < 2:\n            return None\n        return self._data[-1] - self._data[0]\n\nbuf = RingBuffer(3)\nfor v in [1.0, 2.0, 3.0, 4.0]:\n    buf.push(v)\nprint(buf.values(), len(buf), buf.mean(), buf.trend())\n',
   tests='''
ns, out = run()
b = call(ns, "RingBuffer", 3)
check(hasattr(b, "_data") and safe(lambda: len(b)) == 0 and method(b, "mean") is None and method(b, "trend") is None, "Leerer Puffer: len 0, mean/trend None, Attribut _data", "Empty buffer: len 0, mean/trend None, attribute _data")
method(b, "push", 1.0)
check(method(b, "trend") is None and method(b, "is_full") is False, "Ein Wert: trend None, nicht voll", "One value: trend None, not full")
method(b, "push", 2.0)
check(approx(method(b, "trend"), 1.0), "Zwei Werte: trend = 1.0", "Two values: trend = 1.0")
for v in [3.0]:
    method(b, "push", v)
check(method(b, "is_full") is True and method(b, "values") == [1.0, 2.0, 3.0], "Nach drei Werten voll: [1.0, 2.0, 3.0]", "Full after three values: [1.0, 2.0, 3.0]")
method(b, "push", 4.0); method(b, "push", 6.0)
check(method(b, "values") == [3.0, 4.0, 6.0] and safe(lambda: len(b)) == 3, "Älteste Werte werden verworfen: [3.0, 4.0, 6.0]", "Oldest values are discarded: [3.0, 4.0, 6.0]")
check(approx(method(b, "mean"), 13 / 3) and approx(method(b, "trend"), 3.0), "mean ≈ 4.33, trend = 3.0", "mean ≈ 4.33, trend = 3.0")
v = method(b, "values"); v.append(99)
check(method(b, "values") == [3.0, 4.0, 6.0], "values() liefert eine Kopie", "values() returns a copy")
''',
   require=["class", "magic"], refs=["10.7", "10.6", "8.7"])
