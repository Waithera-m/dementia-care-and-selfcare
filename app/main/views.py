from flask import render_template,request,url_for,abort,redirect
from . import main


@main.route('/')
def index():

    '''
    view function returns index template and its contents
    '''
    title='Dementia Care'
    
    return render_template('index.html',title=title)

@main.route('/about')
def about():
    return render_template('about.html',title='About us')

@main.route('/info')
def info():

    '''
    view function returns index template and its contents
    '''
    title='Information on Dimensia'
    
    return render_template('info.html',title=title)