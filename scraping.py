import requests,bs4
from urllib.parse import urljoin 
def scrape(con):
    res=''
    try:
        if con:
            res=requests.get(con)
            soup=bs4.BeautifulSoup(res.content,'lxml')
            images=soup.find_all('img')
            links=[]
            for i in images:
                src=i['src']
                links.append(urljoin(con,src))
            if not links:return []
            return links
        else:return []
    except:
        return [] 