from flask import Flask, jsonify, request

app = Flask(__name__)


@app.route("/<string:name>")
def dummy_api(name: str):
    return jsonify(data=name), 200


if __name__ == "__main__":
    app.run()