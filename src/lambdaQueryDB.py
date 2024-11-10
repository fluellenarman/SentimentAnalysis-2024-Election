import boto3
import debugPrint
import traceback

from dotenv import load_dotenv
import os

def scanTable(session):
    
    dynamodb = session.resource('dynamodb')

    table = dynamodb.Table("Sentiment_Analysis_Trump")
    response = table.scan()
    items = response['Items']
    print(items)
    print(type(items))
    print(type(items[0]))
    debugPrint.greenPrintAll("SCAN TABLE: SUCESS")
    return

def getItem(session, key_value):
    dynamodb = session.resource("dynamodb")
    table = dynamodb.Table("Sentiment_Analysis_Trump")
    try:
        response = table.get_item(Key={
            "URL": key_value,
            # "date": "2024-08-02 00:00:00"
            })

        debugPrint.greenPrint("GET Success: ", response["Item"])
        debugPrint.greenPrintAll("GET ITEM: SUCESS")
    except Exception as e:
        debugPrint.redPrint("ERROR: ", e)
    return

def putItem(item, tableName):
    dynamodb = boto3.resource("dynamodb")
    table = dynamodb.Table(tableName)
    try:
        response = table.put_item(Item={
            "URL": item["URL"],
            "date": item["date"],
            "title": item["title"],
            "authors": item["authors"],
            "text": item["text"],
            "summary": item["summary"],
            "keyWords": item["keyWords"],
            "vaderTitle": item["vaderTitle"],
            "textBlobTitle": item["textBlobTitle"],
            "vaderText": item["vaderText"],
            "textBlobText": item["textBlobText"],
            "vaderSummary": item["vaderSummary"],
            "textBlobSummary": item["textBlobSummary"],
            "vaderKeywords": item["vaderKeywords"],
            "textBlobKeywords": item["textBlobKeywords"]
        })
        debugPrint.greenPrintAll("PUT ITEM: SUCESS")
    except Exception as e:
        debugPrint.redPrint("ERROR: ", e)
        debugPrint.redPrint("TRACEBACK: ", traceback.print_exc())
    return