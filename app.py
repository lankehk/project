from flask import Flask, render_template, url_for
import pypyodbc
app = Flask(__name__)
connection1= pypyodbc.connect(
    "Driver={SQL Server};"
    "Server=;"
    "Database=;"
    "Trusted_Connection=yes;"
)

@app.route("/")
@app.route('/login')
def login():
    return render_template('login.html')


@app.route('/signup')
def signup():
    return render_template('signup.html')


@app.route('/forgotpassword')
def forgotpassword():
    return render_template('forgotpassword.html')


if __name__ == '__main__':
    app.run(debug=True)
