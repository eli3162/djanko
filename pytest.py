from djanko_lib import *
file = pyx()
file.title('Pyodide Test')
file.add(heading('Loading...', id='loading-element'))
file.python(pyscript('pyscript.script.py'))

content = file.compile()