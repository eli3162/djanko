from js import *
import asyncio
import pyodide_js
from pyodide.ffi import create_proxy
from pyscript import *

pressed_keys = set()

def on_keydown(event):
    pressed_keys.add(event.key)

def on_keyup(event):
    pressed_keys.discard(event.key)

keydown_proxy = create_proxy(on_keydown)
keyup_proxy = create_proxy(on_keyup)

document.addEventListener("keydown", keydown_proxy)
document.addEventListener("keyup", keyup_proxy)

def key_pressed(key_name):
    return key_name in pressed_keys

def get_mouse_position(event):
    global client_mouse_x, client_mouse_y
    client_mouse_x = event.clientX
    client_mouse_y = event.clientY

mouse_proxy = create_proxy(get_mouse_position)

document.addEventListener("mousemove", mouse_proxy)

client_mouse_x = 0
client_mouse_y = 0

def mouse_x():
    global client_mouse_x
    return client_mouse_x

def mouse_y():
    global client_mouse_y
    return client_mouse_y

def create_element(html):
    element = document.createElement("div")
    element.innerHTML = html
    document.body.appendChild(element)
    return element

def goto(element, x, y):
    rect = element.getBoundingClientRect()
    height = rect.height
    y_height = document.documentElement.clientHeight
    left = x
    y = y + (y_height - height)
    top = y_height - y
    element.style.left = f'{left}px'
    element.style.top = f'{top}px'
    document.body.style.overflow = "hidden"
    return(left, top)