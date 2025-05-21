from flask import Flask, render_template
import os

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')  # or just return "Hello, World!"

def create_app():
    return app

if __name__ == '__main__':
    # Bind to PORT environment variable if defined (e.g. GalaxyCloud, Heroku)
    port = int(os.environ.get('PORT', 3000))
    app.run(host='0.0.0.0', port=port)
