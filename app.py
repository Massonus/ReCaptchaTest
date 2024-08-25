from flask import Flask, render_template, request, jsonify, redirect, url_for
from dotenv import load_dotenv
import os
import requests

# Загрузка переменных окружения из .env файла
load_dotenv()

app = Flask(__name__)


@app.route('/')
def index():
    site_key = os.getenv('RECAPTCHA_SITE_KEY')
    return render_template('index.html', site_key=site_key)


@app.route('/verify-captcha', methods=['POST'])
def verify_captcha():
    secret_key = os.getenv('RECAPTCHA_SECRET_KEY')
    response = request.json.get('response')
    verify_url = f'https://www.google.com/recaptcha/api/siteverify?secret={secret_key}&response={response}'
    verification_response = requests.post(verify_url)
    verification_result = verification_response.json()
    return jsonify(verification_result)


@app.route('/result')
def result():
    return render_template('result.html')


if __name__ == '__main__':
    app.run(debug=True)
