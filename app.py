from flask import Flask

app = Flask(__name__)

@app.post("/api/try")
def trial():
  return{"blocks": [
    {
      "type": "section",
      "text": {
        "type": "mrkdwn",
        "text": ''' Please check if your question is answered in https://hackclub.slack.com/canvas/C077TSWKER0
        If not please post your question'''
      }
    }]}, 200

