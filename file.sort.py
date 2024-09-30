import os
import shutil

Pfad ='c:\\Users\\GoeMa05-ext\\Downloads'
os.chdir (Pfad)
print ("arbeite in: " + os.path.abspath("."))
images = [f for f in os.listdir() if '.jpg' in f.lower()]

# os.mkdir('downloaded_images')

for image in images:
    new_path = 'downloaded_images/' + image
    shutil.move(image, new_path)
