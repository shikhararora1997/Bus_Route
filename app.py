from flask import render_template, request, Flask, url_for
import json
from paths import directpath
app = Flask(__name__)

@app.route("/")
def hello():
    return render_template('index.html')

@app.route('/getRoute', methods=['GET', 'POST'])
def getRoute():
        source_stop_id = request.form['source_stop_id']
        dest_stop_id = request.form['dest_stop_id']
        routes={}
        print(source_stop_id,dest_stop_id)
        routes=directpath(source_stop_id,dest_stop_id)
        if bool(routes):
              return render_template('output.html',routes=routes)
        else:
              return render_template('nopath.html',routes=routes)
        

        
