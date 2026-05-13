from djanko_lib import *
file = pyx()
file.title('Pyodide Test')
file.add(heading('Loading...', id='loading-element'))
file.add(heading('.', id='sprite'))
file.add(python(pyscript('djanko_lib_client.py')))
file.add(python(pyscript('pytest.script.py')))

content = file.compile()