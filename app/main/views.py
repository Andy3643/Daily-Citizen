from flask import render_template,request,redirect,url_for,abort
from . import main
from ..newsrequests import  get_article,get_sources,search_url

@main.route('/')
def index ():
    articles = get_article('source_id')
    sources = get_sources ()
    # place search functionality below and use it to make requests
    #if else ststemnt
    return render_template('index.html',articles=articles,sources=sources)