import requests

# Assuming send_email is properly imported and expects two arguments: subject and body
from send_email import send_email

topic = "tesla"
api_key = "1047dae7ae354483a340487c001236c3"
url = f"https://newsapi.org/v2/everything?q={topic}&sortBy=publishedAt&apiKey={api_key}&language=en"

response = requests.get(url)
content = response.json()

message = ""
for article in content["articles"][:20]:
    if article["title"] is not None and article["description"] is not None:
        message += f"{article['title']}\n{article['description']}\n{article['url']}\n\n"

# Send the email with a fixed subject and the formatted message as the body
send_email("Today's News on Tesla", message)
