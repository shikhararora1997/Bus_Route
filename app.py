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
        source_lat = request.form['source_lat']
        source_lon = request.form['source_lon']
        dest_lat = request.form['dest_lat']
        dest_lon = request.form['dest_lon']
        routes={}       
        routes=directpath(source_stop_id,dest_stop_id)
        if bool(routes):
               return render_template('map.html',routes=routes)
        else:
               return render_template('nopath.html',routes=routes)
        

        
