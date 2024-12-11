from flask import Flask, request, jsonify

app = Flask(__name__)

@app.route('/add', methods=['GET'])
def add_numbers():
    a = request.args.get('a', type=float)
    b = request.args.get('b', type=float)
    if a is not None and b is not None:
        return jsonify({'result': a + b})
    else:
        return jsonify({'error': 'Please provide both a and b as query parameters'}), 400

if __name__ == '__main__':
    app.run(debug=True)
