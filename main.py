from PIL import Image 
from PIL import ImageDraw
from PIL import ImageFont

font = ImageFont.truetype('fonts/MinecraftTen-VGORe.ttf', 200)

image = Image.open('pictures/original/creeper.png')
bounds = image.getbbox()
font = ImageFont.truetype('fonts/MinecraftTen-VGORe.ttf', 200)

I1 = ImageDraw.Draw(image)
length = I1.textlength("Ethan", font = font)
I1.text(((bounds[2] - length) / 2, 1250), "Ethan", font = font, fill = (0, 0, 0), align = 'center')
image.show()