# parse_time
- ungültige eingabe ("9:5"), (datentyp)
- normales beispiel ("14:05")
- grenzwert ("23:59")
- über grenzwert ("30:80")

# parse_measurement
- ungültiger datentyp
- eingabe aber mehr leerzeichen
- eingabe aber mit 4 feldern

# filter_by_temperature
- ungültiger datentyp
- reihenfolge bleibt gleich
- Dopplungen bleiben vorhanden
- Grenzen überschreiten
- eingabe liste bleibt unverändert
- lower > upper funktioniert nicht
- Ergebnis ist liste

# average_temperature
- ungültiger datentyp
- city name aber andere klein und großschreibung
- keine messung = valueError
- eingabe bleibt gleich

# hottest_measurement
- ungültiger datentyp
- leer = valueError
- eingabe bleibt gleich
- bei mehrereren gleichen ausgaben (temperatur") kommt das mit frühere uhrzeit, sonst das erste