from flask import Flask,request,render_template,redirect,send_file
from urllib.parse import urljoin
#from flask import jsonify
import requests,uuid,os,shutil
from io import BytesIO
from zipfile import ZipFile
from glob import glob
from scraping import scrape
app=Flask(__name__)
@app.route('/',methods=['GET',"POST"])
def index():
    return render_template('home.html')

@app.route('/down',methods=['GET','POST'])
def down():
    if request.method=='POST':
        con=request.get_json()['data']
        links=scrape(con)
        check=os.listdir(os.getcwd())
        target = 'send'
        if target in check: 
            shutil.rmtree('send', ignore_errors=True)
        os.mkdir('send')
        if links:
            for i in links:
                res=requests.get(i).content
                try:
                    f=open(f'send/{uuid.uuid1()}.{i[-3:]}','wb')
                    f.write(res)
                    f.close()
                except:pass
            stream = BytesIO()
            with ZipFile(stream, 'w') as zf:
                for file in glob(os.path.join(target,'*')):
                    zf.write(file, os.path.basename(file))
            stream.seek(0)
            return send_file(
                    stream,
                    as_attachment=True,
                    download_name='Images.zip',
                    mimetype='application/zip'
                        )
        else:
            stream=BytesIO()
            stream.write('There is no images in the given url'.encode())
            stream.seek(0)
            return send_file(stream,as_attachment=True,download_name='No-Images.txt',mimetype='application/text')
    return redirect('/')
