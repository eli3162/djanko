# compile.py allows you to compile your djanko site into static html files, so that you can also host your app on a static site, like Github Pages
import os, ast
from djanko_lib import serve_pyx
import configparser
config = configparser.RawConfigParser()
config.read('djanko_config.cfg')
settings = dict(config.items('compiler'))

compileignore = ast.literal_eval(settings.get('compilerignorelist'))
files = os.listdir()
compiletargets = []
try:
    os.mkdir('build')
except Exception as e:
    pass


for i in range(len(files)):
    if files[i].endswith('.py') and not files[i] in compileignore:
        docompile = True
        for j in range(len(compileignore)):
            if compileignore[j] in files[i]:
                docompile = False 
        if docompile:
            compiletargets.append(files[i])
            with open(os.path.join('build', files[i].replace('.py', '.html')), "w") as file:
                file.write(serve_pyx(files[i]))

print('Compiled targets', compiletargets)