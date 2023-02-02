from flask import Flask, render_template
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField
from wtforms.validators import DataRequired, Email
from secret_key import MY_SECRET_KEY
from flask_bootstrap import Bootstrap


class LoginForm(FlaskForm):
    email = StringField(label='Email', validators=[DataRequired(message='email입력'), Email()])
    password = PasswordField(label='Password', validators=[DataRequired(message='password입력')])
    submit = SubmitField(label="Log In")


app = Flask(__name__)
app.secret_key = MY_SECRET_KEY
Bootstrap(app)


@app.route("/")
def home():
    return render_template('index.html')


@app.route("/login", methods=["GET", "POST"])
def login():
    login_form = LoginForm()
    print(login_form)
    if login_form.validate_on_submit():
        if login_form.email.data == 'admin@email.com' and login_form.password.data == '1234':
            return render_template('success.html')
        else:
            return render_template('denied.html')
    return render_template('login.html', form=login_form)


if __name__ == '__main__':
    app.run(debug=True)
