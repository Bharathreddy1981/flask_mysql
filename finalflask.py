from flask import Flask,jsonify,request
from reddy import flask_get,flask_post,flask_range,flask_between

finalflask = Flask(__name__)


@finalflask.route("/mango/<int:number>", methods=["GET"])
def cricket(number):
    phone=flask_get.salt(number)
    return jsonify(phone)


@finalflask.route("/orange/<value>",  methods=["GET"])
def ball(value):
    phone=flask_range.salt(value)
    return jsonify(phone)


@finalflask.route("/apple/<id>/<data>",  methods=["GET"])
def wicket(id,data):
    phone=flask_between.powder(id,data)
    return jsonify(phone)


@finalflask.route("/card/<int:id>", methods=['POST'])
def square(id):
    jsondata=request.get_json()
    final=flask_post.bus(jsondata, id)
    return jsonify(final)



if __name__=="__main__":
    finalflask.run(debug=True)
