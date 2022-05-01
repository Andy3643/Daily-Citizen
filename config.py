import os


class Config:
    #NEWS_API_BASE_URL ='https://api.themoviedb.org/3/news/{}?api_key={}'
    NEWS_API_KEY = os.environ.get('NEWS_API_KEY')
    
    
class ProdConfig(Config):
    pass

class DevConfig(Config):
    DEBUG = True
    
config_options = {
'development':DevConfig,
'production':ProdConfig
}