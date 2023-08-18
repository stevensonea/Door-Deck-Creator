from PIL import Image 
from PIL import ImageDraw
from PIL import ImageFont
import pandas as pd

"""font = ImageFont.truetype('fonts/MinecraftTen-VGORe.ttf', 200)
image = Image.open('pictures/original/creeper.png')
bounds = image.getbbox()
font = ImageFont.truetype('fonts/MinecraftTen-VGORe.ttf', 200)
I1 = ImageDraw.Draw(image)
length = I1.textlength("Ethan", font = font)
I1.text(((bounds[2] - length) / 2, 1250), "Ethan", font = font, fill = (0, 0, 0), align = 'center')
image.show()
image.save()
"""

file = pd.read_excel('info.xlsx')
yurt = file.values
data = yurt[0:5]
print(data)
for i in data:
    if data[1].lower() == "axolotl":
        image = Image.open('pictures/original/axolotl.png')

    elif data[1].lower() == "bee":
        image = Image.open('pictures/original/bee.png')

    elif data[1].lower() == "cat":
        image = Image.open('pictures/original/cat.png')

    elif data[1].lower() == "cow":
        image = Image.open('pictures/original/cow.png')

    elif data[1].lower() == "creeper":
        image = Image.open('pictures/original/creeper.png')
    
    elif data[1].lower() == "dog":
        image = Image.open('pictures/original/dog.png')

    elif data[1].lower() == "ender dragon":
        image = Image.open('pictures/original/ender_dragon.png')

    elif data[1].lower() == "frog":
        image = Image.open('pictures/original/frog.png')

    elif data[1].lower() == "glow squid":
        image = Image.open('pictures/original/glow_squid.png')

    elif data[1].lower() == "goat":
        image = Image.open('pictures/original/goat.png')

    elif data[1].lower() == "iron golem":
        image = Image.open('pictures/original/iron_golem.png')

    elif data[1].lower() == "pig":
        image = Image.open('pictures/original/pig.png')

    elif data[1].lower() == "polar bear":
        image = Image.open('pictures/original/polar_bear.png')

    elif data[1].lower() == "turtle":
        image = Image.open('pictures/original/turtle.png')

    elif data[1].lower() == "villager":
        image = Image.open('pictures/original/villager.png')

    elif data[1].lower() == "witch":
        image = Image.open('pictures/original/witch.png')

    elif data[1].lower() == "zombie piglin":
        image = Image.open('pictures/original/zombie_piglin.png')

    name = data[0]
    bounds = image.getbbox()
    font = ImageFont.truetype('fonts/MinecraftTen-VGORe.ttf', 200)
    I1 = ImageDraw.Draw(image)
    length = I1.textlength(name, font = font)
    I1.text(((bounds[2] - length) / 2, 1250), name, font = font, fill = (0, 0, 0), align = 'center')
    image.save('pictures/final/' + name)


    
    

