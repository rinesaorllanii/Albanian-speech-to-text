import psycopg2
from flask import Flask, render_template, request, redirect, url_for

from components.user import User

app = Flask(__name__)

@app.route('/')
def home():
    return render_template('index.html')

@app.route('/contact')
def contact():
    return render_template('contact.html')

@app.route('/about')
def about():
    return render_template('about.html')

@app.route('/login')
def login():
    return render_template('login.html')

@app.route('/register')
def register():
    return render_template('register.html')

def db_conn():
    conn = psycopg2.connect(database="astt_db", host="localhost", user="postgres", password="postgres", port="5432")
    return conn

@app.route('/')
def index():
    conn = db_conn()
    cur = conn.cursor()
    cur.execute('''SELECT * FROM users''')
    data = cur.fetchall();
    cur.close();
    conn.close();
    return render_template('index.html', data = data)

@app.route('/create', methods=['POST'])
def createUser():
    username = request.form['username']
    email = request.form['email']
    password = request.form['password']
    level = request.form['security_level']
    user = User(username, email, password, level)
    user.add_user()
    return render_template('login.html')

if __name__ == '__main__':
    app.run(debug=True)