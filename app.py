from flask import *
import os
from djanko_lib import *

JIT = True

app = Flask(__name__)
@app.route('/<path:subpath>')
def fetchfiles(subpath):
    if subpath.endswith('.py'):
        return serve_pyx(subpath)
    else:
        return send_file(subpath)
        
@app.route('/')
def fetchindex():
    subpath = 'index.py'
    if subpath.endswith('.py'):
        return serve_pyx(subpath)
    else:
        return send_file(subpath)

app.run(debug=True, port=80, host='0.0.0.0')