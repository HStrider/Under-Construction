
from cs50 import SQL
from flask import Flask, flash, redirect, render_template, request
from flask_session import Session
import datetime


# Configure application
app = Flask(__name__)


# Configure session to use filesystem (instead of signed cookies)
app.config["SESSION_PERMANENT"] = False
app.config["SESSION_TYPE"] = "filesystem"
Session(app)

# Configure CS50 Library to use SQLite database
db = SQL("sqlite:///customers.db")

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/payment")
def payment():
    return render_template("payment.html")

@app.route("/bim")
def bim():
    return render_template("bim.html")

@app.route("/arcgis")
def arcgis():
    return render_template("arcgis.html")

@app.route("/management")
def management():
    return render_template("management.html")

@app.route("/apology")
def apology():
    return render_template("apology.html")

@app.route("/thanks")
def thanks():
    return render_template("thanks.html")

@app.route("/contact" , methods=["GET", "POST"])
def contact():
    if request.method == "GET":
        return render_template("contact.html")
    else:
        name = request.form.get("name")
        email = request.form.get("email")
        number = request.form.get("phone")
        message = request.form.get("message")
        if not name:
            flash("please enter your name in the fourm")
        if not email:
            flash("please enter your name in the fourm")
        date = datetime.datetime.now()
        db.execute("INSERT into people(name,email,number,message,date) VALUES (?,?,?,?,?)", name , email , number , message , date)
        return render_template("thanks.html")
        return redirect("thanks.html")
