from flask import render_template,request,url_for,abort,redirect
from . import main
from ..request import get_topics


@main.route('/')
def index():

    '''
    view function returns index template and its contents
    '''
    title='Dementia Care'
    
    return render_template('index.html',title=title)

@main.route('/dementia')
def dementia():

    '''
    view function returns dementia template and its contents
    '''
    dementia_list = get_topics('dementia')
    
    return render_template('dementia.html',dementia_list=dementia_list)