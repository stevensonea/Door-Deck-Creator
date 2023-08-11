from PIL import Image 
from PIL import ImageDraw
from PIL import ImageFont

image = Image.open('pictures/creeper.jpeg')
print(image.getbbox())
font = ImageFont.truetype('fonts/MinecraftTen-VGORe.ttf', 200)

I1 = ImageDraw.Draw(image)
I1.text((image.getbbox()[2] / 6, image.getbbox()[3] / 2.5), "Ethan", font = font, fill = (0, 0, 0))
image.show()