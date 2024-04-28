from flask import Flask

app = Flask(__name__)
@app.route("/")
def hello_flask():
    return "<p>"'Witaj w mojej aplikacji Flask!'"</p>"


@app.route('/about')
def show_blog():
   return "<p>"'Zaprogramowano przez Kamila.'"</p>"

@app.route('/contact')
def revision():
    return "<p>"'Email: kontakt@example.com.'"</p>"

if __name__ == '__main__':
   app.run(debug=True)