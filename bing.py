from bing import Flask, render_template
from geopy.geocoders import Nominatim

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/location')
def location():
    geolocator = Nominatim(user_agent="geoapiExercises")
    location = geolocator.geocode("175 5th Avenue NYC")
    return str(location.latitude) + ", " + str(location.longitude)

if __name__ == '__main__':
    app.run(debug=True)
