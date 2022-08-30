from flask import Flask, render_template, request, session
from DBConnection import Db

app = Flask(__name__)
app.secret_key = "hii"


@app.route('/')
def login():
    return render_template('loginindex.html')


@app.route('/login_post', methods=['post'])
def login_post():
    Username = request.form['name']
    Password = request.form['name2']
    db = Db()
    qry = "SELECT * FROM login WHERE Username='" + Username + "' AND PASSWORD='" + Password + "'"
    print(qry)
    res = db.selectOne(qry)
    if res is not None:
        session['lid'] = res['Login_id']
        if res["Type"] == "Admin":
            return "<script>alert('success');window.location='/AdminHome';</script>"

        else:
            return "Invalid"
    else:

        return "<script>alert('Invalid details');window.location='/';</script>"


@app.route('/AdminHome')
def AdminHome():
    return render_template('Admin/Home.html')


@app.route('/Add_course')
def Add_course():
    db = Db()
    qry = "select * from department"
    res = db.select(qry)
    return render_template('Admin/Add_Course.html', data=res)


@app.route('/Add_Course_post', methods=['post'])
def Add_Course_post():
    deptname = request.form['select']
    coursename = request.form['textfield']
    db = Db()
    qry = "INSERT INTO course(Course_name,Dept_id)VALUES('" + coursename + "','" + deptname + "')"
    db.insert(qry)

    return Add_course()


@app.route('/View_course')
def View_course():
    q = "select department.*,course.* from department inner join course on course.Dept_id=department.Dept_id"
    d = Db()
    res = d.select(q)

    qry2 = "select * from department"
    res2 = d.select(qry2)
    return render_template('Admin/View_Course.html', data=res, dept=res2)


@app.route('/View_course_search', methods=["post"])
def View_course_search():
    dep = request.form["select"]
    q = "select department.*,course.* from department inner join course on course.Dept_id=department.Dept_id where course.Dept_id='" + dep + "'"
    d = Db()
    res = d.select(q)

    qry2 = "select * from department"
    res2 = d.select(qry2)
    return render_template('Admin/View_Course.html', data=res, dept=res2)


@app.route('/delete_course/<id>')
def delete_course(id):
    q = "delete from course where Course_id='" + id + "'"
    d = Db()
    res = d.delete(q)
    return View_course()


@app.route('/Add_Department')
def Add_Department():
    return render_template('Admin/Add_Department.html')


@app.route('/Add_Department_post', methods=['post'])
def Add_Department_post():
    deptname = request.form['textfield']
    db = Db()
    qry = "INSERT INTO department (Dept_name)VALUES('" + deptname + "')"
    db.insert(qry)
    return Add_Department()


@app.route('/view_dept')
def view_dept():
    q = "select * from department"
    d = Db()
    res = d.select(q)
    return render_template('Admin/View_Department.html', data=res)


@app.route('/view_dept_delete/<id>')
def view_dept_delete(id):
    q = "delete from department where Dept_id='" + id + "'"
    d = Db()
    res = d.delete(q)
    return view_dept()


@app.route('/Add_Question')
def Add_Question():
    # from accuracy_check import placement
    # ob=placement()
    # score=ob.pred()
    score = ""

    return render_template('Admin/Add_Question.html', res="", sc=score)


@app.route('/Add_Question_post', methods=['post'])
def Add_Question_post():
    question = request.form['textfield']
    opta = request.form['textfield6']
    optb = request.form['textfield2']
    optc = request.form['textfield3']
    optd = request.form['textfield4']
    crrctanswer = request.form['textfield5']

    from checking import placement
    placem = placement()
    result = placem.pred(question)

    db = Db()
    qry = "insert into question(Question,Answer,Difficulty_level,Option1,Option2,Option3,Option4) values('" + question + "','" + crrctanswer + "','" + result + "','" + opta + "','" + optb + "','" + optc + "','" + optd + "')"
    db.insert(qry)

    from accuracy_check import placement
    ob = placement()
    score = ob.pred()
    return render_template('Admin/Add_Question.html', res=result, sc=score)


@app.route('/view_question')
def view_question():
    q = "select * from question"
    d = Db()
    res = d.select(q)
    return render_template('Admin/View_Question.html', data=res)


@app.route('/delete_questions/<id>')
def delete_questions(id):
    q = "delete from question where Q_id='" + id + "'"
    d = Db()
    d.delete(q)
    return view_question()


@app.route('/Add_Student')
def Add_Student():
    db = Db()
    qry = "select * from course"
    res = db.select(qry)
    return render_template('Admin/Add_Student.html', data=res)


@app.route('/Add_Student_post', methods=['post'])
def Add_Student_post():
    name = request.form['textfield']
    course = request.form['select']
    sem = request.form['select2']
    admno = request.form['textfield2']
    dob = request.form['textfield3']
    email = request.form['textfield4']
    phone = request.form['textfield5']
    qry = "INSERT INTO login(Username,PASSWORD,TYPE)VALUES('" + email + "','" + phone + "','Student')"
    db = Db()
    lid = db.insert(qry)
    qry1 = "INSERT INTO student VALUES('" + str(
        lid) + "','" + name + "','" + course + "','" + sem + "','" + admno + "','" + dob + "','" + email + "','" + phone + "')"
    db.insert(qry1)
    return Add_Student()


@app.route('/view_student')
def view_student():
    q = "select student.*,course.* from student inner join course on student.Course_id=course.Course_id"
    d = Db()
    res = d.select(q)

    qry2 = "select * from course"
    res2 = d.select(qry2)
    return render_template('Admin/View_Student.html', data=res, course=res2)


@app.route('/view_student_post', methods=["post"])
def view_student_post():
    cid = request.form["cid"]
    q = "select student.*,course.* from student inner join course on student.Course_id=course.Course_id where student.Course_id='" + cid + "'"
    d = Db()
    res = d.select(q)

    qry2 = "select * from course"
    res2 = d.select(qry2)
    return render_template('Admin/View_Student.html', data=res, course=res2)


@app.route('/delete_student/<id>')
def delete_student(id):
    q = "delete from student where S_id='" + id + "'"
    d = Db()
    res = d.delete(q)
    return view_student()


@app.route('/Send_Reply')
def Send_Reply():
    return render_template('Admin/Send_Reply.html')


@app.route('/Send_Reply_post', methods=['post'])
def Send_Reply_post():
    reply = request.form['textarea']
    return "ok"


@app.route('/home')
def home():
    return render_template('Admin/home.html')


if __name__ == '__main__':
    app.run(debug=True)
