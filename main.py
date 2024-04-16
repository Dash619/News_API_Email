import requests

api_key = "1047dae7ae354483a340487c001236c3"
url = "https://newsapi.org/v2/everything?q=tesla&" \
    "sortBy=publishedAt&apiKey=" \
    "1047dae7ae354483a340487c001236c3"

request = requests.get(url)
content = request.json()
for article in content["articles"]:
    print(article["title"])
    print(article["description"])
