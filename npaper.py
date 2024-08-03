import nltk
nltk.download('punkt')
nltk.download('averaged_perceptron_tagger')

from newspaper import Article

from textblob import TextBlob
from vaderSentiment.vaderSentiment import SentimentIntensityAnalyzer

def greenPrint(category, data):
    GREEN = "\033[32m"
    RESET = "\033[0m"
    data = str(data)
    print(GREEN + category + RESET + " " + data)

def yellowPrint(category, data):
    YELLOW = "\033[33m"
    RESET = "\033[0m"
    data = str(data)
    print(YELLOW + category + RESET + " " + data)

def redPrint(category, data):
    RED = "\033[31m"
    RESET = "\033[0m"
    data = str(data)
    print(RED + category + RESET + " " + data)

# Initialize VADER
vaderAnalyzer = SentimentIntensityAnalyzer()

def analyzeSentimentVADER(text):
    return vaderAnalyzer.polarity_scores(text)

def analyzeSentimentTextBlob(text):
    return TextBlob(text).sentiment

print("starting")

# url = "https://www.theguardian.com/us-news/article/2024/jul/27/kamala-harris-young-voters-israel-gaza-jayapal"
url = input("Enter the URL: ")
article = Article(url)

# download and parse the article
article.download()
article.parse()
article.nlp()


# Extract information
# greenPrint("Title:", article.title)
greenPrint("Title:", article.title)
greenPrint("Authors: ", article.authors)
greenPrint("Publication Date: ", article.publish_date)
greenPrint("Article Text: ", article.text)
greenPrint("Summary:", article.summary)
greenPrint("Keywords:", article.keywords)
yellowPrint("VADER: Article Text: ", analyzeSentimentVADER(article.text))
yellowPrint("TextBlob: Article Text: ", analyzeSentimentTextBlob(article.text))
yellowPrint("VADER: Article Title: ", analyzeSentimentVADER(article.title))
yellowPrint("TextBlob: Article Title: ", analyzeSentimentTextBlob(article.title))
yellowPrint("VADER: Article Summary: ", analyzeSentimentVADER(article.summary))
yellowPrint("TextBlob: Article Summary: ", analyzeSentimentTextBlob(article.summary))
yellowPrint("VADER: Article Keywords: ", analyzeSentimentVADER(str(article.keywords)))
yellowPrint("TextBlob: Article Keywords: ", analyzeSentimentTextBlob(str(article.keywords)))