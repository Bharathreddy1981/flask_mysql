
from flask import Flask,jsonify


app = Flask(__name__)


@app.route("/aws",methods=['GET'])
def what():
    d={"NAME":"Bharath Reddy",
       "COLLEGE":"SAINT ANNS COLLEGE",
       "TOWN":"HYDERABAD",
       "HOBBIES":"CRICKET,VOLLEYBALL,KABADI",
       "MOBILE":78541254785211}

    return jsonify(d)



if(__name__=="__main__"):
    app.run(host='0.0.0.0')








