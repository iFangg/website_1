from flask import Flask, render_template, url_for
app = Flask(__name__)

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
    return(render_template('login.html'))

@app.route("/register")
def register():
    return(render_template('register.html'))

if (__name__ == "__main__"):
    app.run(debug=True)
