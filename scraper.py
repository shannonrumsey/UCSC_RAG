from bs4 import BeautifulSoup
import requests
import os
import time
 
urls = ["https://www.gradadmissions.ucsc.edu/graduate-studies", "https://www.gradadmissions.ucsc.edu/nlp",
        "https://docs.google.com/spreadsheets/d/1ritoeqeeMPk8s_X8nmBTf5E2BfHd21a0RLggd5Rm5YE/edit?gid=0#gid=0",
        "https://docs.google.com/spreadsheets/d/1Q45Rw5fX2RY-HUl60JyCc3Wm9XEVlweBat3BXZYLJFw/edit?gid=0#gid=0",
        "https://nlp.ucsc.edu/", "https://nlp.ucsc.edu/admissions/", "https://nlp.ucsc.edu/apply/", "https://nlp.ucsc.edu/capstone-projects/",
        "https://nlp.ucsc.edu/about-us/", "https://nlp.ucsc.edu/program-overview/", "https://nlp.ucsc.edu/financials/", "https://nlp.ucsc.edu/industry/",
        "https://nlp.ucsc.edu/your-career/", "https://nlp.ucsc.edu/facilities/", "https://nlp.ucsc.edu/contact/"]

# Iterate over websites
for i, url in enumerate(urls):
    time.sleep(30)

    # Scrape and parse HTML
    path = os.path.join(os.path.dirname(__file__), "scraped/page_")
    response = requests.get(url)
    data = response.text
    soup = BeautifulSoup(data, "html.parser")
    
    # Remove tags
    for data in soup(["style", "script"]):
        data.decompose()

    final_scraped = " ".join(soup.stripped_strings)

    # Write to file
    with open(path + str(i) + ".txt", "w") as f:
        f.write(final_scraped)
