from flask import render_template
from . import main
from ..request import get_top_news,get_top_news_by_source,get_sources,get_news_by_directory,search_news


#Views
@main.route('/')
def index():
    '''
    View root page function that returns the index page and its data
    '''

    #Getting top news and categorically arranged news
    top_articles = get_topnews(general-news)
    print(top_articles)
    biz_articles  = get_categories('business')
    tech_articles = get_categories('technology')
    ent_articles = get_categories('entertainment')
    sprt_articles = get_categories('sports')
    title = 'NEWSHIGHLIGHT'
    return render_template('index.html',title = title,google_news = top_articles, biz= biz_articles,tech = tech_articles, ent = ent_articles,sprt= sprt_articles)