from flask import Flask, render_template, url_for, flash, redirect
from forms import LoginForm, RegistrationForm
app = Flask(__name__)

# import secrets
# secrets.token_hex(16)
app.config['SECRET_KEY'] = '785ed885c477272acc2eeb7c5f26cc75'

posts = [
    {
        'author': 'George Orwell',
        'title': 'Down and out in Paris London',
        'content': 'First post content',
        'date_posted': 'Jan 9, 1933'
    },
    {
        'author': 'Big Brother',
        'title': 'I am the book',
        'content': 'Always watching',
        'date_posted': 'Jan 1, 1989'
    }
]

@app.route("/")
@app.route("/home")
def home():
    return render_template('home.html', posts = posts, title = "Testing...")

@app.route("/about")
def about():
    return(render_template('about.html'))

@app.route("/login")
def login():
    form = LoginForm()
    return(render_template('login.html', title = 'Login', form = form))

@app.route("/register", methods = ['GET', 'POST'])
def register():
    form = RegistrationForm()
    if form.validate_on_submit():
        flash(f'Account created for {form.username.data}!', 'success')
        return redirect(url_for('home'))
    return(render_template('register.html', title = 'Register', form = form))

if (__name__ == "__main__"):
    app.run(debug=True)
