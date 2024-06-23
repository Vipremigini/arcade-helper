from flask import Flask, request
import cohere
import os
from openai import OpenAI

bot = cohere.Client("VNPtolkc0NSINvIbVcKc3cmn9SMp2X4OzZjUVMZL")
client = OpenAI(
    # This is the default and can be omitted
    api_key= "A0SO2U3QRRBRAQWO0CBUFSJK00VHCQGBP30BL18U834PZ4FACE00W60VFJVD8EDW")

app = Flask(__name__)

@app.post("/api/try")
def trial():
  response = client.chat.completions.create(
    messages=[
        {
            "role": "user",
            "content": "You are a software engineer that wants to bring joy through chaos. Come up with something different every time. Please propose a funky simple project that will take under 6 hours to complete in 1 quick sentence. Keep it at less than 15 words. The funkier, stupidier, and sillier your ideas the better. Think out of the box, and do not propose ideas that do nothing but generate text, like a joke or dance move generator. Random sound effect generators are boring, do not suggest them. Be very creative, do not suggest projects that are too simple.",
        }
    ],
    model="gpt-3.5-turbo",
)

  return{"blocks": [
    {
      "type": "section",
      "text": {
        "type": "mrkdwn",
        "text": response.choices[0].message.content
      }
    }]}, 200

