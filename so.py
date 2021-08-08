import requests
from bs4 import BeautifulSoup

URL = f"https://stackoverflow.com/jobs?q=python"
headers = {"User-Agent":"Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/92.0.4515.131 Safari/537.36" }

def get_last_page():
    result = requests.get(URL, headers = headers)
    soup = BeautifulSoup(result.text, "html.parser")
    pages = soup.find("div", {"class": "s-pagination"}).find_all("a")
    last_page = pages[-2].get_text(strip=True)
    return int(last_page)

# extract_jobs 함수를 통해 얻어낸 일자리 정보들의 세부정보 추출
def extract_job(html):
    title = html.find("h2", {"class" : "mb4"}).find("a")["title"]
    company, location = html.find("h3", {"class" : "mb4"}).find_all("span", recursive=False)
    company = company.get_text(strip=True)
    location = location.get_text(strip=True)
    job_id = html['data-jobid']

    return {'title': title, 'company': company, 'location': location, 'apply_link': f"https://stackoverflow.com/jobs/{job_id}"}


# 마지막 페이지를 인자로 받아서 URL 페이지의 시작부터 끝페이지 까지의 class 추출
def extract_jobs(last_page):
    jobs = []

    for page in range(last_page):
        print(f"Scrapping SO: Page {page+1}")
        result = requests.get(f"{URL}&pg={page+1}")
        soup = BeautifulSoup(result.text, "html.parser")
        results = soup.find_all("div", {"class": "-job" })

        for result in results:
            job = extract_job(result)
            jobs.append(job)
    return jobs

def get_jobs():
    last_page = get_last_page()
    jobs = extract_jobs(last_page)

    return jobs