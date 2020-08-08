import os
import string
from random import randint

from flask import Blueprint, jsonify, request, Response
from PIL import ImageFont, ImageDraw, Image
import numpy as np

BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MEDIA_FOLDER = os.path.join(BASE_DIR, 'media')


captcha_module = Blueprint('captach_module', __name__, url_prefix='/gt-captcha/')


def get_random_text():
	'''
		return random number
	'''
	text = [list(string.ascii_lowercase), list(string.ascii_uppercase), list(string.digits)]
	text = text[randint(0, 2)]
	return text[randint(0, len(text)-1)]


def get_random_color():
	'''
		return the RGB color format
	'''
	return randint(120, 200), randint(120, 200), randint(120, 200)


@captcha_module.route('', methods=['GET'])
def get_captcha():
	width = 140
	height = 60
	text_length = 4
	text = ''
	img = Image.new(mode='RGB', size=(200, 200), color=(250, 250, 250))
	draw = ImageDraw.Draw(img)
	# print(get_random_text())

	for i in range(text_length):
		c = get_random_text()
		text += c
		rand_len = randint(-5, 5)
		print(width * 0.2 * (i+1) + rand_len, height * 0.2 + rand_len)
		draw.text((width * 0.2 * (i+1) + rand_len, height * 0.2 + rand_len), c,  fill=get_random_color(), align='center')
	
	# draw lines
	for i in range(3):
		x1 = randint(0, width)
		y1 = randint(0, height)
		x2 = randint(0, width)
		y2 = randint(0, height)
		draw.line((x1, y1, x2, y2), fill=get_random_color())
	print(MEDIA_FOLDER, 'mmmmmm')
	img.save(text + '.png')
	return text + '.png'



