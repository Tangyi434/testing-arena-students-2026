#parse_time
-eingabe ("xx:xx")
-normales beistpiel ("12:11")
-grenzwert ("23:59")
-formatierung (int)

#parse_measurement
- eingabe mit 4 felder
- formatierung (str)
- Zeile muss aus genau drei durch ; getrennten Feldern bestehen
-  Leerzeichen nach der drei Felder werden entfernt

#filter_by_temperatur
- Die Grenzen sind inklusive: lower <= temperature <= upper.
- Die Reihenfolge der Messungen bleibt erhalten.
- Doppelte bzw. identische Messungen bleiben doppelt vorhanden.
- Die übergebene Liste wird nicht verändert.
- Ist lower > upper, wird ValueError ausgelöst.
- Das Ergebnis ist eine neue Liste.

#average_temperature
- Es werden ausschließlich Messungen berücksichtigt, deren Stadtname exakt city entspricht.
- Städtenamen werden case-sensitive verglichen. "Köln" und "köln" sind also unterschiedliche Namen.
- Der Mittelwert wird über alle passenden Messungen gebildet.
- Gibt es keine Messung für die angegebene Stadt, wird ValueError ausgelöst.
- Die Eingabedaten werden nicht verändert.

#hottest_measurement
- Gibt es nur eine eindeutige höchste Temperatur, wird diese Messung zurückgegeben.
- Haben mehrere Messungen dieselbe höchste Temperatur, wird die Messung mit der frühesten Uhrzeit zurückgegeben.
- Haben mehrere Messungen sowohl dieselbe höchste Temperatur als auch dieselbe Uhrzeit, bleibt die zuerst vorkommende dieser
- Messungen maßgeblich.
- Für eine leere Sequenz wird ValueError ausgelöst.
- Die Eingabedaten werden nicht verändert.