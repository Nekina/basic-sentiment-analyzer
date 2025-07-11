''' Executing this function initiates the application of sentiment
    analysis to be executed over the Flask channel and deployed on
    localhost:5001.
'''

# Import Flask, render_template, request from the flask framework package
from flask import Flask, render_template, request

# Import the sentiment_analyzer function from the package created
from SentimentAnalysis.sentiment_analysis import sentiment_analyzer # pylint: disable=import-error, wrong-import-position


#Initiate the flask app
app = Flask("Sentiment Analyzer")


@app.route("/sentimentAnalyzer")
def sent_analyzer():
    ''' This code receives the text from the HTML interface and 
        runs sentiment analysis over it using sentiment_analysis()
        function. The output returned shows the label and its confidence 
        score for the provided text.
    '''
    text_to_analyze = request.args.get("textToAnalyze")
    # Handle no input from user
    if (text_to_analyze == ""):
        return "No input! Try again."
        
    res = sentiment_analyzer(text_to_analyze)
    # Handle invalid input
    if (res["label"] is None or res["score"] is None):
        return "Invalid input! Try again."

    label = res["label"].split("_", 1)[1] # Extract remaining string after "_"
    score = res["score"]
    return f"The given text has been identified as {label} with a score of {score}."

@app.route("/")
def render_index_page():
    ''' This function initiates the rendering of the main application
        page over the Flask channel
    '''
    return render_template("index.html")

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5001)
