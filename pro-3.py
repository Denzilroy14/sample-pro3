'''        Mini-project-1
Name:-Multiple file uploaded
Author:- Denzil Roy.I
About:-
A multiple file uploaded that allows user to upload multiple files on a website or an app etc....

Features:
1.Can upload multiple files 
2.Download uploaded files

@COPYRIGHT-www.github.com//Denzilroy14(NOTE:- THIS PROJECT CONTAINS THE LICENSCE FOR 
WHICH IF USED WITHOUT PERMISSION OF AUTHOR WOULD BE CHARGED PENALTY)
FOR MORE QUERIES CONTACT @denzilroy80@gmail.com
'''
from flask import*
import sqlite3
app=Flask(__name__)
@app.route('/')
def index():
    return render_template('uploadpage.html')
@app.route('/upload',methods=['GET','POST'])
def upload():
    if request.method=='POST':
        files=request.files.getlist('file')
        for file in files:
              file.save(file.filename)
        return "<html><body<h1>Files uploaded succesfully</h1></body></html"
if __name__=='__main__':
    app.run(debug=True)
