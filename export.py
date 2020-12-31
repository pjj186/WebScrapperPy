import csv


def save_to_file(jobs, word):
  file = open(f"{word}.csv", mode="w")  # 1. 파일을 열고 그 파일을 file 변수에 저장
  writer = csv.writer(file)  # 방금 연 파일에다가 csv를 작성
  writer.writerow(["title", "company", "link"])
  for job in jobs :
    writer.writerow(list(job.values()))
  return