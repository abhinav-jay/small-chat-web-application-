import time
import pickle
# importing Flask and other modules
from flask import Flask, request, render_template
# Flask constructor
app = Flask(__name__)

@app.route('/', methods =["GET", "POST"])
def name():
    global user_input
    user_input=request.form.get("user_input")
    return render_template("name.html")


@app.route('/index', methods =["GET", "POST"])
def hello():
    # ls = ['first','second','third']
    # a = "first"
    # b = 'second'
    # c = 'third'
    ls = pickle.load( open( "save.p", "rb" ) )
    if request.method == "POST":
        
        # getting input with name = fname in HTML form
        name = request.form.get("firstname")
        ls.append(name)
        pickle.dump( ls, open( "save.p", "wb" ) )
        # a = ls[-1]
        # b = ls[-2]
        # c = ls[-3]
    return render_template("index.html", ls=ls, user_input=user_input )
   
if __name__=='__main__':
   app.run()
