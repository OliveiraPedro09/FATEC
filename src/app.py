from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('home.html')

@app.route('/info')
def sobre():
    return render_template('info.html')

if __name__ == "__main__":
    app.run(debug=True)
