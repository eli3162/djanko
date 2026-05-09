# /// script
# requires-python = ">=3.14"
# dependencies = [
#     "flask>=3.1.3",
# ]
# ///
from flask import *
from djanko_lib import *
from djanko_lib import serve_pyx as compile_pyx
import configparser
compile_pyx('compile.py')
config = configparser.RawConfigParser()
config.read('config.cfg')
settings = dict(config.items('server'))

# Config
homepage = settings.get('homepage')
errorpage = settings.get('errorpage')

app = Flask(__name__)
@app.route('/<path:subpath>')
def fetchfiles(subpath):
    global errorpage
    subpath = subpath.replace('.html', '.py')
    try:
        if subpath.endswith('.py'):
            return serve_pyx(subpath)
        else:
            return send_file(subpath)
    except Exception as e:
        return serve_pyx(errorpage)
        
@app.route('/')
def fetchindex():
    global errorpage, homepage
    try:
        return serve_pyx(homepage)
    except Exception as e:
        return serve_pyx(errorpage)

app.run(debug=settings.get('debug'), port=settings.get('port'), host='0.0.0.0')