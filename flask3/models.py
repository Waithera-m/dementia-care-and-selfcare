class DementiaNews():

    '''
    class facilitates the creation of news articls objects
    '''
    def __init__(self,author,title,publishedAt,description,url,urlToImage):

        '''
        Method facilitates the definition of objects; properties

        Args:
            author (str): article's author 
            title (str): article's title
            publishedAt (str): article publication date
            description (str): brief description of article content
            url (str): link to full article
        '''

        
        self.author = author
        self.title = title
        self.publishedAt = publishedAt
        self.description = description
        self.url = url
        self.urlToImage = urlToImage