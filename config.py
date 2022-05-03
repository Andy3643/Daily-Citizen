import os


class Config:
    HEADLINES_API_URL='https://newsapi.org/v2/top-headlines?country=us&apiKey={}'
    SOURCE_API_URL='https://newsapi.org/v2/sources?apiKey={}'
    SEARCH_SOURCES='https://newsapi.org/v2/everything?q={}&apiKey={}'
    NEWS_API_KEY = '0d17d16443b24e18b582d11709286dfb'
    
    
class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True
    
config_options = {
'development':DevConfig,
'production':ProdConfig
}