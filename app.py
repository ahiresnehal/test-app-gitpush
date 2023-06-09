from flask import Flask , request , render_template ,  redirect
from flask_pymongo import PyMongo 
import pymongo



app = Flask( __name__ ) 
client = pymongo.MongoClient("mongodb://localhost:27017")
db = client['db']
student = db['student']


@app.route("/" , methods=['GET','POST'])
def myhome():
    if request.method=='POST':
        x = request.form['std_name']
        y = request.form['std_age']
        z = request.form["std_email"]
        print(x,y,z)
        db.student.insert_one({'name':x , 'age':int(y) , 'email': z})
        if 10 = 10:
            print("All OK")
        if 10 == 10:
            print("All OK")
    return render_template("home.html")

@app.route("/get_data" , methods=['GET'])
def login():
    students = db.student.find()
    students = list(students)
    return render_template('list.html' , students=students)


@app.route("/replace_student/<string:name>-<string:email>" , methods=['GET','POST'])
def replace_student(name,email):
    if request.method=='POST':
        x = request.form['std_name']
        y = request.form['std_age']
        z = request.form["std_email"]
        db.student.replace_one({'name': name ,'email': email}, {'name': x, 'age': int(y) , 'email': z})
        return redirect("/get_data")
    return render_template("update.html")

@app.route("/delete_student/<string:name>-<string:email>" , methods=['GET','POST'])
def delete_student(name,email):
    db.student.delete_one({'name':name,  'email':email})
    return redirect("/get_data")
