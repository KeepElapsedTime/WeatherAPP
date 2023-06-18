from flask import Flask, render_template, request
import requests

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/weather.html', methods=['POST'])
def weather():
    params = {
        "Authorization": "your-token-here",
        "locationName": request.form['city'],
    }
    url = f'https://opendata.cwb.gov.tw/api/v1/rest/datastore/F-C0032-001'
    response = requests.get(url, params=params)
    data = response.json()
    if response.status_code == 401 :
        weather_data = {
            'city': request.form['city'],
            'temperature': 0,
            'description': 0,
            'error': 401,
            'image_value': 0
        }
    elif data["records"]["location"] == [] :
        weather_data = {
            'city': request.form['city'],
            'temperature': 0,
            'description': 0,
            'error': 404,
            'image_value': 0
        }
    else:
        weather_elements = data["records"]["location"][0]["weatherElement"]
        min_tem = weather_elements[2]["time"][0]["parameter"]["parameterName"]
        max_tem = weather_elements[4]["time"][0]["parameter"]["parameterName"]
        tem_range = min_tem + " to " + max_tem
        comfort = weather_elements[3]["time"][0]["parameter"]["parameterName"]
        weather_state = weather_elements[0]["time"][0]["parameter"]["parameterName"]
        image_key = weather_elements[0]["time"][0]["parameter"]["parameterValue"]
        des = comfort + " 的 " + weather_state
        weather_data = {
            'city': data["records"]["location"][0]["locationName"],
            'temperature': tem_range,
            'description': des,
            'error': response.status_code,
            'image_value': image_key
        }
    return render_template('weather.html', weather=weather_data)

if __name__ == '__main__':
    app.run(port=3333)