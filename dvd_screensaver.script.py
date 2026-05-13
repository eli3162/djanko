from djanko_lib_client import *
from js import *
import asyncio
import math, sys

async def main():
    sprite = document.getElementById("sprite")
    sprite.style.fontSize = "200px"
    sprite.style.position = 'absolute'
    x = 50
    y = 50
    rotation = 45
    x_width = window.innerWidth - 720
    y_width = window.innerHeight - 350
    speed = 10
    while True:
        x_width = window.innerWidth - 720
        y_width = window.innerHeight - 350
        sprite.style.color = "blue"
        if x_width > x >= 0 and y_width > y >= 0:
            pass
        else:
            rotation = rotation + 90
            if rotation > 360:
                rotation = rotation - 360
        x = x + math.sin(rotation * 3.14/180) * speed
        y = y + math.cos(rotation * 3.14/180) * speed
        sprite.style.left = f"{x}px"
        sprite.style.top = f"{y}px"
        await asyncio.sleep(0.01)
main()