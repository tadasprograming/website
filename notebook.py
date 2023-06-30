from scrape_app import scrape

url = "https://rekvizitai.vz.lt/imone/maxima_lt_uab/"

dic = scrape.find_info(scrape.scrape(url))

for info in dic:
    print(info, dic[info])