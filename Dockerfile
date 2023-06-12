FROM python:alpine3.18

#Ordner erstellen
RUN mkdir /opt/scripts && mkdir /opt/scripts/webhook

#Python Pakete installieren
RUN pip3 install flask gevent datetime requests tzdata

#Dateien kopieren
COPY hook.py /opt/scripts/webhook/

#env
ENV FE2_URL="https://URL:PORT/rest/external/http/position/v2"
ENV AUTH="secret"
ENV URLDIR="/webhook"
#Port für Webook
EXPOSE 5000

ENTRYPOINT python3 /opt/scripts/webhook/hook.py
