from flask import Flask, render_template

app = Flask(__name__)


@app.route('/')
def index():
    return render_template('layout.html', nums=[1, 2, 3, 4])


if __name__ == '__main__':
    app.run(debug=True)
