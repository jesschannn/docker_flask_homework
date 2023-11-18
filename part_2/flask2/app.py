from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/')
def home():
    return f'Welcome to my Flask Endpoint :)'

@app.route('/pets', methods=['GET'])
def pets_get():
    number = request.args.get('number', '?')
    pet = request.args.get('pet', '?')
    return jsonify({'error': 'Invalid JSON'}), 400

@app.route('/feeling', methods=['GET'])
def feeling_get():
    emotion = request.args.get('emotion', 'nothing')
    return jsonify({'message': f'Why are you feeling {emotion}?'})

if __name__ == '__main__':
    app.run(debug=True, host='0.0.0.0', port=5002)
