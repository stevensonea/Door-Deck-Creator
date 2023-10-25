from PIL import Image 
from PIL import ImageDraw
import pandas as pd
import random

filepaths = [
    'pictures/original/axolotl.png',
    'pictures/original/bee.png',
    'pictures/original/cat.png',
    'pictures/original/cow.png',
    'pictures/original/creeper.png',
    'pictures/original/dog.png',
    'pictures/original/ender_dragon.png',
    'pictures/original/frog.png',
    'pictures/original/glow_squid.png',
    'pictures/original/goat.png',
    'pictures/original/iron_golem.png',
    'pictures/original/pig.png',
    'pictures/original/polar_bear.png',
    'pictures/original/turtle.png',
    'pictures/original/villager.png',
    'pictures/original/witch.png',
    'pictures/original/zombie_piglin.png',
    'pictures/original/blaze.png',
    'pictures/original/mooshroom.png'
]

mobs = [
    'axolotl',
    'bee',
    'cat',
    'cow',
    'creeper',
    'dog',
    'ender_dragon',
    'frog',
    'glow_squid',
    'goat',
    'iron_golem',
    'pig',
    'polar_bear',
    'turtle',
    'villager',
    'witch',
    'zombie_piglin',
    'blaze',
    'mooshroom'
]

for i in range(0,len(filepaths)):
    image = Image.open(filepaths[i])
    bounds = image.getbbox()
    I1 = ImageDraw.Draw(image)
    image.save('pictures/singles/' + mobs[i] + '.png')