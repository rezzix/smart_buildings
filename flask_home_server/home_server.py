from flask import Flask
from flask import render_template

app = Flask(__name__)

@app.route('/')
def hello_world():
   return render_template('index.html')

@app.route('/accueil')
def accueil():
   return render_template('accueil.html')

@app.route('/motor')
def motor():
   return "motor running"

@app.route('/light')
def light():
   return "light shining"

if __name__ == '__main__':
   app.run(host='0.0.0.0')
