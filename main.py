import requests

# Basic Information to Fetch Data:
apiKey = 'YOUR_API_KEY'
baseURL = 'https://newsapi.org/v2/top-headlines'

# Search Filter:
country = None
sources = None
selection = input("Hello User! You want to watch news in which format, Country(c) or Sources(s)?: ")
if selection.lower() == "c":
    country = input("Enter country code for news: ")
elif selection.lower() == "s":
    sources = input("Which specific Source do you want? (Press enter for all): ")
else:
    print("Invalid Response! Try again :(")
    exit()

# Initializing Parameters:
category = input("Enter category of news (Press enter to skip): ")
keyword = input("Enter a Keyword you want to search for (Press enter to skip): ")

parameters = {
    'apiKey': apiKey
}

if country:
    parameters['country'] = country
if category:
    parameters['category'] = category
if keyword:
    parameters['q'] = keyword
if sources:
    parameters['sources'] = sources

# Fetching Response: 
response = requests.get(baseURL, params=parameters)
data = response.json()

# Printing Article: 
if response.status_code == 200:
    articles = data['articles']
    for article in articles:
        print(f"Title: {article['title']}")
        print(f"Author: {article['author']}")
        print(f"Source: {article['source']['name']}")
        print(f"Published at: {article['publishedAt']}")
        print(f"Description: {article['description']}")
        print(f"URL: {article['url']}")
        print("-"*80)
else:
    print(f"Error: {response.status_code}")
