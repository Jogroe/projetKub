from flask import Flask, request, jsonify
from werkzeug.urls import url_quote

app = Flask(__name__)

data = []

@app.route('/data', methods=['GET'])
def get_data():
    return jsonify(data)

@app.route('/data', methods=['POST'])
def add_data():
    new_entry = request.json
    data.append(new_entry)
    return jsonify({'message': 'Données ajoutées avec succès !'})

if __name__ == '__main__':
    app.run(debug=True)