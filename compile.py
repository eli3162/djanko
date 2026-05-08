# compile.py allows you to compile your djanko site into static html files, so that you can also host your app on a static site, like Github Pages
import os
from djanko_lib import serve_pyx
files = os.listdir()
compiletargets = []
compileignore = ['compile.py', 'app.py', 'djanko_lib.py']
try:
    os.mkdir('build')
except Exception as e:
    pass

for i in range(len(files)):
    if files[i].endswith('.py') and not files[i] in compileignore:
        compiletargets.append(files[i])
        with open(os.path.join('build', files[i].replace('.py', '.html')), "w") as file:
            file.write(serve_pyx(files[i]))

print('Compiled targets', compiletargets)