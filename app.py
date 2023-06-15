import os
import openai
from flask import Flask, redirect, render_template, request, url_for

app = Flask(__name__)
openai.api_key = os.getenv("OPENAI_API_KEY")
openai.api_type = "azure"
openai.api_base = os.getenv("ENDPOINT")
openai.api_version = "2023-03-15-preview"


@app.route("/", methods=("GET", "POST"))
def index():
    text = request.json["text"]
    response = openai.ChatCompletion.create(
        engine=os.getenv("MODEL"),
        temperature=0.7,
        max_tokens=120,
        messages=[
        {"role": "system", "content": "You are a helpful assistant. Summarize the following text in 60 words or less."},
            {"role": "user", "content": text}
        ]
    )
    return response.choices[0].message.content

    # result = request.args.get("result")
    # return result
