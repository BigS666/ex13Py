from flask import Flask
from flask import request
import json
from flask import jsonify
import sqlite3

app = Flask(__name__)

AllData = list()




#for row in c.execute('SELECT * FROM dataBrute'):
#    AllData.append(json.loads(row[0]))

@app.route('/', methods=['GET', 'POST'])
def github_statuses_list():
    params=request.args
    numeroPage=int(params['page'])
    nombreParPage=int(params['nb'])

    debut = int((numeroPage-1)*nombreParPage)

    maliste = list()
    conn = sqlite3.connect('ex13.db')
    c = conn.cursor()
    for row in c.execute('SELECT * FROM dataBrute limit ? offset ?',(nombreParPage,debut)):
        maliste.append(json.loads(row[0]))
    c.close()
    return jsonify(maliste)

@app.route('/byid<int:author_id>')
def github_status_by_author_id(author_id):
    retour = list()
    conn = sqlite3.connect('ex13.db')
    c = conn.cursor()
    #"actor":{"id":8837415
    machaine = "%\"actor\":{\"id\":"+str(author_id)+"%"
    for row in c.execute("select * from dataBrute where [all] like ?",(machaine,)):
        retour.append(json.loads(row[0]))

    #for status in AllData:
    #    if(status['actor']['id'] == author_id):
    #        retour.append(status)
    c.close()
    return jsonify(retour)
