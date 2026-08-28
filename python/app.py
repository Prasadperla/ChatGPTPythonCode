from flask import Flask, render_template, request
import pymysql

app = Flask(__name__)

db = pymysql.connect(
    host="mysql-service",
    user="root",
    password="password",
    database="employee"
)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/add', methods=['POST'])
def add_employee():
    name = request.form['name']

    cursor = db.cursor()

    sql = "INSERT INTO employees(name) VALUES(%s)"
    cursor.execute(sql, (name,))
    db.commit()

    return f"{name} added successfully"

@app.route('/employees')
def employees():

    cursor = db.cursor()

    cursor.execute("SELECT * FROM employees")

    data = cursor.fetchall()

    result = ""

    for row in data:
        result += f"{row}<br>"

    return result


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
