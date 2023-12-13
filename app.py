from flask import Flask, render_template, request
from google.cloud import translate_v2 as translate
import os

os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = 'key.json'

app = Flask(__name__)

translate_client = translate.Client()

default_lang_code = "es"

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/translate', methods=['POST'])
def translate_text():
    text_to_translate = request.form['text']
    try:
        translation = translate_client.translate(text_to_translate, target_language=default_lang_code)
        translated_text = translation['translatedText']
    except Exception as e:
        translated_text = f"An error occurred: {e}"
    return render_template('index.html', translation=translated_text)

if __name__ == '__main__':
    app.run(debug=True)
