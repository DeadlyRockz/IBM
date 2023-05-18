from flask import Flask, render_template,request
import ibm_db
import re

app = Flask(__name__)
app.secret_key = 'a'
con = ibm_db.connect("DATABASE=bludb;HOSTNAME=fbd88901-ebdb-4a4f-a32e-9822b9fb237b.c1ogj3sd0tgtu0lqde00.databases.appdomain.cloud;PORT=32731;SECURITY=SSL;SSLServerCertificate=DigiCertGlobalRootCA.crt;UID=wyh10210;PWD=7pHZf8MoRZs1izdd;", "", "")
print("connection successful")

@app.route('/')
def home():
    return render_template('home.html')
@app.route('/login.html')
def logn():
    return render_template('login.html')
@app.route('/register.html')
def regis():
    return render_template('register.html')
@app.route('/fgpassword.html')
def fgpass():
    return render_template('fgpassword.html')
@app.route('/about.html')
def about():
    return render_template('about.html')
@app.route('/service.html')
def service():
    return render_template('service.html')
@app.route('/contact.html')
def contact():
    return render_template('contact.html')
@app.route('/img')
def img_res():
    return render_template('img_resizer.html')

@app.route('/login',methods=['POST'])
def login():
    Email=request.form['Email']
    Password=request.form['Password']
    sql = "SELECT * FROM REGISTRATION WHERE Email=? AND Password=?"
    smtp = ibm_db.prepare(con,sql)    
    ibm_db.bind_param(smtp, 1, Email)
    ibm_db.bind_param(smtp, 2, Password)
    ibm_db.execute(smtp)
    account=ibm_db.fetch_assoc(smtp)
    if account:
        return render_template('img_resizer.html')
    else:
        return render_template('register.html',msg='You have not registerd yet!')
    
@app.route('/register',methods=['POST'])
def register():
    Username=request.form['Username']
    Email=request.form['Email']
    Password=request.form['Password']
    insert_sql = "INSERT INTO REGISTRATION VALUES (?,?,?)"
    prepSql=ibm_db.prepare(con,insert_sql)
    ibm_db.bind_param(prepSql, 1, Username)
    ibm_db.bind_param(prepSql, 2, Email)
    ibm_db.bind_param(prepSql, 3, Password)
    result=ibm_db.execute(prepSql)
    return render_template('login.html',msg='You have successfully created an account and use this credentials for login')



if __name__=='__main__':
    app.run(debug=True, host='0.0.0.0')