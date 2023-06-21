# TTN to FE2 Bridge

Die TTN to FE2 Bridge wertet GPS-Daten die als Webhook von The Things Network kommen aus und sendet diese an einen [Alamos FE2 Server](https://alamos.gmbh/) als Positionsmeldung weiter.

## Unterstützte Tracker
- [ELV LoRaWAN® GPS Tracker ELV-LW-GPS1](https://de.elv.com/elv-bausatz-lorawan-gps-tracker-elv-lw-gps1-157519)


## Docker Environment Variable
|Key|Value|
|-----|-----|
|FE2-URL|Adresse des FE2 Servers inkl API Pfad /(https://alamos.exampe.com:9443/rest/external/http/position/v2/)|
|AUTH|Geheimnis das in der Externen Schnittstelle bei Gültiger Absender hinterlegt wird um sich gegenüber des FE2 Server zu Authentifizieren|
|URLDIR|Subordner an den der Webhook von TTN gesendet wird z.B. /webhook|

## The Things Network
Der Webhook von TTN wird am Port 5000 erwartet.

#### Payload Parser
[ELV LoRaWAN® GPS Tracker ELV-LW-GPS1](https://github.com/lasergraph/ttn-to-fe2-bridge/blob/e07ee6f1cc6b7f95129ffa3849a7f9500e305adf/ttn/ttn_payload-parser.js)

#### Webhook Konfiguration:
<img src="https://raw.githubusercontent.com/lasergraph/ttn-to-fe2-bridge/00d033aedc362003f727467202454ac7c93857b3/ttn/config_webhook.png">
