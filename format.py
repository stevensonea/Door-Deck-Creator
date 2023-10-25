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
NUMBER_OF_PAGES = math.floor(len(filepaths) / IMAGE_PER_PAGE) + 1
REMAINDER = len(filepaths) % IMAGE_PER_PAGE
print(len(filepaths))
print(NUMBER_OF_PAGES)
print(REMAINDER)

currentImageIndex = 0
currentPageIndex = 1
for i in range(0, NUMBER_OF_PAGES):
    images = []
    width = []
    height = []
    if currentPageIndex == NUMBER_OF_PAGES:
        for j in range (0, REMAINDER):
            currentImage = Image.open(filepaths[currentImageIndex])
            images.append(currentImage)
            width.append(currentImage.size[0])
            height.append(currentImage.size[1])
            currentImageIndex += 1
    else:
        for j in range(0, IMAGE_PER_PAGE):
            currentImage = Image.open(filepaths[currentImageIndex])
            images.append(currentImage)
            width.append(currentImage.size[0])
            height.append(currentImage.size[1])
            currentImageIndex += 1

    xCoordinate = [0, 0, 0, width[0], width[0], width[0]]
    yCoordinate = [0, height[0], height[0] + height [0], 0, height[0], height[0] + height[0]]
    newImage = Image.new('RGB', (images[0].size[0] * 2, images[0].size[1]*3))

    if currentPageIndex == NUMBER_OF_PAGES:
        for i in range(0, REMAINDER):
            newImage.paste(images[i], (xCoordinate[i], yCoordinate[i]))

    else:
        for i in range(0, len(images)):
            newImage.paste(images[i], (xCoordinate[i], yCoordinate[i]))
        
    newImage.save('pictures/pages/page' + str(currentPageIndex) + '.png')
    currentPageIndex += 1


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