import tls_client
from bs4 import BeautifulSoup

requests = tls_client.Session(client_identifier="safari_ios_15_5")

def dowonload(url):
    a = requests.get(url)


    data = BeautifulSoup(a.text,"lxml")
    t = data.find(class_="widget-episodeTitle js-vertical-composition-item")
    b = data.find(class_="widget-episodeBody js-episode-body")
    return(t.text,b.text)

a = requests.get("https://kakuyomu.jp/works/1177354054886847987")
soup = BeautifulSoup(a.text, 'html.parser')

# 特定のクラスを持つ要素を抽出
content_elements = soup.find_all(class_="widget-toc-episode")

# 抽出した要素内のリンクを表示
for content in content_elements:
    links = content.find_all('a')
    for link in links:
        href = link.get('href')
        a = dowonload("https://kakuyomu.jp"+href)
        print(a[0])
        with open(f"{a[0]}.txt","w+",encoding="utf-8") as f:
            f.write(a[1])
            print("success")
