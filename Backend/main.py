from flask import Flask, request, jsonify
import requests

app = Flask(__name__)

@app.route("/")
def hello_world():
        return "hello world!"

@app.route("/sum")
def sum():
    num1 = request.args.get("num1", type=int)
    num2 = request.args.get("num2", type=int)

    sum_result = {
        'sum': num1 + num2
    }
    return jsonify(sum_result)

@app.route("/lot")
def parkinglot():
    name = request.args.get("name")

    if name is None:
        return jsonify({
            'message:': 'missing title parameter!'
        })

    url = "https://openlibrary.org/search.json?q=" + title
    
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()

        top_ten = []

        for result in data['docs']:
            top_ten.append(result["title"])

        top_ten = top_ten[:10]

        return jsonify({"results": top_ten})

if __name__ == "__main__":
    app.run(host='0.0.0.0', port=3000, debug=True)