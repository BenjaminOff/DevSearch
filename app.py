from flask import Flask, render_template, request, jsonify, redirect, url_for, flash, session
from flask_babel import Babel
from flask_cors import CORS
import os
import requests
from werkzeug.security import generate_password_hash, check_password_hash

app = Flask(__name__)
CORS(app)
app.config['BABEL_DEFAULT_LOCALE'] = 'en'
app.config['BABEL_SUPPORTED_LOCALES'] = ['en', 'fr']
app.config['SECRET_KEY'] = 'your_secret_key_here'
babel = Babel(app)

# In-memory user store (for demo purposes only)
users = {}

def get_locale():
    return request.accept_languages.best_match(app.config['BABEL_SUPPORTED_LOCALES'])

babel = Babel(app, locale_selector=get_locale)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/search')
def search():
    query = request.args.get('q', '')
    locale = request.args.get('lang') or get_locale()
    if locale not in app.config['BABEL_SUPPORTED_LOCALES']:
        locale = app.config['BABEL_DEFAULT_LOCALE']
    if not query:
        return jsonify([])

    GOOGLE_API_KEY = os.getenv('GOOGLE_API_KEY')
    GOOGLE_CX = os.getenv('GOOGLE_CX')

    if not GOOGLE_API_KEY or not GOOGLE_CX:
        return jsonify([])

    params = {
        'key': GOOGLE_API_KEY,
        'cx': GOOGLE_CX,
        'q': query,
        'lr': 'lang_' + locale if locale in ['en', 'fr'] else '',
        'num': 10
    }
    response = requests.get('https://www.googleapis.com/customsearch/v1', params=params)
    results = []
    if response.status_code == 200:
        data = response.json()
        for item in data.get('items', []):
            results.append({
                'title': item.get('title'),
                'content': item.get('snippet'),
                'link': item.get('link')
            })
    return jsonify(results)

@app.route('/register', methods=['GET', 'POST'])
def register():
    if request.method == 'POST':
        username = request.form.get('username')
        password = request.form.get('password')
        if not username or not password:
            flash('Please provide both username and password.')
            return redirect(url_for('register'))
        if username in users:
            flash('Username already exists.')
            return redirect(url_for('register'))
        hashed_password = generate_password_hash(password)
        users[username] = hashed_password
        flash('Account created successfully! Please log in.')
        return redirect(url_for('index'))
    return render_template('register.html')

if __name__ == '__main__':
    app.run(debug=True)