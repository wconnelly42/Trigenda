from app import app
from flask import render_template, request
from app.models import model, formopener

@app.route('/')
@app.route('/index')
def index():
    return render_template("index.html")
@app.route('/genda')
def genda():
    return render_template("genda.html")


@app.route('/results', methods=['GET','POST'])
def results():
    if request.form == 'GET':
        return render_template("results.html")
    else:
        print(request.form)
        userdata = dict(request.form)
        print(userdata)
        city = userdata['yourCity']
        pack = model.whatToPack(city)
        return render_template("results.html", a = pack["desc"])  