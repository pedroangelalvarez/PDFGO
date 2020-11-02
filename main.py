# -*- coding:utf-8 -*-
from webui import WebUI # Add WebUI to your imports
from flask import Flask,jsonify, render_template, request

app = Flask(__name__)
ui = WebUI(app, debug=True) # Create a WebUI instance

@app.route('/get_file')
def get_file():
  word = request.args.get('file')
  print(word)
  return jsonify({'html':getFile(word)})

@app.route('/')
def index():
    return render_template('index.html')

# all of your standard flask logic
if __name__ == '__main__':
  ui.run() #replace app.run() with ui.run(), and that's it


'''
from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')
'''
