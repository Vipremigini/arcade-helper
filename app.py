from flask import Flask, request
import threading
import requests


app = Flask(__name__)

@app.post("/api/try")
def trial():
    sendurl = request.form.get("response_url")
    send = { "rurl" = sendurl }
    requests.post(, json=send)
    return {"blocks": [
    {
      "type": "section",
      "text": {
        "type": "mrkdwn",
        "text": "Processing"
      }
    }]}

