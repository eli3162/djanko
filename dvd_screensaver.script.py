from djanko_lib_client import *
from js import *
import math, random, asyncio

async def main():
    sprite = document.getElementById("sprite")
    sprite.style.position = 'absolute'
    sprite.style.color = "blue"
    sprite.style.fontSize = "200px"
    await asyncio.sleep(0.01)
    height = sprite.getBoundingClientRect().height
    width = sprite.getBoundingClientRect().width
    x = 50
    y = 100
    rotation = random.randint(0, 360)
    speed = random.randint(5, 50)
    delta_x = math.sin(rotation * 3.14/180) * speed
    delta_y = math.cos(rotation * 3.14/180) * speed 
    while True:
        y_height = document.documentElement.clientHeight - height
        x_width = document.documentElement.clientWidth - width
        if not x_width > x >= 0 or not y_height > y >= 0:
            if (x_width > x >= 0) == False:
                delta_x = -1 * delta_x
            if (y_height > y >= 0) == False:
                delta_y = -1 * delta_y
        x = x + delta_x
        y = y + delta_y
        goto(sprite, x, y)
        await asyncio.sleep(0.01)
main()