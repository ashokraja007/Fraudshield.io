from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/url')
def url_check():
    return render_template('url.html')

if __name__ == '__main__':
    app.run(debug=True)
