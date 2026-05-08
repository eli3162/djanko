# You can customize this 404 page to your heart's content. The '404.py' page will always be the default 404 page
from djanko_lib import pyx, heading
file = pyx()
file.add(heading('404 Not Found'))
file.add(heading('Site made using djanko', level=4))

content = file.compile()