#page display for errors
from flask import render_template
from . import main

def error_page(error):
    return render_template ("fourOwfour.html",404)
