# TTN to FE2 Bridge

Die TTN to FE2 Bridge wertet GPS-Daten die als Webhook von The Things Network kommen aus und sendet diese an einen FE2 Server als Positionsmeldung weiter.

## Unterstützte Tracker
- [ELV LoRaWAN® GPS Tracker ELV-LW-GPS1](https://de.elv.com/elv-bausatz-lorawan-gps-tracker-elv-lw-gps1-157519)

## Docker Environment Variable
|Key|Value|
|-----|-----|
|FE2-URL|Adresse des FE2 Servers inkl API Pfad /(https://alamos.exampe.com:9443//rest/external/http/position/v2/)|
|AUTH|Geheimnis das in der Externen Schnittstelle bei Gültiger Absender hinterlegt wird um sich gegenüber des FE2 Server zu Authentifizieren|
|URLDIR|Subordner an den der Webhook von TTN gesendet wird z.B. /webhook|
