# PAAN
# Parse And ANalyze
import nltk
import debugPrint

nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

from newspaper import Article

from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer


def initializeVADER():
    return SentimentIntensityAnalyzer()

def analyzeSentimentVADER(vaderAnalyzer, text):
    return vaderAnalyzer.polarity_scores(text)

def analyzeSentimentTextBlob(text):
    return TextBlob(text).sentiment

def parseArticle(url):
    article = Article(url)
    try:
        # download and parse
        article.download()
        article.parse()
        article.nlp()
        # debugPrint.greenPrint("Success PAAN: ", url)
        return article
    except Exception as e:
        debugPrint.redPrint("Error: ", e)
        return e