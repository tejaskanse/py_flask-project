from flask import *
from dbms import *
from werkzeug.utils import secure_filename

app=Flask(__name__)
app.secret_key='abc'

app.config["UPLOAD_FOLDER"] = "static/"

@app.route("/")
def home_func():
    return render_template("home.html")

#registration code
@app.route("/reglink")
def reg_func():
    return render_template("registration.html")

@app.route("/savelink",methods=["POST"])
def regsave_fun():
    name=request.form['name']
    email=request.form['email']
    mob=request.form['mob']
    address=request.form['address']
    age=request.form['age']
    gender=request.form['gender']
    password=request.form['password']
    t=(name,email,mob,address,age,gender,password)
    addData(t)
    return redirect("/loglink")

#login code
@app.route("/loglink")
def login_fun():
    return render_template("login.html")

@app.route("/savelink2", methods=['POST'])
def loginsave_fun():
    if request.method=='POST' and 'email' in request.form and 'password' in request.form:
        email=request.form['email']
        password=request.form['password']
        con=getConnection()
        cur=con.cursor()
        cur.execute("select * from employee where email=%s AND password=%s",(email,password))
        result=cur.fetchone()
        if result:
           session['k']=True
           return redirect("/displaylink")
        else:
            return render_template("login.html")
    


#logout code
@app.route('/logoutlink')
def logout_fun():
    session.pop('Email',None)
    session.pop('Password',None)
    return render_template("home.html")

#display code
@app.route("/displaylink")
def display_func():
    datalist=fetchData()
    return render_template("display.html",data=datalist)

#edit code
@app.route('/editlink/<int:id>')
def displayforupdate(id):
    datalist=specificData(id)
    return render_template("edit.html",data=datalist)

#update code
@app.route('/updatelink/<int:id>',methods=["POST"])
def updatefun(id):
    name=request.form['name']
    email=request.form['email']
    mob=request.form['mob']
    address=request.form['address']
    age=request.form['age']
    gender=request.form['gender']
    password=request.form['password']
    t=(name,email,mob,address,age,gender,password,id)
    updateData(t)
    return redirect("/displaylink")

#delete code
@app.route('/deletelink/<int:id>')
def deletefun(id):
    deleteData(id)
    return redirect("/displaylink")

#about code
@app.route("/aboutlink")
def about_fun():
    return render_template("about.html")

#career 
@app.route("/careerlink")
def career_fun():
    return render_template("career.html")

#contactus code
@app.route("/contactlink")
def contact_fun():
    return render_template("contactus.html")

@app.route("/savelink3",methods=["POST"])
def cnctsave_fun():
    name=request.form['name']
    email=request.form['email']
    subject=request.form['subject']
    message=request.form['message']
    t1=(name,email,subject,message)
    addData1(t1)
    return redirect("/")

#career code
@app.route('/careerlink')
def upload_file():
    return render_template('career.html')

@app.route('/savelink4', methods = ['GET','POST'])
def display_file():
    if request.method == 'POST':
        f = request.files['file']
        filename = secure_filename(f.filename)

        f.save(app.config['UPLOAD_FOLDER'] + filename)

        file = open(app.config['UPLOAD_FOLDER'] + filename,"rb")
        content = file.read()   
        
    return render_template('home.html', content=content) 

if __name__=="__main__":
    app.run(debug=True) 