# /// script
# requires-python = ">=3.14"
# dependencies = [
#     "flask>=3.1.3",
#     "python-minifier>=3.2.0",
# ]
# ///
from flask import *
from djanko_lib import *
from djanko_lib import serve_pyx as compile_pyx
import configparser, ast
import compile
config = configparser.RawConfigParser()
config.read('djanko_config.cfg')
settings = dict(config.items('server'))
compilersettings = dict(config.items('compiler'))
compileignore = ast.literal_eval(compilersettings.get('compilerignorelist'))
# Config
homepage = ast.literal_eval(settings.get('homepage'))
errorpage = ast.literal_eval(settings.get('errorpage'))
print('Homepage: ', homepage)
print('Errorpage: ', errorpage)

app = Flask(__name__)
@app.route('/<path:subpath>')
def fetchfiles(subpath):
    global errorpage
    subpath = subpath.replace('.html', '.py')
    try:
        if subpath.endswith('.py'):
            docompile = True
            for j in range(len(compileignore)):
                if compileignore[j] in subpath:
                    docompile = False 
            if docompile:
                return serve_pyx(subpath)
            else:
                return send_file(subpath)
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





