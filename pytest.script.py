from djanko_lib_client import *
from js import *
import asyncio
import pyodide_js
from pyodide.ffi import create_proxy
import math, sys

async def main():
    element = document.getElementById("loading-element")
    sprite = document.getElementById("sprite")
    element.style.color = "red"
    element.textContent = "Pyodide Loaded"
    element.style.position = 'absolute'
    sprite.style.position = 'absolute'
    element.style.fontSize = "50px"
    element.style.left = '0px'
    element.style.top = '0px'
    x = 500
    y = 500
    run_speed = 3
    tracking_interval = 4
    rotation = 0
    marker = document.createElement("div")
    marker.innerHTML = '<p>.</p>'
    document.body.appendChild(marker)
    await asyncio.sleep(0.01)
    marker.style.position = 'absolute'

    while True:
        rotation = rotation + 2
        if key_pressed('c'):
            create_element('<p>p</p>')
        if key_pressed('w'):
            y = y - tracking_interval
        if key_pressed('a'):
            x = x - tracking_interval
        if key_pressed('s'):
            y = y + tracking_interval
        if key_pressed('d'):
            x = x + tracking_interval

        client_mouse_x = mouse_x()
        client_mouse_y = mouse_y()
        delta_x = client_mouse_x - x
        delta_y = client_mouse_y - y
        distance_away = math.sqrt(math.pow(delta_x, 2) + math.pow(delta_y, 2))
        element.textContent = 'Python running in the web browser'
        if distance_away < 100:
            while not run_speed > delta_x > -run_speed or not run_speed > delta_y > -run_speed:
                delta_y = delta_y / 2
                delta_x = delta_x / 2
            x = x - delta_x
            y = y - delta_y

        marker.style.top = y
        marker.style.left = x
        element.style.transform = f"rotate({rotation}deg)"
        #element.style.transition = f"transform {0.01}s ease"
        element.style.left = f"{x - 374}px"
        element.style.top = f"{y - 16}px"
        sprite.style.left = f"{x}px"
        sprite.style.top = f"{y}px"
        element.style.fontSize = f"{50}px"
        await asyncio.sleep(0.01)
main()

