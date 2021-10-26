# Flask_main 파일에서 생성된 db를 CSV형식의 파일로 변환 후
# 저장하는 python file
import csv

def save_to_file(jobs):
    file = open("jobs.csv", mode="w", encoding="utf-8-sig", newline="")
    writer = csv.writer(file)
    writer.writerow(["title", "company", "location", "link"])

    for job in jobs:
        writer.writerow(list(job.values()))
    return