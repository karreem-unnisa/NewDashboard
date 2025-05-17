from flask import Flask, render_template, request
import requests
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
NEWS_API_KEY = os.getenv('NEWS_API_KEY')

@app.route('/', methods=['GET', 'POST'])
def index():
    query = None
    articles = []

    if request.method == 'POST':
        query = request.form.get('query')
        url = f"https://newsapi.org/v2/everything?q={query}&language=en&sortBy=publishedAt&apiKey={NEWS_API_KEY}"
    else:
        # Show top headlines if no search query is made
        url = f"https://newsapi.org/v2/top-headlines?country=us&apiKey={NEWS_API_KEY}"

    response = requests.get(url)
    data = response.json()
    articles = data.get('articles', [])

    return render_template('index.html', articles=articles, query=query or "")

if __name__ == '__main__':
    app.run(debug=True)

if __name__ == '__main__':
    port = int(os.environ.get('PORT', 5000))
    app.run(host='0.0.0.0', port=port)