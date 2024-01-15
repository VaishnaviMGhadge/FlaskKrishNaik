from flask import Flask

##WSGI Application
app=Flask(__name__)

@app.route('/')
def welcome():
    return  '<h1>welcome to the flask learning!!</h1?'

@app.route("/members")
def welcome1():
    return '<div>the things are happening</div>'

if __name__=="__main__":
    app.run(debug=True)