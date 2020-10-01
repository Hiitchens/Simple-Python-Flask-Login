import urllib.request, re
from flask import Flask, redirect, render_template, request, session
import scrape
app = Flask(__name__)
app.secret_key = "BigChungusWholesome"

@app.route('/', methods=["GET", "POST"])
def login():
    if request.method == "GET":
        # if session['isLoggedIn']:
        #     redirect("/secure")
        # else:
            return render_template("loginTemplate.html")
    elif request.method == "POST":
        if request.form.get("email") == "test@test.net" and request.form.get("password") == "myAwesomePassword":
            session['isLoggedIn'] = 'Chungus'
            return redirect('/secure')
        else:
            return redirect("/")
    else:
        return "You shouldnt be here"


@app.route('/secure', methods=["GET"])
def secureLogin():
    key = session.get('isLoggedIn') == 'Chungus'
    if key:
        email = key
        return render_template("secureTemplate.html", username=key)
    else:
        return redirect('/')

@app.route('/logout')
def logout():
    session.pop('isLoggedIn', None)
    redirect('/')




