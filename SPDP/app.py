from flask import Flask, render_template, request
import requests
import json
app = Flask(__name__)

@app.route('/', methods=['GET', 'POST'])

def index():
    if request.method == 'POST':
        text = request.form['text']
        Traslate_language = request.form['target_language']
        Output_text = Traslate_text(text,Traslate_language)
        return render_template('index.html', Output_text=Output_text)
    else:
        return render_template('index.html')


def Traslate_text(text,target_language):
    api_url="https://v1.genr.ai/api/circuit-element/translate-text"
    response = requests.post(api_url, json={'text': text,'target_language':target_language})
    if response.status_code == 200:
        return json.loads(response.text)["output"]
    else:
        return None

if __name__ == '__main__':
    index.run(debug=True)