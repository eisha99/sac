import json
from flask import request

def process_request(request):
    # get the intent and parameters from the request
    intent = request.get("queryResult").get("intent").get("displayName")
    parameters = request.get("queryResult").get("parameters")
    
    # do some processing based on the intent and parameters
    if intent == "greet":
        name = parameters.get("name")
        response_text = f"Hello, {name}! How can I assist you today?"
    elif intent == "search":
        query = parameters.get("query")
        response_text = f"Here are the search results for {query}: ..."
    else:
        response_text = "I'm sorry, I didn't understand your request."
    
    # build the response object
    response = {
        "fulfillmentText": response_text
    }
    
    # return the response object as a JSON string
    return json.dumps(response)
