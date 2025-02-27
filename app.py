from flask import Flask, jsonify, request
import requests

app = Flask(__name__)


@app.route('/countries', methods=['GET'])
def get_countries():
    try:
        response = requests.get("https://restcountries.com/v3.1/all?fields=name,cca3")
        if response.status_code != 200:
            return jsonify({"error": "Failed to fetch countries"}), 500

        countries = response.json()


        sorted_countries = sorted(countries, key=lambda x: x['name']['common'])

        formatted_countries = [
            f"{country['name']['common']} ({country['cca3']})"
            for country in sorted_countries
        ]

        return jsonify(formatted_countries)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


@app.route('/country/<string:code>', methods=['GET'])
def get_country_details(code):
    try:
        response = requests.get(f"https://restcountries.com/v3.1/alpha/{code}")
        if response.status_code != 200:
            return jsonify({"error": "Failed to fetch country details"}), 500

        country = response.json()
        if not country:
            return jsonify({"error": "Country not found"}), 404

        country = country[0]  


        details = {
            "name": country['name']['common'],
            "capital": country.get('capital', ["N/A"])[0],
            "languages": list(country.get('languages', {}).values()),
            "currencies": [
                f"{currency['name']} ({currency['symbol']})"
                for currency in country.get('currencies', {}).values()
            ]
        }

        return jsonify(details)

    except Exception as e:
        return jsonify({"error": str(e)}), 500


if __name__ == '__main__':
    app.run(debug=True)
