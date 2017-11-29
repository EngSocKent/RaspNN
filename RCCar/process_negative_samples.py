#!/usr/bin/env python

from PIL import Image
from os import listdir, mkdir
from os.path import isfile, join


def process_negative_samples(path, maxWidth):
    src = join(path, "img")
    images = [join(src, img) for img in listdir(src) if isfile(join(src, img))]
    mkdir(join(path, 'output'))
    names = range(len(images))
    # Resize process from https://opensource.com/life/15/2/resize-images-python
    bg = open(join(path, 'bg.txt'), 'w')
    for image, name in zip(images, names):
        try:
            img = Image.open(image)
            if img.size[0] > maxWidth:
                scalePercentage = float(maxWidth / float(img.size[0]))
                img = img.resize((maxWidth, int(float(img.size[1]) * scalePercentage)), Image.ANTIALIAS)
            new_name = str(name) + '.jpg'
            img.save(join(join(path, "output"), new_name))
            bg.write(join('output', new_name) + "\r\n")
        except Exception as e:
            print(e)
    bg.close()

if __name__ == "__main__":
    process_negative_samples("./dataset/negative", 640)
