import requests
from bs4 import BeautifulSoup
import time

def download_as_txt(url, output_filename):

    # Scrapes each URL and parses it as HTML file
    response = requests.get(url)
    soup = BeautifulSoup(response.text, 'html.parser')
    
    # Removes HTML tags
    for script in soup(["script", "style"]):
        script.decompose()
    text = soup.get_text()
    
    # Remove empty lines and whitespaces
    lines = (line.strip() for line in text.splitlines())
    chunks = (phrase.strip() for line in lines for phrase in line.split("  "))
    text = '\n'.join(chunk for chunk in chunks if chunk)
    
    with open(output_filename, 'w', encoding='utf-8') as f:
        f.write(text)

urls = ["https://www.gradadmissions.ucsc.edu/graduate-studies", "https://www.gradadmissions.ucsc.edu/nlp",
        "https://docs.google.com/spreadsheets/d/1ritoeqeeMPk8s_X8nmBTf5E2BfHd21a0RLggd5Rm5YE/edit?gid=0#gid=0",
        "https://docs.google.com/spreadsheets/d/1Q45Rw5fX2RY-HUl60JyCc3Wm9XEVlweBat3BXZYLJFw/edit?gid=0#gid=0",
        "https://nlp.ucsc.edu/", "https://nlp.ucsc.edu/admissions/", "https://nlp.ucsc.edu/apply/", "https://nlp.ucsc.edu/capstone-projects/",
        "https://nlp.ucsc.edu/about-us/", "https://nlp.ucsc.edu/program-overview/", "https://nlp.ucsc.edu/financials/", "https://nlp.ucsc.edu/industry/",
        "https://nlp.ucsc.edu/your-career/", "https://nlp.ucsc.edu/facilities/", "https://nlp.ucsc.edu/contact/"]

for i, url in enumerate(urls):
    # Delay each request by 30 seconds so we don't get banned :)
    time.sleep(30)
    download_as_txt(url, f'scraped/page_{i}.txt')