# from app import app
# import urllib.request,json
# from .models import user
# from .models import post
# from .models import comment
# from .models import quote

# User = user.User
# Post = post.Post
# Comment = comment.Comment
# Quote = quote.Quote
# # getting api key
# # api_key = app.config['NEWS_API_KEY']
# # getting the news base url

# base_url = app.config['SOURCE_API_BASE_URL']
# articles_base_url=app.config['NEWS_API_BASE_URL']


# def get_quote(id):
#     get_article_details_url = articles_base_url.format(id,api_key)
#     with urllib.request.urlopen(get_article_details_url) as url:
#         article_details_data = url.read()
#         article_details_response = json.loads(article_details_data)
#         article_object = None
        
#         if article_details_response['articles']:
#                 article_results_list=article_details_response['articles']
#                 article_results=process_article(article_results_list)
#     return article_results
# def process_process(article_list):
#     '''
#     Function  that processes the news result and transform them to a list of Objects
#     Args:
#     article_list: A list of dictionaries that contain article details
#     Returns :
#     article_results: A list of articles objects
#     '''
#     article_results=[]
#     for article in article_list:
#         id=article.get('id')
#         title=article.get('title')
#         description=article.get('description')
#         url=article.get('url')
#         imageUrl=article.get('urlToImage')
#         publishedAt=article.get("publishedAt")
#         author=article.get("author")
#         content=article.get('content')

#         if imageUrl:
#             article_object=Article(id,title,description,imageUrl,url,publishedAt,author,content)
#             article_results.append(article_object)
#     return article_results 
