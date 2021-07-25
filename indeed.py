import requests
from bs4 import BeautifulSoup

LIMIT = 50
URL = f"https://kr.indeed.com/%EC%B7%A8%EC%97%85?as_and=python&limit={LIMIT}"

# URL 검색창의 페이지 최대값 불러오는 함수
def get_last_page():
    # 원하는 웹사이트의 실시간 html 값 불러오기
    result = requests.get(URL)
    soup = BeautifulSoup(result.text, "html.parser")

    # html 내부의 원하는 정보값 추출하기 (html 페이지의 pagination 클래스 탐색 후 )
    # pagination 변수에 저장 -> pages변수에 pagintion 클래스 하위 메소드중 a 탐색후 저장.
    # 저장한 a 값들을 pages 리스트에 저장 후 리스트 인덱싱을 통해 마지막 np(next-page) 제거
    pagination = soup.find("div", {"class": "pagination"})
    links = pagination.find_all('a')
    pages = []

    for link in links[:-1]:
        pages.append(int(link.string))

    max_page = pages[-1]

    return max_page

def extract_job(html):
    jobTitle = html.find("h2", {"class": "jobTitle"})
    title = jobTitle.find("span").string
    if title == "new":
        title = jobTitle.find_all("span")[1].string

    # 회사명 정보 추출
    company = html.find("span", {"class": "companyName"})

    if company:
        company_anchor = company.find("a")
        if company_anchor is not None:
            company = str(company_anchor.string)
        else:
            company = str(company.string)
    else:
        company: None

    # 회사 주소 정보 추출
    location = html.find("div", {"class": "companyLocation"}).string

    # 회사 상세정보 link id 정보값 추출
    job_id = html.parent["data-jk"]

    return {'title': title, 'company': company, 'location': location,
            'link': f"https://kr.indeed.com/jobs?q=python&vjk={job_id}"}


def extract_jobs(last_page):
    jobs = []
    for page in range(last_page):
        print(f"Scrapping page {page}")
        result = requests.get(f"{URL}&start={page*LIMIT}")
        soup = BeautifulSoup(result.text, "html.parser")
        # 직무(title) 정보 추출
        results = soup.find_all("div", {"class": "slider_container"})

    for result in results:
        job = extract_job(result)
        jobs.append(job)

    return jobs

def get_jobs():
    last_page = get_last_page()
    jobs = extract_jobs(last_page)

    return jobs
