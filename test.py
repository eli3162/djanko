from djanko_lib import pyx, heading, paragraph, image, link, style
file = pyx()
file.title('Candy')
file.add(style('picture', ['width: 500px', 'length: 500px']))
file.add(heading('Candy Pictures'))
file.add(image('/dango.png', alt='Dango Candy', styles='picture'))
file.add(heading('YAY!'))
content = file.compile()