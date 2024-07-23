import requests
from bs4 import BeautifulSoup


def gettext(url="https://realpython.github.io/fake-jobs/"):
    URL = url
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")

    content = soup.find_all('div', class_="break-words")

    text = ''

    for line in content:
        text += line.text.strip()
        
    return text

def tofile(url="https://metruyencv.com/truyen/thien-menh-phan-phai-ta-cu-tuyet-tu-hon/chuong-622"):
    URL = url
    page = requests.get(URL)

    soup = BeautifulSoup(page.content, "html.parser")

    #test
    # results = soup.find(id="ResultsContainer")
    # job_elements = results.find_all("div", class_="card-content")

    content = soup.find_all('div', class_="break-words")

    with open("myfile.txt", 'a', encoding='utf-8') as f:
        for line in content:
            f.writelines(line.text.strip())
        f.close()

def scrap(a,b):
    for i in range(a,b):
        tofile(f"https://metruyencv.com/truyen/thien-menh-phan-phai-ta-cu-tuyet-tu-hon/chuong-{i}")

scrap(674,706)