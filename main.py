import requests
from flask import Flask, render_template, request
app = Flask(__name__)
app.debug = False

#start code:
@app.route('/', methods=['GET','POST'])
def page():
    if request.args.get('url')!=None:
        url = request.args.get('url')
    else:
        url = ""
    if url!="":
        try:
            http = (requests.head("http://"+url)).status_code
            success = True
        except:
            http = "Unsuccessful"
            success = True
        try:
            https = (requests.head("https://"+url)).status_code
            success = True
        except:
            https = "Unsuccessful"
            success = True
    else:
        success = None
        http = None
        https = None
    return render_template('index.html', url=url, http=http, https=https, success=success)
if __name__ == "__main__":
    app.run()