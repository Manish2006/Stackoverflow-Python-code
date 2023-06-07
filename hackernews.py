import requests
import pandas as pd
from bs4 import BeautifulSoup
response = requests.get("https://news.ycombinator.com/")
soup = BeautifulSoup(response.text, "html.parser")
questions = soup.select(".athing")

for question in questions:
    print(str(question.select_one(".titleline").getText()))
print(type(question))





