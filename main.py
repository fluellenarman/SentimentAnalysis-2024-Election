import debugPrint
import scrapeGoogleNews
import paan
import sys
from datetime import datetime
import queryDB
from decimal import Decimal

def paanController(query, numPages):
    linkArray = scrapeGoogleNews.scrapeGoogleNews(query, numPages)
    vaderAnalyzer = paan.initializeVADER()

    skipLinks = [
        "support.google",
        "maps.google",
        "accounts.google",
        "/search%"
    ]

    skipTitles = [
        "Subscribe to read"
    ]
    
    for link in linkArray:
        skip = False

        for skipLink in skipLinks:
            if skipLink in link:
                debugPrint.redPrint("Skipping: ", link)
                skip = True
                break
        
        if skip == True:
            continue

        parsedArticle = paan.parseArticle(link)
        if isinstance(parsedArticle, Exception):
            # debugPrint.redPrintAll("ERROR: EXCEPTION")
            debugPrint.redPrint("Error: ", parsedArticle)
        else:
            # Get the article's title, author, date, text, and summary
            title = parsedArticle.title
            author = parsedArticle.authors
            date = parsedArticle.publish_date
            text = parsedArticle.text
            summary = parsedArticle.summary
            keyWords = parsedArticle.keywords

            # Skip articles
            for skipTitle in skipTitles:
                if skipTitle in title:
                    debugPrint.redPrint("Skipping: ", title)
                    skip = True
                    break
            if skip == True:
                continue
            if sys.getsizeof(text) < 1250:
                # Skipping because the article is too short, could indicate it's a video
                debugPrint.redPrint("Skipping: ", title)
                continue

            # Analyze the sentiment of the title, text, summary, and keywords
            vaderTitle = paan.analyzeSentimentVADER(vaderAnalyzer, parsedArticle.title)
            textBlobTitle = paan.analyzeSentimentTextBlob(parsedArticle.title)
            vaderText = paan.analyzeSentimentVADER(vaderAnalyzer, parsedArticle.text)
            textBlobText = paan.analyzeSentimentTextBlob(parsedArticle.text)
            vaderSummary = paan.analyzeSentimentVADER(vaderAnalyzer, parsedArticle.summary)
            textBlobSummary = paan.analyzeSentimentTextBlob(parsedArticle.summary)
            vaderKeywords = paan.analyzeSentimentVADER(vaderAnalyzer, str(parsedArticle.keywords))
            textBlobKeywords = paan.analyzeSentimentTextBlob(str(parsedArticle.keywords))

            if date == None:
                debugPrint.yellowPrint("Date is None: ", date)
                date = (datetime.now().strftime("%Y-%m-%d %H:%M:%S"))
                debugPrint.yellowPrint("Date is Now: ", date)

            # Convert the sentiment scores to Decimal
            decimalVaderTitle = convertVADERToDecimal(vaderTitle)
            decimalTextBlobTitle = convertTextBlobToDecimal(textBlobTitle)
            decimalVaderText = convertVADERToDecimal(vaderText)
            decimalTextBlobText = convertTextBlobToDecimal(textBlobText)
            decimalVaderSummary = convertVADERToDecimal(vaderSummary)
            decimalTextBlobSummary = convertTextBlobToDecimal(textBlobSummary)
            decimalVaderKeywords = convertVADERToDecimal(vaderKeywords)
            decimalTextBlobKeywords = convertTextBlobToDecimal(textBlobKeywords)

            data = {
                "URL": link,
                "date": str(date),
                "title": title,
                "authors": author,
                "text": text,
                "summary": summary,
                "keyWords": keyWords,
                "vaderTitle": decimalVaderTitle,
                "textBlobTitle": decimalTextBlobTitle,
                "vaderText": decimalVaderText,
                "textBlobText": decimalTextBlobText,
                "vaderSummary": decimalVaderSummary,
                "textBlobSummary": decimalTextBlobSummary,
                "vaderKeywords": decimalVaderKeywords,
                "textBlobKeywords": decimalTextBlobKeywords
            }

            tableName = ""
            if query == "Donald Trump":
                tableName = "Sentiment_Analysis_Trump"
            elif query == "Kamala Harris":
                tableName = "Sentiment_Analysis_Harris"
            
            session = queryDB.getSession()

            queryDB.putItem(session, data, tableName)
            # debugPrint.printStatus(data)
            
def convertVADERToDecimal(vaderDict):
    for i in vaderDict.keys():
        vaderDict[i] = Decimal(str(vaderDict[i]))
    return vaderDict

def convertTextBlobToDecimal(textBlob):
    newPolarity = Decimal(str(textBlob.polarity))
    newSubjectivity = Decimal(str(textBlob.subjectivity))
    outputDict = {
        "polarity": newPolarity,
        "subjectivity": newSubjectivity
    }
    return outputDict



query = 'Donald Trump'
numPages = 2  # Number of pages to scrape

debugPrint.greenPrintAll("========================= Donald Trump =========================")
paanController(query, numPages)

query = "Kamala Harris"

debugPrint.greenPrintAll("========================= Kamala Harris =========================")
paanController(query, numPages)