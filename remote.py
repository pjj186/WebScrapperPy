import requests
from bs4 import BeautifulSoup



headers = {'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_9_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/35.0.1916.47 Safari/537.36'}



def extract_info(company) :
  company_ = company.find("h3", {"itemprop":"name"}).string # 회사이름
  title = company.find("h2", {"itemprop":"title"}).string # 공고제목
  return {
    "title" : title,
    "company" : company_,
    "link" : f"https://remoteok.io/remote-companies/{company_}"
  }
  
def get_remoteok(word) :
  url = f"https://remoteok.io/remote-dev+{word}-jobs"
  company_infos = []
  result = requests.get(url, headers = headers)
  soup = BeautifulSoup(result.text, "html.parser")
  companys = soup.find_all("td", {"class":"company_and_position"})
  for company in companys :
    company_info = extract_info(company)
    company_infos.append(company_info)  
  return company_infos 

