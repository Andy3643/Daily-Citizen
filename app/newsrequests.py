from concurrent.futures import process
import urllib.request,json
import requests 
from .models import Source, Article

#Get API Key
api_key = None

#Get base URL
sources_url = None
highlights_url = None
search_url = None

def configure_request(app):
    global api_key,sources_url,highlights_url,search_url
    api_key = app.config['NEWS_API_KEY']
    sources_url = app.config['SOURCE_API_URL']
    highlights_url = app.config ['HEADLINES_API_URL']
    search_url = app.config ['SEARCH_SOURCES']
   
   #get json response from url
# def get_sources ():
#     sources_url = sources_url.format (api_key)
    
#     with urllib.request.urlopen(source_api_url) as url:
#         unread_data=url.read()
#         read_json=json.loads(unread_data)

#         source_results=None

#         if read_json['sources']:
#             sources_list=read_json['sources']
#             source_results=process_results(sources_list)

#     return source_results
    
    
#processs source results
def process_results(sources_list):
    
    source_results = []
    for sources in sources_list:
        id=sources.get('id')
        name=sources.get('name')
        description=sources.get('description')
        url=sources.get('url')
        
        if description:
            new_source=Source(id,name,description,url)
            source_results.append(new_source)

    return source_results

#return highlight results
def get_article (source_id):
     get_highlights_url = highlights_url.format (api_key)
     with urllib.request.urlopen(get_highlights_url) as url:
        get_data = url.read()
        retrieve_json_data = json.loads(get_data)
        articles_data = None
         
        if retrieve_json_data['articles']:
             articles_list = retrieve_json_data['articles']
             articles_data = process_article(articles_list)
            
        return articles_data
    
#process source results
def process_article(articles_list):
    articles_data = []
    for article in articles_list:
        id=article.get('id')
        name=article.get('name')
        urlToImage=article.get('urlToImage')
        description=article.get('description')
        publishedAt=article.get('publishedAt')
        url=article.get('url')
        title=article.get('title')
        source=article.get('source')
        if description:
            new_article=Article(id,name,urlToImage,description,title,url,publishedAt,source)
            articles_data.append(new_article)

    return articles_data