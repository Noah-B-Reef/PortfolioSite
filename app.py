from flask import Flask, render_template, redirect, request
import smtplib
import os

app = Flask(__name__)


@app.route('/')
def index():
	return render_template('index.html')

@app.route('/donate')
def donate():
	return redirect('https://www.buymeacoffee.com/NoahReef')

@app.route('/projects')
def projects():
	return render_template('projects.html')

@app.route('/contact', methods=["GET", "POST"])
def contact():
	if request.method == "POST":
		fname = request.form.get("fname")
		lname = request.form.get("lname")
		name = f'{fname} {lname}'
		msg = request.form.get("msg")
		email = request.form.get("email")

		SendEmail(name, email, msg)

	return render_template('contact.html')

def SendEmail(name, email, msg):
	site_email = os.environ['SITE_EMAIL']
	psswd = os.environ['SITE_PASSWORD']
	to = os.environ['MY_EMAIL']

	with smtplib.SMTP('smtp.gmail.com', 587) as smtp:
	  smtp.ehlo()
	  smtp.starttls()
	  smtp.ehlo()

	  smtp.login(str(site_email), str(psswd))
	  subject = "Portfolio Website Message"
	  body = f"Name: {name}\nEmail: {email}\n{msg}"
	  content = f'Subject: {subject}\n\n{body}'

	  smtp.sendmail(str(site_email), str(to) , content)