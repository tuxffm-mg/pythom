import os
import shutil

os.system('cd c:\Users\tuxffm\Downloads')
images = [f for f in os.listdir() if '.jpg' in f.lower()]

os.mkdir('downloaded_images')

for image in images:
    new_path = 'downloaded_images/' + image
    shutil.move(image, new_path)
