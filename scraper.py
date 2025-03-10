from bs4 import BeautifulSoup
import requests
import os
import time
 
urls = ["https://www.gradadmissions.ucsc.edu/graduate-studies", "https://www.gradadmissions.ucsc.edu/nlp",
        "https://docs.google.com/spreadsheets/d/1ritoeqeeMPk8s_X8nmBTf5E2BfHd21a0RLggd5Rm5YE/edit?gid=0#gid=0",
        "https://docs.google.com/spreadsheets/d/1Q45Rw5fX2RY-HUl60JyCc3Wm9XEVlweBat3BXZYLJFw/edit?gid=0#gid=0",
        "https://nlp.ucsc.edu/", "https://nlp.ucsc.edu/admissions/", "https://nlp.ucsc.edu/apply/", "https://nlp.ucsc.edu/capstone-projects/",
        "https://nlp.ucsc.edu/about-us/", "https://nlp.ucsc.edu/program-overview/", "https://nlp.ucsc.edu/financials/", "https://nlp.ucsc.edu/industry/",
        "https://nlp.ucsc.edu/your-career/", "https://nlp.ucsc.edu/facilities/", "https://nlp.ucsc.edu/contact/",
        "https://myucship.org/uc-santa-cruz/about-uc-ship/overview/", "https://myucship.org/uc-santa-cruz/eligibility-and-enrollment/eligibility/",
        "https://myucship.org/uc-santa-cruz/eligibility-and-enrollment/enrolling-in-coverage/", "https://myucship.org/uc-santa-cruz/eligibility-and-enrollment/waiving-coverage/",
        "https://myucship.org/uc-santa-cruz/eligibility-and-enrollment/paying-for-coverage/", "https://myucship.org/uc-santa-cruz/eligibility-and-enrollment/when-coverage-begins-and-ends/",
        "https://myucship.org/uc-santa-cruz/coverage/medical/", "https://myucship.org/uc-santa-cruz/coverage/mental-health/", "https://myucship.org/uc-santa-cruz/coverage/prescription-drugs/",
        "https://myucship.org/uc-santa-cruz/coverage/dental/", "https://myucship.org/uc-santa-cruz/coverage/vision/", "https://myucship.org/uc-santa-cruz/getting-care/where-to-get-care/",
        "https://myucship.org/uc-santa-cruz/getting-care/when-youre-away-from-campus/", "https://myucship.org/uc-santa-cruz/getting-care/extending-coverage/", "https://myucship.org/uc-santa-cruz/getting-care/filing-claims/",
        "https://myucship.org/uc-santa-cruz/getting-care/when-youre-covered-by-more-than-one-plan/", "https://myucship.org/uc-santa-cruz/contacts/", "https://registrar.ucsc.edu/calendar/key-dates/index.html", 
        "https://registrar.ucsc.edu/soc/final-examinations.html", "https://summer.ucsc.edu/studentlife/index.html", "https://catalog.ucsc.edu/en/current/general-catalog/courses/nlp-natural-language-processing/", 
        "https://registrar.ucsc.edu/faqs/students/enrollment/index.html", "https://registrar.ucsc.edu/faqs/students/grading/index.html",
        "https://registrar.ucsc.edu/faqs/students/honors/index.html", "https://registrar.ucsc.edu/faqs/students/wait-list/index.html",
        "https://registrar.ucsc.edu/faqs/students/degree-verification.html", "https://registrar.ucsc.edu/faqs/students/evaluations.html", "https://registrar.ucsc.edu/faqs/students/fees.html",
        "https://registrar.ucsc.edu/faqs/students/graduation.html", "https://registrar.ucsc.edu/faqs/students/id-card-photos.html", "https://registrar.ucsc.edu/faqs/students/residency.html", "https://registrar.ucsc.edu/faqs/students/transcripts.html", 
        "https://registrar.ucsc.edu/faqs/students/withdrawal.html"]

# # Iterate over websites
# for i, url in enumerate(urls):

#     # Scrape and parse HTML
#     path = os.path.join(os.path.dirname(__file__), "scraped/page_")
#     response = requests.get(url)
#     data = response.text
#     soup = BeautifulSoup(data, "html.parser")
    
#     # Remove tags
#     for data in soup(["style", "script"]):
#         data.decompose()

#     text = soup.get_text()
#     split = text.split("\n")
#     removed_newlines = [i for i in split if i != ""]
#     stripped = [i.strip() for i in removed_newlines]
#     final_scraped = "\n".join(stripped)

#     # Write to file
#     with open(path + str(i) + ".txt", "w") as f:
#         f.write(final_scraped)
#     time.sleep(30)
