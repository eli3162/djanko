# /// script
# requires-python = ">=3.14"
# dependencies = [
#     "flask>=3.1.3",
# ]
# ///
from flask import *
from djanko_lib import *
from djanko_lib import serve_pyx as compile_pyx
compile_pyx('compile.py')

app = Flask(__name__)
@app.route('/<path:subpath>')
def fetchfiles(subpath):
    subpath = subpath.replace('.html', '.py')
    try:
        if subpath.endswith('.py'):
            return serve_pyx(subpath)
        else:
            return send_file(subpath)
    except Exception as e:
        return serve_pyx('404.py')
        
@app.route('/')
def fetchindex():
    try:
        return serve_pyx('index.py')
    except Exception as e:
        return serve_pyx('404.py')

app.run(debug=True, port=80, host='0.0.0.0')