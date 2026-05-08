from djanko_lib import pyx, heading
file = pyx()
file.add(heading('404 Not Found'))
file.add(heading('Site made using djanko', level=4))

content = file.compile()