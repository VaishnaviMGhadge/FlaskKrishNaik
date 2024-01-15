#building URL dynamically 
# variables rules and URL bindings


from flask import Flask,jsonify,redirect,url_for,render_template,request
app=Flask(__name__)


@app.route("/")
def welcome():
    return render_template("index.html")

@app.route('/success/<int:score>')
def success(score):
    return f'the person passed the exams with  {score} marks'

@app.route('/fail/<int:score>')
def fail(score):
    return f'the person failed the exams with {score} marks'

"""@app.route('/check/<int:score>')
def checker(score):
    if(score<40):
        return redirect (url_for("fail",score=score))
    else:
        return redirect (url_for("success",score=score))"""
    

@app.route('/submit',methods=['GET','POST'])
def submit():
    
    if(request.method=='POST'):
        total_score=0
        science=float(request.form['science'])
        maths=float(request.form['maths'])
        c=float(request.form['c'])
        datascience=float(request.form['datascience'])
        total_score=(science+maths+c+datascience)/4
    res=""
    if(total_score>50):
        res="success"
        return redirect(url_for("success",score=total_score))
    else:
        res='fail'
        return jsonify(total_score)
    return redirect (url_for(res,score=total_score))
    



if __name__=="__main__":
    app.run(debug=True)