# Uhrzeit-Sync

Eine kleine Web-App, die **nur** Uhrzeit und Datum einer Fitnessuhr (z. B. SB1435H von Müller)
per Bluetooth stellt. Keine Anmeldung, kein Konto, keine Datensammlung – alles andere läuft allein auf der Uhr.

## Benutzen

1. Seite auf einem **Android-Handy in Google Chrome** öffnen
   (iPhone: nur über die kostenlose Browser-App „Bluefy“, weil Safari kein Bluetooth kann).
2. Alte Uhren-App schließen/deinstallieren, Uhr **nicht** in den Bluetooth-Einstellungen koppeln.
3. „Uhr suchen & verbinden“ → Uhr auswählen → „Uhrzeit & Datum übertragen“.
4. Optional: Chrome-Menü → „Zum Startbildschirm hinzufügen“, dann sieht es aus wie eine normale App.

## Online stellen (GitHub Pages)

Web-Bluetooth funktioniert nur über `https://`. Am einfachsten:
GitHub → Repository → *Settings* → *Pages* → Branch auswählen, Ordner `/ (root)` → *Save*.
Danach ist die App unter `https://<benutzername>.github.io/<repository>/` erreichbar.

## Unterstützte Protokolle

Der Hersteller veröffentlicht sein Bluetooth-Protokoll nicht. Die App erkennt automatisch diese
verbreiteten Varianten (Befehle nach dem Open-Source-Projekt Gadgetbridge):

| Name in der App | Bluetooth-Dienst | Befehl |
|---|---|---|
| Typ A – Da Fit / Moyoung | `FEEA` | `FE EA 10 0A 31 <Zeitstempel GMT+8> 08` |
| Typ B – FitPro | `6E400001-…-CA9D` | `CD 00 09 12 01 01 00 04 <gepacktes Datum>` |
| Typ C – Lefun | `18D0` | `AB 0B 04 01 JJ MM TT hh mm ss <CRC8>` |
| Bluetooth-Standard | `1805` / `2A2B` | Current Time (10 Bytes) |

Passt keine Variante, zeigt „Erweitert / Fehlersuche → Protokoll kopieren“ alle Dienste der Uhr an.
Damit (oder mit einem Android-„Bluetooth-HCI-Snoop-Log“ der Original-App) lässt sich das
richtige Protokoll ergänzen.

## Dateien

- `index.html` – die komplette App
- `manifest.json`, `icon.svg`, `sw.js` – App-Symbol und Offline-Nutzung
