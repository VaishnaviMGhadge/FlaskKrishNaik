from flask import Flask,request,render_template,redirect,url_for,jsonify
app=Flask(__name__)


@app.route("/")
def index():
    return render_template("index.html")


@app.route('/submit',methods=['GET','POST'])
def submit():
    
    if(request.method=='POST'):
        total_score=0
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        c=float(request.form['c'])
        datascience=float(request.form['datascience'])
        total_score=(science+maths+c+datascience)/4
        return jsonify(total_score)
    else:
        return 'it"s working!!'
    
        



if __name__=="__main__":
    app.run(debug=True)