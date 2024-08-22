from flask import Flask, request

app = Flask(__name__)

@app.route('/add', methods=['POST'])
def add_values():
    if not request.is_json:
        return {'error': 'Content-Type must be application/json'}, 400
    data = request.json
    if not isinstance(data['num1'], (int, float)) or not isinstance(data['num2'], (int, float)):
        return {'error': 'Bad data, values must be int or float'}, 400
    return {'result': data['num1'] + data['num']}


if __name__ == '__main__':
    app.run(debug=True)