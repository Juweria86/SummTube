from flask import Flask
from flask import render_template, url_for

app = Flask(__name__)

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html')

@app.route("/url_process")
def url_process():
    return render_template('url_process.html')


if __name__ == '__main__':
    app.run(debug=True)