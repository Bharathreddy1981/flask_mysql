
from flask import Flask,jsonify


app = Flask(__name__)


@app.route("/aws",methods=['GET'])
def what():
    d={"name":"Banuri.Bharath Reddy",
       "college":"MALLAREDDY COLLEGE",
       "town":"KAMAREDDY",
       "SONGS":"EZINDAGI,SCENE"}
    
    return jsonify(d)



if(__name__=="__main__"):
    app.run(host='0.0.0.0')








