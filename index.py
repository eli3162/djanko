filename = 'index.html'
from djanko_lib import *
index = pyx()
index.title('DJanko Demo')
index.add(heading('DJanko Webpage'))
index.add(paragraph('This is a simple webpage generated using DJanko'))
index.add(paragraph('DJanko removes the need for learning HTML with Python'))
index.add(paragraph('example image:'))
index.add(image('/dango.png', alt=' example image'))
index.add(paragraph(link('/', 'example link')))
index.add(paragraph('example headings:'))
index.add(heading('Heading 1', level=1))
index.add(heading('Heading 2', level=2))
index.add(heading('Heading 3', level=3))
index.add(heading('Heading 4', level=4))
index.add(heading('Heading 5', level=5))
index.add(heading('Heading 6', level=6))

with open(filename, 'w') as f:
    f.write(index.compile())
