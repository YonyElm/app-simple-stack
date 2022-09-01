from flask import Flask, redirect, url_for, request
from .DBManager import DBManager
from .CloudMetadata import CloudMetadata

server = Flask(__name__)
dbconn = None

# Simple check for DB connection status
@server.route('/proxy/db_conn_status', methods = ['GET'])
def getConnStatus():
    global dbconn
    if (not dbconn or not dbconn.is_connected()):
        return {"value": False}
    else:
        return {"value": True}

# Connection request to DB
@server.route('/proxy/settings', methods = ['POST'])
def settings():
    endpoint = request.form['endpoint']
    dbname   = request.form['dbname']
    username = request.form['username']
    password = request.form['password']
    global dbconn
    if (not dbconn or not dbconn.is_connected()):
        dbconn = DBManager(endpoint, dbname, username, password)
        dbconn.connect()
        dbconn.populate_db() # Every connection resets DB (Ensuring table is ready)
    return redirect("/index") # <domain>/index


@server.route('/proxy/add_item_to_db', methods = ['POST'])
def addItem():
    itemNum = request.form['inum']
    itemName   = request.form['iname']
    global dbconn
    if (dbconn.is_connected()):
        dbconn.insert_records(itemNum, itemName)
    return redirect("/index") # <domain>/index

@server.route('/proxy/read_db', methods = ['GET'])
def listName():
    global dbconn
    resultArr = []
    if (dbconn.is_connected()):
        resultArr = dbconn.query_item_names()
    return {"value": resultArr}

@server.route('/proxy/cloud_metadata', methods = ['GET'])
def metadata():
    metadata = CloudMetadata()
    return  metadata.getCloudMetadata()

if __name__ == '__main__':
    server.run()
