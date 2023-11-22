from flask import Flask, render_template, request
import requests

url='https://api.waqi.info/v2/search/'

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("index.html")

@app.route('/aqiApp', methods = ['POST'])
def get_weather_data():
    param = {'keyword': request.form.get('city'),
             'token': request.form.get('key')}
    res = requests.get(url, params = param)
    data = res.json()
    return f"Data: {data}"


if __name__ == "__main__":
    app.run(host ='0.0.0.0')
