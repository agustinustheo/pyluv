import re
import bs4
import nltk
from google import google
from newspaper import Article
from bs4 import BeautifulSoup
from django.http import HttpResponse
from nltk.tokenize import word_tokenize, sent_tokenize
from sklearn.metrics.pairwise import euclidean_distances
from sklearn.feature_extraction.text import CountVectorizer

def preproccess_text(text_messages):
    # change words to lower case - Hello, HELLO, hello are all the same word
    processed = text_messages.lower()

    # Remove remove unnecessary noise
    processed = re.sub(r'\[[0-9]+\]|\[[a-z]+\]|\[[A-Z]+\]|\\\\|\\r|\\t|\\n|\\', ' ', processed)

    # Remove punctuation
    processed = re.sub(r'[.,\/#!%\^&\*;\[\]:|+{}=\-\'"_”“`~(’)?]', ' ', processed)

    # Replace whitespace between terms with a single space
    processed = re.sub(r'\s+', ' ', processed)

    # Remove leading and trailing whitespace
    processed = re.sub(r'^\s+|\s+?$', '', processed)
    return processed

def remove_unnecessary_noise(text_messages):
    text_messages = re.sub(r'\\([a-z]|[A-Z]|[0-9])([a-z]|[A-Z]|[0-9])([a-z]|[A-Z]|[0-9])\\([a-z]|[A-Z]|[0-9])([a-z]|[A-Z]|[0-9])([a-z]|[A-Z]|[0-9])\\([a-z]|[A-Z]|[0-9])([a-z]|[A-Z]|[0-9])([a-z]|[A-Z]|[0-9])', ' ', text_messages)
    text_messages = re.sub(r'\\([a-z]|[A-Z]|[0-9])([a-z]|[A-Z]|[0-9])([a-z]|[A-Z]|[0-9])\\([a-z]|[A-Z]|[0-9])([a-z]|[A-Z]|[0-9])([a-z]|[A-Z]|[0-9])', ' ', text_messages)
    text_messages = re.sub(r'\[[0-9]+\]|\[[a-z]+\]|\[[A-Z]+\]|\\\\|\\r|\\t|\\n|\\', ' ', text_messages)

    return text_messages

def news_title_tokenization(message):
    tokenized_news_title = []
    for word in word_tokenize(message):
        tokenized_news_title.append(word)

    return tokenized_news_title

def find_similar_articles(news, similarity):
    news_title_tokenized = ""
    
    if(re.match(r'^https?:\/\/(www\.)?[-a-zA-Z0-9@:%._\+~#=]{2,256}\.[a-z]{2,6}\b([-a-zA-Z0-9@:%_\+.~#?&//=]*)$', news)):
        news_article = Article(news)
        news_article.download()
        news_article.parse()
        news_title_tokenized = news_title_tokenization(preproccess_text(news_article.title))
    else:
        news_title_tokenized = news_title_tokenization(preproccess_text(news))

    search_title = ""
    for word in news_title_tokenized:
        search_title = search_title + word + " "

    num_page_searched = 1
    search_results = google.search(search_title, num_page_searched)

    similar_articles = []
    similar_articless = {}
    
    similar_articless["article_title"] = len(search_results)
    similar_articless["article_url"] = len(search_results)
    similar_articles.append(similar_articless)

    for result in search_results:
        similar_article = {}
        search_result_title = result.name.split('http')[0].split('...')[0]
        search_result_title = remove_unnecessary_noise(search_result_title)
        search_result_title = preproccess_text(search_result_title)
        search_result_title = news_title_tokenization(search_result_title)

        result_string = ""
        for w in search_result_title:
            result_string = result_string + w + " "

            corpus = []
            corpus.append(search_title)
            corpus.append(result_string)

        vectorizer = CountVectorizer()
        features = vectorizer.fit_transform(corpus).todense()

        for f in features:
            dist = euclidean_distances(features[0], f)

        if dist < similarity:
            similar_article["article_title"] = result.name.split('http')[0].split('...')[0]
            similar_article["article_url"] = dist
            similar_articles.append(similar_article)

    return similar_articles

def checkNews(request):
    article = request.GET.get('article')
    result = find_similar_articles(article, 2.5)
    return HttpResponse(result)

