import requests
from bs4 import BeautifulSoup


url = "https://weworkremotely.com/remote-jobs/search?term=python"

headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}



def extract_info(company_) :
  title = company_.find("span", {"class":"title"}).string
  company = company_.find("span", {"class":"company"}).string
  link = company_.find("a")["href"]
  return {
    "title" : title,
    "company" : company,
    "link" : f"https://weworkremotely.com/company/{link}"
  }



def get_wwr(word):
  url = f"https://weworkremotely.com/remote-jobs/search?term={word}"
  company_infos = []
  result = requests.get(url, headers=headers)
  soup = BeautifulSoup(result.text, "html.parser")
  companys = soup.find("section", {"class":"jobs"}).find_all("li", {"class":"feature"})
  for company in companys :
    company_info = extract_info(company)
    company_infos.append(company_info)
  return company_infos