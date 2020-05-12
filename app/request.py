import urllib.request,json
from .models import DementiaNews


apiKey = None

def configure_request(app):

    '''
    function facilitates the assignation of values to the apiKey and url variables
    '''
    global apiKey

    apiKey = app.config['NEWS_API_KEY']


def get_topics(topic):

    '''
    function gets and returns articles that cover a specific topic
    '''
    
    topical_url="https://newsapi.org/v2/everything?q={}&apiKey={}".format(topic,apiKey)
    

    with urllib.request.urlopen(topical_url) as url:
        topic_details_data =  url.read()
        topic_data_response = json.loads(topic_details_data)

        topic_results = None
        if topic_data_response['articles']:
            topic_results_list = topic_data_response['articles']
            topic_results = modify_articles(topic_results_list)
    return topic_results

def modify_articles(topic_list):

    '''
    function transforms api response data into a list

    Args:
        topic_list: a list of of dictionaries
    
    Returns:
        topic_results: a list of article objects
    '''
    topic_results = []

    for article in topic_list:
        author = article.get('author')
        title = article.get('title')
        publishedAt = article.get('publishedAt')
        description = article.get('description')
        url = article.get('url')
        urlToImage =  article.get('urlToImage')

        if urlToImage:
            article_object = DementiaNews(author,title,publishedAt,description,url,urlToImage)
            topic_results.append(article_object)
    return topic_results