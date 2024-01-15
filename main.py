##integrating HTML with Flask (called as jinja technique)
## HTTp verbs like GET POST PUTfrom flask import Flask

from flask import Flask,render_template
##WSGI Application
app=Flask(__name__)

@app.route('/')
def welcome():
    return  render_template("index.html")

@app.route('/submit',methods=['GET','POST'])



if __name__=="__main__":
    app.run(debug=True)