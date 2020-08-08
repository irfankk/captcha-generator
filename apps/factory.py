import os
from flask import Flask
from apps.captcha_service.captcha import captcha_module



def create_app():
	app = Flask(__name__)

	app.register_blueprint(captcha_module)

	return app