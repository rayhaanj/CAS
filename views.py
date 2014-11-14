from flask import render_template, request, session, redirect
from application import app
from wrappers import logged_in

@app.route('/')
@app.route('/home')
@logged_in
def main():
	return "Hello"

@app.route('/login', methods=['GET', 'POST'])
def login():
	if request.method == 'GET':
		render_template('login.html')
	else:
		username = request.form['username']
		password = request.form['password']
		# TODO(rayhaan): actually make logging in work

@app.route('/fakelogin')
def fake():
	session['logged_in'] = 1
	return redirect('home')

@app.route('/logout')
def logout():
	session.clear()
	return redirect('home')

@app.route('/admin')
def admin():
	return 'Admin homepage'
