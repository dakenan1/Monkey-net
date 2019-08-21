# -*- coding: utf-8 -*
from PIL import Image

im = Image.open('lucy.png')
width, height = im.size
print('==',width,height)
