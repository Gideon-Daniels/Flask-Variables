from flask import Flask, redirect, url_for

app = Flask(__name__)


@app.route("/")
def username():
    return "Welcome , please enter your name."


@app.route('/validate/<name>/')
def user_login(name):
    if name == 'Gideon':
        return redirect(url_for('admin', name=name))
    elif name == 'Daniels':
        return redirect(url_for('user', name=name))
    else:
        if name == 'Guest':
            return redirect(url_for('guest', name=name))


@app.route('/admin/<name>')
def admin(name):
    return "Welcome Admin %s" % name


@app.route('/user/<name>')
def user(name):
    return "Welcome User %s" % name


@app.route('/guest/<name>')
def guest(name):
    return "Welcome guest %s" % name


@app.route('/payment/<salary>')
def sa_home_loan(salary):
    if float(salary) > 10500.50:
        return redirect('/fnb')
    else:
        return redirect('/sahomeloan')


@app.route('/fnb')
def fnb():
    return "Welcome to FNB"


@app.route('/sahomeloan')
def sahomeloan():
    return "Welcome to sahomeloan"


if __name__ == "__main__":
    app.debug = True
    app.run()
