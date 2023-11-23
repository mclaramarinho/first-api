from get_data import get_data
from flask import Flask, request, make_response

app = Flask(__name__)


@app.route('/veiculos')
def exec():
    name = request.args.get("name")
    res = make_response(get_data(name))
    res.status_code = 201
    return res
