from flask import Flask, request, abort
from gevent.pywsgi import WSGIServer
import json
import requests
from datetime import datetime
from zoneinfo import ZoneInfo
import os

fe2_url = os.getenv("FE2_URL")
auth = os.getenv("AUTH")
urldir = os.getenv("URLDIR")

app = Flask(__name__)


@app.route(urldir, methods=['POST'])
def webhook():
    if request.method == 'POST':
        indata = request.json
        endpoint = indata['end_device_ids']['device_id']
        volt = indata['uplink_message']['decoded_payload']['Supply_Voltage']
        reason = indata['uplink_message']['decoded_payload']['TX_Reason']
        alt = indata['uplink_message']['decoded_payload']['altitude']
        hdop = indata['uplink_message']['decoded_payload']['hdop']
        lat = indata['uplink_message']['decoded_payload']['latitude']
        long = indata['uplink_message']['decoded_payload']['longitude']
        gateway = indata['uplink_message']['rx_metadata'][0]['gateway_ids']['gateway_id']
        zulu = indata['uplink_message']['rx_metadata'][0]['time']
        time = datetime.fromisoformat(zulu.replace('Z', '+00:00')).astimezone(ZoneInfo("Europe/Zurich")).isoformat()

        outdata = {
            "authorization": auth,
            "address": endpoint,
            "timestamp": str(time),
            "lat": lat,
            "lng": long,
            "alt": alt,
            "heading": hdop
        }

        r = requests.post(fe2_url, data=json.dumps(outdata), headers={"Content-Type": "application/json"})

        print(outdata)

        return 'success', 200
    else:
        abort(400)


if __name__ == '__main__':
    http_server = WSGIServer(('', 5000), app)
    http_server.serve_forever()
    print("TTN to FE2 Bridge gestartet...")
