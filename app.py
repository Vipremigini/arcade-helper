from flask import Flask

app = Flask(__name__)

@app.post("/api/try")
def trial():
  data = request.get_json()
  name = data["user_id"]
  return{"blocks": [
    {
      "type": "section",
      "text": {
        "type": "mrkdwn",
        "text": "Hi, " + name
      }
    }]}, 200

