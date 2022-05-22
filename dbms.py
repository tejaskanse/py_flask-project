import pymysql as p

def getConnection():
    return p.connect(host="localhost",
    user="root",
    port=3306,
    database="company")

#registration code
def addData(t):
    con=getConnection()
    cur=con.cursor()
    query1="insert into employee(name,email,mob,address,age,gender,password) values(%s,%s,%s,%s,%s,%s,%s)"
    cur.execute(query1,t)
    con.commit()
    con.close() 

def fetchData(): 
    con=getConnection()
    cur=con.cursor()
    cur.execute("select * from employee")
    datalist=cur.fetchall()
    con.commit()
    con.close()  
    return datalist

def specificData(id):
    con=getConnection()
    cur=con.cursor()
    cur.execute("select * from employee where id=%s",(id,))
    datalist=cur.fetchall()
    con.commit()
    con.close()  
    return datalist[0]

def updateData(t):
    con=getConnection()
    cur=con.cursor()
    query1="update employee set name=%s,email=%s,mob=%s,address=%s,age=%s,gender=%s,password=%s where id=%s"
    cur.execute(query1,t)
    con.commit()
    con.close()  

def deleteData(id):
    con=getConnection()
    cur=con.cursor()
    query1="delete from employee where id=%s"
    cur.execute(query1,(id,))
    con.commit()
    con.close()  

#contact us
def addData1(t1):
    con=getConnection()
    cur=con.cursor()
    query2="insert into contactus(name,email,subject,message) values(%s,%s,%s,%s)"
    cur.execute(query2,t1)
    con.commit()
    con.close() 

def fetchData1(): 
    con=getConnection()
    cur=con.cursor()
    cur.execute("select * from contactus")
    datalist1=cur.fetchall()
    con.commit()
    con.close()  
    return datalist1