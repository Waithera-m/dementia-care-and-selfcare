import os
import secrets

from flask import render_template,url_for,flash, redirect,request,abort
from flask3 import app

from flask3.models import DementiaNews
from flask3.request import get_topics



@app.route('/')
def index():

    '''
    view function returns index template and its contents
    '''
    title='Dementia Care'
    
    return render_template('index.html',title=title)

@app.route('/dementia')
def dementia():

    '''
    view function returns dementia template and its contents
    '''
    dementia_list = get_topics('dementia')

    title='news'
    
    return render_template('dementia.html',dementia_list=dementia_list,title=title)

@app.route('/dementia_care')
def dementia_care():

    '''
    view function returns dementia_care template and its contents
    '''
    title = 'dementia care'
    return render_template('dementia_care.html',title=title)














    
