from flask import Flask, request, jsonify

app = Flask(__name__)

data = []

@app.route('/')
def hello():
    return f'Hello restart !'

@app.route('/get', methods=['GET'])
def get_data():
    return jsonify(data)

@app.route('/post', methods=['POST'])
def add_data():
    new_entry = request.json
    data.append(new_entry)
    return jsonify({'message': 'Données ajoutées avec succès !'})

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000, debug=True)