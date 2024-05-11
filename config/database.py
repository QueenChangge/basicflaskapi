# import request
from flask import request, render_template, redirect, url_for

# Perintah untuk mengimport package/library dari Mysql Connector
import mysql.connector as mysqlpy
import logging


# # inisialisasi data db
host = "localhost"
username = "root"
password = "Changge_034461"
db = "python_dasar"

# # menghubungkan python ke db
mysqldb = mysqlpy.connect(host=host, user=username, password=password, database=db)

# # membantu mengeksesusi perintah ke db
cursor = mysqldb.cursor()

# fungsi eksekusi query ke array
def queryRead(query_read):
    try:
        cursor.execute(query_read)
        records = cursor.fetchall()
        return records
    except:
        return "You have a error"


def showStudents():
    try:
        sql = "Select * from students"
        students = queryRead(sql)
        return students
    except:
        return []


def insert():
    try:
        if request.method == 'POST':
            nama = request.form['nama']
            email = request.form['email']
            nim = request.form['nim']
            jurusan = request.form['jurusan']
            gambar = "faddasfgd"
            sql = "INSERT INTO students VALUES(%s, %s, %s, %s, %s, %s)" 
            data = (None, nama, email, nim, jurusan, gambar)
            # cursor.execute( "INSERT INTO students VALUES(%s, %s, %s, %s, %s, %s )", (None, 'adfs', 'agver@df', 'fegvae', 'dgvsdf', 'rthg'))
            cursor.execute( sql, data)
            print("success inserting")
            mysqldb.commit()
            return showStudents()
            # message = "Succesffully added new student"
            
    except Exception as e:
        # Log the error
        logging.error(f"Error inserting student: {e}")

        # Return an error message or redirect to an error page
        return "An error occurred while adding the student."

def deleteStudent(data):
    try:
        # cursor.execute("DELETE FROM students WHERE id = %s", (data))
        sql = "DELETE FROM students WHERE id = %a"
        val = (data,) 

        cursor.execute(sql, val)
        mysqldb.commit()
        print("Successfully Deleted Student Data")
        return showStudents()
    except Exception as e:        # Log the error
        logging.error(f"Error deleting student: {e}")

        # Return an error message or redirect to an error page
        return "An error occurred while deleting the student."
    
def editStudent(data):
    try:
        
        if request.method == 'GET':
            cursor.execute(f"SELECT * FROM students WHERE id = {data}")
            result = cursor.fetchall()
            return result
        elif request.method == 'POST':
            id = request.form['id']
            nama = request.form['nama']
            email = request.form['email']
            nim = request.form['nim']
            jurusan = request.form['jurusan']
            gambar = "faddasfgd"
            # Parameterized SQL statement
            sql = "UPDATE students SET nama = %s, email = %s, nim = %s, jurusan = %s, gambar = %s WHERE id = %s"
            val = (nama, email, nim, jurusan, gambar, data)

            mycursor.execute(sql, val)
            mydb.commit()
            return redirect(url_for('main'))
        else:
            return []
    except Exception as e:        # Log the error
        logging.error(f"Error updating student: {e}")
        # Return an error message or redirect to an error page
        return "An error occurred while updating the student."
