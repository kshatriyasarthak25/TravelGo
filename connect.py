from flask import Flask, render_template

app = Flask(__name__)

@app.route('/')
def index():
    return render_template('login.html')

@app.route('/signup')
def signup():
    return render_template('signup.html')

# Your other routes and logic
@app.route('/login', methods=['POST'])
def login():
    # Access form data using request.form, e.g., request.form['username']
    # Perform login logic here
    return "Login successful"  # or redirect to another page

@app.route('/signup', methods=['POST'], endpoint='signup_page')
def signup():
    # Access form data using request.form, e.g., request.form['name']
    # Perform signup logic here
    return "Signup successful"  # or redirect to another page
