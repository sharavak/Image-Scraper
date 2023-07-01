
from flask import Flask,render_template,request
import bs4
import requests

app=Flask(__name__)

@app.route('/',methods=['GET','POST'])
def index():
    f=request.form
    req=requests.get(f['url'])
    soup=bs4.BeautifulSoup(req.content,'lxml')
    d=soup.find_all('img')
    print(d[1]['src'])
        
    return render_template('index.html')

@app.route('/price')
def scrape():
    return  render_template('price.html')

@app.route('/show', methods=['GET','POST'])
def s():
    f=request.form
    print(f)
    return render_template('show.html',f=f)

if __name__ =='__main__':
    app.run(debug=True)