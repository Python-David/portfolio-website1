import smtplib
import os
from flask import Flask, render_template, request, send_from_directory
from flask_bootstrap import Bootstrap

app = Flask(__name__)
app.config['SECRET_KEY'] = os.environ["SECRET_KEY"]
Bootstrap(app)

app_password = os.environ["APP_PASSWORD"]


@app.route("/")
def index():
    return render_template("index.html")


@app.route("/contact", methods=["GET", "POST"])
def contact():
    if request.method == "POST":
        data = request.form
        send_email(data["name"], data["email"], data["subject"], data["message"])

        return render_template("index.html")

    return render_template("contact2.html")


def send_email(name, email, subject, message):
    email_message = f"Subject:{subject}\n\nName: {name}\nEmail: {email}\nMessage:{message}"
    with smtplib.SMTP_SSL("smtp.mail.yahoo.com") as connection:
        connection.login(user="viperdavid123@yahoo.com", password=app_password)
        connection.sendmail(from_addr="viperdavid123@yahoo.com", to_addrs="pythondavid123@gmail.com",
                            msg=email_message)


@app.route('/download')
def download():
    return send_from_directory(directory='static', path='images/morse.png', as_attachment=True)


if __name__ == "__main__":
    app.run(debug=True)
