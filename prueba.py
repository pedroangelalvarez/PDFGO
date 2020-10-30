from flask import Flask, render_template, request
from webui import WebUI
app = Flask(__name__)
ui = WebUI(app, debug=True)
@app.route("/")
def index():
    return render_template('index.html', title='Bienvenido')
    return "Hello world!", 200
if __name__ == "__main__":
    ui.run()
