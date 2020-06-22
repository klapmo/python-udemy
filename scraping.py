import requests
from bs4 import BeautifulSoup
from csv import writer

html = "https://www.rithmschool.com/blog"
response = requests.get(html)

soup = BeautifulSoup(response.text, "html.parser")

# Grab articles in page
articles = soup.find_all("article")

# Create file to write to
with open("blog_data.csv","w") as csv_file:
    csv_writer = writer(csv_file)
    # Create Headers
    csv_writer.writerow(["title","link","date"])
    
    # Write Rows
    for article in articles:
        a_tag = article.find("a")
        title = a_tag.get_text()
        url = a_tag['href']
        date = article.find("time")["datetime"]
        csv_writer.writerow([title, url, date])