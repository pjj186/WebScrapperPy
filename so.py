import requests
from bs4 import BeautifulSoup



headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}



def extract_info(company_):
  title = company_.find("h2", {"class": "mb4"}).find("a")["title"]
  company, location = company_.find("h3", {
        "class": "mb4"
    }).find_all(
        "span", recursive=False)
  company = company.get_text(strip=True)
  job_id = company_['data-jobid']
  return {
        'title': title,
        'company': company,
        'link': f"https://stackoverflow.com/jobs/{job_id}"
    }


def get_so(word):
  url = f"https://stackoverflow.com/jobs?r=true&q={word}"
  company_infos=[]
  result = requests.get(url, headers = headers)
  soup = BeautifulSoup(result.text, "html.parser")
  companys = soup.find_all("div", {"class":"-job"})
  for company in companys:
    company_info = extract_info(company)
    company_infos.append(company_info)
  return company_infos