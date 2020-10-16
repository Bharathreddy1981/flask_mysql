import pymysql

def rect(data):
    name=data["name"]
    email=data["email"]
    phonenumber=data["phonenumber"]
    age=data["age"]

    z = pymysql.connect(
        host="localhost",
        user="root",
        passwd = "Vangala@09",
        db = "school"
    )
    y = z.cursor()
    w = "insert into details values('" + str(name) +"','"+ str(email)+"','"+ str(phonenumber) +"',' " + str(age) + "')"
    y.execute(w)
    z.commit()
    return data
