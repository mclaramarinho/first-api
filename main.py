from get_data import get_data
from flask import Flask, request

app = Flask(__name__)


@app.route('/veiculos')
def exec():
    name = request.args.get("name")
    return get_data(name)