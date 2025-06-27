import json

import gradio as gr
from textblob import TextBlob


def sentiment_analysis(text: str) -> str:
    """
    Analyze the sentiment of the given text
    :param text: Text to Analyze.
    :return: A JSON String containing polarity, subjectivity and assessment.
    """

    blob = TextBlob(text)
    sentiment = blob.sentiment

    result = {
        "polarity": round(sentiment.polarity, 2),
        "subjectivity": round(sentiment.subjectivity, 2),
        "assessment": "positive" if sentiment.polarity > 0 else "negative" if sentiment.polarity < 0 else "neutral"
    }

    return json.dumps(result)


demo = gr.Interface(
    fn=sentiment_analysis,
    inputs=gr.Textbox(placeholder="Enter text to analyze...."),
    outputs=gr.Textbox(),
    title="Text Sentiment Analysis",
    description="Analyze the sentiment of text using TextBlob"
)

if __name__ == "__main__":
    demo.launch(mcp_server=True)
