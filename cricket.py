import requests
import bs4
import time

while True:
    link = "https://www.cricbuzz.com/live-cricket-scores/78159/afg-vs-sl-6th-match-group-b-asia-cup-2023"
    # link = "https://www.cricbuzz.com/live-cricket-scorecard/78159/afg-vs-sl-6th-match-group-b-asia-cup-2023"
    res = requests.get(link)
    soup = bs4.BeautifulSoup(res.text, 'html.parser')
    # details = soup.select(".cb-col .cb-col-100 .cb-scrd-hdr-rw")
    details = soup.select(".cb-col .cb-col-67 .cb-scrs-wrp")
    for i in details:
        score = i.getText().strip()
        print(score)
    time.sleep(30)