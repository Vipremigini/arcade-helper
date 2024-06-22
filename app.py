from flask import Flask

app = Flask(__name__)

@app.post("/api/try")
def trial():
  return{"blocks": [
    {
      "type": "section",
      "text": {
        "type": "mrkdwn",
        "text": "*It's 80 degrees right now.*"
      }
    }]}, 200

