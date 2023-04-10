from flask import Flask, request
import psycopg2

app = Flask(__name__)

conn = psycopg2.connect(
    host="localhost",
    database="class",
    user="postgres",
    password="Ruhit@2013"
)

cur = conn.cursor()

def getData():
    data = request.json
    name, roll_no, age = data["name"], data["roll_no"], data["age"]
    return name, roll_no, age

@app.get("/")
def home():
    return "Flask is working!"

@app.get("/getAll")
def getStudents():
    query = "select * from Student;"
    cur.execute(query)
    rows = cur.fetchall()
    return rows, 200


@app.post("/addStudent")
def addStudent():
    name, roll_no, age = getData()
    query = f"insert into Student(name, roll_no, age) values('{name}',{roll_no},{age});"
    cur.execute(query)
    conn.commit()
    return "Student added", 201


@app.patch("/updateStudent")
def updateStudent():
    name, roll_no, age = getData()
    query = f"update Student set name='{name}' where roll_no={roll_no};"
    cur.execute(query)
    conn.commit()
    return ("Student updated", 204)

@app.delete("/deleteStudent/<int:roll_no>")
def deleteStudent(roll_no):
    query = f"delete from Student where roll_no={roll_no};"
    cur.execute(query)
    conn.commit()
    return "Student Deleted", 202

