from datetime import datetime

from flask import Flask, render_template, request, redirect, url_for, make_response
from flask_sqlalchemy import SQLAlchemy
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField
from wtforms.fields.html5 import EmailField
from wtforms.validators import InputRequired, AnyOf

app = Flask(__name__)

app.config['SECRET_KEY'] = "mark"
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite3:///db.sqlite3'

db = SQLAlchemy(app)


# creating a schema for the database
class FormDatabase(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    fullname = db.Column(db.String(50))
    email = db.Column(db.String(50))
    talent = db.Column(db.String(50))
    date_Created = db.Column(db.DateTime, default=datetime.now)


# validating the form

class ValidateForm(FlaskForm):
    fullName = StringField('FullName', validators=[InputRequired("Fullname is Required")])
    email = EmailField('Email', validators=[InputRequired("Email is Required")])
    talent = StringField('Talent', validators=[InputRequired("A talent must be inputed")])
    # adminPassword = PasswordField('adminPassword', validators=[AnyOf(values=['adminPassword', 'mark'])])


# router for the homePage

@app.route("/", methods=['POST', 'GET'])
def form():
    form = ValidateForm()
    if form.validate_on_submit():
        user = FormDatabase(fullname=form.fullName.data, email=form.email.data, talent=form.talent.data)
        # db.session.add(user)
        # db.session.commit()
        return 'Form has successfully been validated'

    return render_template('talent.html', form=form)


# router for the submision of the form
@app.route("/form", methods=['POST', 'GET'])
def FormSubmision():
    if request.methods == "POST":
        fullName = request.form["name"]
        skills = request.form["skills"]
    else:
        fullName = request.args.get("name")
        skills = request.args.get("skills")

    # Supposed skills
    supposedSkills = ["dancing", "drumming", "singing", "rapping", "prophetic words", "chanting"]

    def ValidatingSkills(x):
        for e in x:
            if e == skills.lower():
                return redirect(render_template("message.html", message="success"))
            else:
                return redirect(render_template("message.html", message="failure"))

    ValidatingSkills(supposedSkills)


if __name__ == "__main__":
    app.run(debug=True)
