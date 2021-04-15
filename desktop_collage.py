from PIL import Image
import os
import random
import ctypes

DIRECTORY = "img"
PATH = (os.path.dirname(os.path.realpath(__file__))+"\\bungulo.png").replace("\\","/").replace("c:/","C:/")

files = os.listdir(DIRECTORY)

WIDTH = 1920
HEIGHT = 1080

print("this will run 4ever just close it if u want it to stop. thank u")

while True:

    img = Image.open("blank.png")

    for i in range(100):
        paste_img = Image.open(DIRECTORY+"/"+random.choice(files))
        paste_img = paste_img.convert("RGBA")

        paste_width = random.randint(200,600)
        paste_height = int(paste_img.height*paste_width/paste_img.width)
        paste_img = paste_img.resize((paste_width,paste_height))
        paste_img.putalpha(random.randint(128,255))

        paste_x = random.randint(-paste_width,WIDTH)
        paste_y = random.randint(-paste_height,HEIGHT)
        img.paste(paste_img,(paste_x,paste_y), paste_img.convert("RGBA"))

    img.save("bungulo.png")

    ctypes.windll.user32.SystemParametersInfoW(20, 0, PATH , 0)