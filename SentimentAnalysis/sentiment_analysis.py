import requests, json

def sentiment_analyzer(text_to_analyze):
    ''' This is the actual function to make HTTP GET requests to the Watson NLP API
    '''
    url = 'https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict'
    header = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}
    myobj = { "raw_document": { "text": text_to_analyze } }
    res = requests.post(url, json = myobj, headers = header)

    # Handle invalid input to Watson NLP
    if (res.status_code == 500):
        return { "label": None, "score": None }

    label = json.loads(res.text)['documentSentiment']['label']
    score = json.loads(res.text)['documentSentiment']['score']
    return { "label": label, "score": score }

def sentiment_analyzer_checker():
    ''' This function tests different inputs for the Watson NLP API
        For debug purposes only, not used in server
    '''
    # Define the URL for the sentiment analysis API
    url = "https://sn-watson-sentiment-bert.labs.skills.network/v1/watson.runtime.nlp.v1/NlpService/SentimentPredict"

    # Set the headers with the required model ID for the API
    headers = {"grpc-metadata-mm-model-id": "sentiment_aggregated-bert-workflow_lang_multi_stock"}

    # Define the first payload with nonsensical text to test the API
    myobj = { "raw_document": { "text": "Nonsense lorem ipsum blablabla" } }

    # Make a POST request to the API with the first payload and headers
    response = requests.post(url, json=myobj, headers=headers)

    # Print the status code of the first response
    print(response.status_code)

    # Define the second payload with a meaningful text to test the API
    myobj = { "raw_document": { "text": "Testing this application for error handling" } }

    # Make a POST request to the API with the second payload and headers
    response = requests.post(url, json=myobj, headers=headers)

    # Print the status code of the second response
    print(response.status_code)
    