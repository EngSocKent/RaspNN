#!/usr/bin/env python3
# -*- coding: utf-8 -*-

from __future__ import print_function
from PIL import Image
from sys import argv, exit

if __name__ == "__main__":
    if len(argv) < 2:
        print("Usage: %s input.csv" % argv[0])
        exit(1)
    with open(argv[1]) as csv:
        with open('info.dat', 'w') as description_file:
            _ = csv.readline()
            for line in csv.readlines():
                try:
                    filename, _, _, x1, y1, x2, y2, _ = line.split(';')
                    img = Image.open(filename).convert('L')
                    # img.thumbnail((32, 32), Image.ANTIALIAS)
                    new_name = filename + '.jpeg'
                    img.save(new_name, "JPEG")
                    print('%(name)s\t1\t%(x)s\t%(y)s\t%(width)s\t%(height)s' % {
                        'name': new_name,
                        'x': x1,
                        'y': y1,
                        'width': int(x2) - int(x1),
                        'height': int(y2) - int(y1)
                    }, file=description_file)
                except Exception as e:
                    print(e)
