import sqlite3  as sql 
from flask import Flask, render_template 
con= sql.connect('/home/dion/myapp/mydatabase1.db',check_same_thread=False)
cursor = con.cursor() 
app=Flask(__name__)
#CORS(app)
@app.route("/", methods=['GET','POST'] )
def example(): 
    cursor.execute("select * from mytable1") 
    data = cursor.fetchall() #data from database 
    return render_template("index.html", value=data) 


if __name__ =="__main__":
   app.run(debug=True)