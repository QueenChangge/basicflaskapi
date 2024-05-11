from flask import Flask, render_template, redirect, url_for
import config.database as db

app = Flask(__name__)

# MAIN
@app.route('/')
def main():
    val = db.showStudents()
    return render_template('index.html', data=val)


# ADDING NEW STUDENT
@app.route('/add-student')
def addStudent():
    return render_template('add-student.html')

@app.route('/student/insert', methods=['POST'])
def insert():
    db.insert()
    # data = db.showStudents()
    # print(data)
    # return render_template('index.html', data=data)
    return redirect(url_for('main'))


# PROCESSING TO DELETE
@app.route('/student/delete/<int:id_data>', methods= ['GET'])
def delete(id_data):
    db.deleteStudent(id_data)
    return redirect(url_for('main'))


# UPDATING STUDENT DATA
@app.route('/student/edit/<int:id_data>', methods= ['POST','GET'])
def update(id_data):
    val = db.editStudent(id_data)
    return render_template('edit-student.html', data=val)

if __name__ == "__main__":
    app.run(debug=True)