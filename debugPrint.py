def greenPrintAll(data):
    GREEN = "\033[32m"
    RESET = "\033[0m"
    data = str(data)
    print(GREEN + data + RESET)

def redPrintAll(data):
    RED = "\033[31m"
    RESET = "\033[0m"
    data = str(data)
    print(RED + data + RESET)

def yellowPrintAll(data):
    YELLOW = "\033[33m"
    RESET = "\033[0m"
    data = str(data)
    print(YELLOW + data + RESET)


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

def printStatus(item):
    greenPrintAll("Success PAAN: ")
    for i in item:
        if  (i == "URL" or
            i == "Title" or
            i == "Authors" or
            i == "Date"):
            greenPrint(i + ": ", item[i])
        elif i == "text" or i == "summary":
            yellowPrint(i + ": ", len(item[i]))
        else:
            yellowPrint(i + ": ", item[i])
        # yellowPrint("Type of: " + i + ": ", type(item[i]))

# def printStatus(link, title, authors, date, vaderTitle, textBlobTitle, vaderText, textBlobText, vaderSummary, textBlobSummary, vaderKeywords, textBlobKeywords):
#     greenPrint("Success PAAN: ", link)
#     greenPrint("Title: ", title)
#     greenPrint("Authors: ", authors)
#     greenPrint("Date: ", date)
#     yellowPrint("URL: ", link)
#     yellowPrint("VADER: Title: ", vaderTitle)
#     yellowPrint("TextBlob: Title: ", textBlobTitle)
#     yellowPrint("VADER: Text: ", vaderText)
#     yellowPrint("TextBlob: Text: ", textBlobText)
#     yellowPrint("VADER: Summary: ", vaderSummary)
#     yellowPrint("TextBlob: Summary: ", textBlobSummary)
#     yellowPrint("VADER: Article Keywords: ", vaderKeywords)
#     yellowPrint("TextBlob: Article Keywords: ", textBlobKeywords)
#     print()
#     greenPrint("Type of: Success PAAN: ", link)
#     greenPrint("Type of: Title: ", type(title))
#     greenPrint("Type of: Authors: ", type(authors))
#     greenPrint("Type of: Date: ", type(date))
#     yellowPrint("Type of: URL: ", type(link))
#     yellowPrint("Type of: VADER: Title: ", type(vaderTitle))
#     yellowPrint("Type of: TextBlob: Title: ", type(textBlobTitle))
#     yellowPrint("Type of: VADER: Text: ", type(vaderText))
#     yellowPrint("Type of: TextBlob: Text: ", type(textBlobText))
#     yellowPrint("Type of: VADER: Summary: ", type(vaderSummary))
#     yellowPrint("Type of: TextBlob: Summary: ", type(textBlobSummary))
#     yellowPrint("Type of: VADER: Article Keywords: ", type(vaderKeywords))
#     yellowPrint("Type of: TextBlob: Article Keywords: ", type(textBlobKeywords))