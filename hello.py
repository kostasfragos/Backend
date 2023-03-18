from flask import Flask, render_template, request, redirect, url_for

app = Flask(__name__)

user_list = []

@app.route('/hello/')
@app.route('/hello/<name>')
def hello(name=None):
    return render_template('hello.html', name=name)

@app.get('/adduser')
def adduser(name=None):
    return render_template('userform.html')

@app.post('/adduser')
def adduser_data():
    print(request.form)

    user_list.append(request.form)

    return redirect(url_for('users'))

@app.route('/users')
def users():
    return render_template('users.html', users=user_list)