import os
class pyx:
    html = '<!DOCTYPE html><html lang="en"><head><meta charset="UTF-8"></head><body></body></html>'
    def add_style(self, href):
        self.html = self.html.replace('</head>', f'<link rel="stylesheet" href="{href}"></head>')
    def add_script(self, src):
        self.html = self.html.replace('</head>', f'<script src="{src}"></script></head>')
    def add_metadata(self, metadata):
        self.html = self.html.replace('</head>', f'{metadata}</head>')
    def add(self, content):
        self.html = self.html.replace('</body>', f'{content}</body>')
    def compile(self):
        return self.html
    def title(self, title):
        self.html = self.html.replace('</head>', f'<title>{title}</title></head>')
    def lang(self, lang):
        self.html = self.html.replace('<html', f'<html lang="{lang}"')
    def charset(self, charset):
        self.html = self.html.replace('<head>', f'<head><meta charset="{charset}">')
    def viewport(self, content):
        self.html = self.html.replace('<head>', f'<head><meta name="viewport" content="{content}">')

def paragraph(text, styles=None):
    if styles:
        return (f'<p class="{styles}">{text}</p>')
    return (f'<p>{text}</p>')
def heading(text, level=1, styles=None):
    if styles:
        return (f'<h{level} class="{styles}">{text}</h{level}>')
    return (f'<h{level}>{text}</h{level}>')
def image(src, alt='', styles=None):
    if styles:
        return (f'<img src="{src}" alt="{alt}" class="{styles}">')
    return (f'<img src="{src}" alt="{alt}">')
def link(href, text, styles=None):
    if styles:
        return (f'<a href="{href}" class="{styles}">{text}</a>')
    return (f'<a href="{href}">{text}</a>')
def br():
    return '<br>'
def hr():
    return '<hr>'

def style(name, value):
    css = '.' + name + ' { '
    for i in range(len(value)):
        css += f'{value[i]};'
    css += '}'
    css = f'<style>{css}</style>'
    return css

def serve_pyx(filename):
    output_variables = {}
    filename = os.path.join(os.getcwd(), filename)
    with open(filename, 'r') as f:
        pyxcode = f.read()
    exec(pyxcode, output_variables)
    return output_variables.get('content')
