from flask import *
import os

JIT = True

app = Flask(__name__)
@app.route('/<path:subpath>')
def fetchfiles(subpath):
    global JIT
    filepath = os.path.join(os.getcwd(), subpath)
    if filepath.endswith('.py'):
        if JIT:
            importpath = subpath.replace('.py', '')
            exec(f'import {importpath}')
        
        filepath = filepath.replace('.py', '.html')
        with open(filepath, 'r') as f:
            content = f.read()
        return content
    else:
        return send_file(filepath)
        
@app.route('/')
def fetchindex():
    global JIT
    subpath = 'index.py'
    filepath = os.path.join(os.getcwd(), subpath)
    if filepath.endswith('.py'):
        if JIT:
            importpath = subpath.replace('.py', '')
            exec(f'import {importpath}')
        filepath = filepath.replace('.py', '.html')
        with open(filepath, 'r') as f:
            content = f.read()
        return content
    else:
        return send_file(filepath)

app.run(debug=True, port=3100)