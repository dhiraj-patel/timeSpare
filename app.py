from flask import Flask, render_template, url_for, request, redirect, session
from utils import auth, dispEvent, dispFood, databaseIO

app = Flask(__name__)
app.secret_key = 'nine'

@app.route('/')
@app.route('/login')
def login():
	if 'user' in session:
		return redirect(url_for('home'))
	return render_template('login.html')
