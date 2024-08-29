'''Project name:-MUltiple file uploader

Date of publish:-25/08/24

Author:-Denzil Roy.I

About:-A mini project to upload multiple files using
flask in python

@COPYRIGHTS RESERVED www.github.com/Denzilroy14'''
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
