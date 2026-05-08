from flask import *
from djanko_lib import *

app = Flask(__name__)
@app.route('/<path:subpath>')
def fetchfiles(subpath):
    try:
        if subpath.endswith('.py'):
            return serve_pyx(subpath)
        else:
            return send_file(subpath)
    except Exception as e:
        return serve_pyx('404.py')
        
@app.route('/')
def fetchindex():
    subpath = 'index.py'
    try:
        if subpath.endswith('.py'):
            return serve_pyx(subpath)
        else:
            return send_file(subpath)
    except Exception as e:
        return serve_pyx('404.py')

app.run(debug=True, port=80, host='0.0.0.0')