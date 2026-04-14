from flask import Flask, jsonify
import json

app = Flask(__name__)

with open('airports.json', 'r') as f:
    airports = json.load(f)

@app.route('/airport/<icao>', methods=['GET'])
def get_airport(icao):
    icao_upper = icao.upper()

    for airport in airports:
        if airport.get('icao') == icao_upper:
            return jsonify({
                "icao": airport.get('icao'),
                "name": airport.get('name'),
                "city": airport.get('city'),
                "country": airport.get('country')
            }), 200
    
    return jsonify({
        "error": "Airport not found",
        "icao": icao_upper
    }), 404

if __name__ == '__main__':
    app.run(debug=True, host='127.0.0.1', port=5000)