import sqlite3 as sql
from flask import Flask, render_template, request, redirect, url_for, session, flash

app = Flask(__name__)
host = "http://127.0.0.1:5000/"


@app.route('/register', methods=['GET', 'POST'])
def register():
    conn = sql.connect('hca_db.db')

    if request.method == 'POST':
        if "signup" in request.form:
            CreateUser(request.form['fullN'], request.form['email'], request.form['phoneN'], request.form['address'], request.form['userHeight'],
                       request.form['userWeight'], request.form['eyeColor'], request.form['userMC'], request.form['userPre'], request.form['psw'])

            return render_template('RegisPage.html', url=host)

    return render_template("RegisPage.html", error=None)


def CreateUser(name, email, phone, addr, height, weight, eyecolor, mc, pre, passw):
    conn = sql.connect('hca_db.db')
    conn.execute('INSERT INTO Users (name, email, phone, addr, height, weight, eyecolor, mc, pre, passw) VALUES (?,?,?,?,?,?,?,?,?,?)',
                 (name, email, phone, addr, height, weight, eyecolor, mc, pre, passw))
    conn.commit()


if __name__ == '__main__':
    app.run(debug=True)
