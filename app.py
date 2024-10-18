from flask import Flask, redirect, request, render_template
import pickle
import numpy as np

app = Flask(__name__)

@app.route("/")
def fun1():
    return render_template("info.html")

@app.route("/predict", methods = ["post"])
def fun2():
    nm = request.form['name']
    exp = float(request.form['exp'])
    mymodel = pickle.load(open('model1.pkl',"rb"))
    sal = round(mymodel.predict([[exp]])[0],2)
    #return "<h1>Hi {} <br/> your predicted salary is {} </h1>".format(nm,sal)
    return render_template("second.html", name = nm, salary = sal)

if __name__ == "__main__":
    app.run(debug=True)
    #app.run(host='0.0.0.0', port=8080)