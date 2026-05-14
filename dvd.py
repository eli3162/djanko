from djanko_lib import *
file = pyx()
file.title('DVD Screensaver')
file.add(heading('ETHAN', id='sprite', level=6))
file.add(python(pyscript('djanko_lib_client.py')))
file.add(python(pyscript('dvd_screensaver.script.py')))

content = file.compile()