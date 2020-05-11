from flask import render_template,request,url_for,abort,redirect
from . import main


@main.route('/')
def index():

    '''
    view function returns index template and its contents
    '''
    title='Dementia Care'
    
    return render_template('index.html',title=title)