from flask import Blueprint, jsonify
from .services import *

# Define the blueprint for the main section of the site
main = Blueprint('main', __name__)

@main.route('/')
def index():
    return 'Main route!'

@main.route('/test')
def about():
    data = testFunction()
    return jsonify(data)