from PIL import Image
import math

filepaths = [
    'pictures/singles/axolotl.png',
    'pictures/singles/bee.png',
    'pictures/singles/cat.png',
    'pictures/singles/cow.png',
    'pictures/singles/creeper.png',
    'pictures/singles/dog.png',
    'pictures/singles/ender_dragon.png',
    'pictures/singles/frog.png',
    'pictures/singles/glow_squid.png',
    'pictures/singles/goat.png',
    'pictures/singles/iron_golem.png',
    'pictures/singles/pig.png',
    'pictures/singles/polar_bear.png',
    'pictures/singles/turtle.png',
    'pictures/singles/villager.png',
    'pictures/singles/witch.png',
    'pictures/singles/zombie_piglin.png',
    'pictures/singles/blaze.png',
    'pictures/singles/mooshroom.png'
]

IMAGE_PER_PAGE = 6
NUMBER_OF_PAGES = math.floor(len(filepaths / IMAGE_PER_PAGE))
REMAINDER = len(filepaths) % IMAGE_PER_PAGE




"""
image1 = Image.open(filepaths[0])
image2 = Image.open(filepaths[0])
image3 = Image.open(filepaths[0])
image4 = Image.open(filepaths[0])
image5 = Image.open(filepaths[0])
image6 = Image.open(filepaths[0])

w1, h1 = image1.size
w2, h2 = image2.size
w3, h3 = image3.size
w4, h4 = image4.size
w5, h5 = image5.size
w6, h6 = image6.size

w = max(w1, w2, w3, w4)
h = max(h1, h2, h3, h4)

newImage = Image.new('RGB', (w*2, h*3))

newWidth, newHeight = newImage.size
xMargin = 0 #int(newWidth * 0.05)
yMargin = 0 #int(newHeight * 0.05)

newImage.paste(image1, (xMargin, yMargin))
newImage.paste(image2, (xMargin, yMargin + h1))
newImage.paste(image3, (xMargin, yMargin + h1 + h2))
newImage.paste(image4, (xMargin + w1, yMargin))
newImage.paste(image5, (xMargin + w1, yMargin + h1))
newImage.paste(image6, (xMargin + w1, yMargin + h1 + h2))

newImage.save('pictures/final/testImage.png')
"""