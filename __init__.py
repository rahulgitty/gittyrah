from flask import Flask
from flask import Flask, render_template, request, flash, url_for, redirect, session
from content_management import Content

TOPIC_DICT = Content()

app = Flask(__name__)

@app.route('/')
def homepage():
    return render_template("Main.html")


@app.route('/dashboard/')
def dashboard():
	return render_template("dashboard.html", TOPIC_DICT = TOPIC_DICT)
	# flash("Welcome to 8K Online Store! Cart your Online purchases !!")
	# flash("Visit our Hot purchase Store for New Arrivals!! ")
	# flash("Get the biggest deals to your shopping Cart!! ")	
	# return render_template("dashboard.html", TOPIC_DICT = TOPIC_DICT, user = red['username'])

# @app.errorhandler(405)
# def method_not_found(e):
# 	return render_template("dashboard.html")


@app.errorhandler(500)
def page_not_found(e):
	return("<br/><br/><center><h1>Ouch !</h1>, <h2>Looks like you had knocked out!!</h2><h1> :( </h1> </center>")


@app.route('/slashboard/')
def slashboard(): 
	try:
		return render_template("dashboard.html", TOPIC_DICT = TOPIC_DICT )
	except Exception as e:
		return render_template("errorhandler.html")


@app.route('/allen/')
def allen():
	return render_template("allen.html",field1=A1,field2=A2, user = red['username'])

@app.route('/peter/')
def peter():
	return render_template("peter.html",field1=PE1)




if __name__ == "__main__":
    app.run()
