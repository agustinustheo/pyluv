import re
import bs4
import nltk
from googlesearch import search as google_search  # googlesearch-python (the 2019 'google' package is gone)
from newspaper import Article  # newspaper4k, the maintained fork of newspaper3k
from bs4 import BeautifulSoup
from nltk.stem import PorterStemmer
from django.http import HttpResponse
from nltk.tokenize import word_tokenize, sent_tokenize
from sklearn.metrics.pairwise import euclidean_distances
from sklearn.feature_extraction.text import CountVectorizer

nltk.download('punkt_tab', quiet=True)
nltk.download('stopwords', quiet=True)

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
    stopwords = nltk.corpus.stopwords.words('english')
    tokenized_news_title = []
    ps = PorterStemmer()
    for word in word_tokenize(message):
        if word not in stopwords:
            tokenized_news_title.append(ps.stem(word))

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
    search_results = list(google_search(search_title, num_results=10 * num_page_searched, advanced=True))

    similar_articles = []
    for result in search_results:
        similar_article = {}
        search_result_title = result.title.split('http')[0].split('...')[0]
        search_result_title = remove_unnecessary_noise(search_result_title)
        search_result_title = preproccess_text(search_result_title)
        search_result_title = news_title_tokenization(search_result_title)

        result_string = ""
        for w in search_result_title:
            result_string = result_string + w + " "

        corpus = [search_title, result_string]

        vectorizer = CountVectorizer()
        features = vectorizer.fit_transform(corpus).toarray()

        # distance between the query title and this search result's title
        dist = euclidean_distances(features[0:1], features[1:2])[0][0]

        if dist < similarity:
            similar_article["article_title"] = result.title.split('http')[0].split('...')[0]
            similar_article["article_url"] = result.url
            similar_articles.append(similar_article)

    return similar_articles

def checkNews(request):
    article = request.GET.get('article')
    result = find_similar_articles(article, 2.5)
    return HttpResponse(result)

