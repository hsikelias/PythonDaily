from PIL import ImageEnhance
import os

path = "./imgs"
pathOut = "/editedImgs"

for filename in os.listdir(path):
    img = img.open(f"{path}/{filename}")

    edit = img.filter(ImageFilter.SHARPEN)
     clean_name = os.path.splitext(filename)[0]