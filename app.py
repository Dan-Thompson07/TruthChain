# ...existing code...
from shiny.express import ui, render, input
from shiny import reactive
import requests

with ui.nav_panel("Home"):
    ui.h2("Welcome to TruthChain, an AI News Authenticator"),
    ui.p("This application helps you determine whether a news article is real or fake using machine learning."),
    ui.input_text("news_input", "Enter the news article text here:"),
    ui.input_action_button("check_btn", "Check"),
    ui.p("Result:"),


@reactive.event(input.check_btn())
def classify_news():
    news = input.news_input()
    if not news:
        return "Enter text and click Check."
    try:
        resp = requests.post("http://localhost:5000/predict", json={"news": news}, timeout=5)
        resp.raise_for_status()
        data = resp.json()
        pred = data["Prediction"]
        conf = float(data["Confidence"])
        return f"{pred} (Confidence: {conf:.2%})"
    except Exception as e:
        return f"Error contacting prediction service: {e}"

@reactive.effect
def result():
    return classify_news()

