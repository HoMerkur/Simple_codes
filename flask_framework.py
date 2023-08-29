from flask import Flask

app = Flask(__name__)

@app.route("/")
def anasayfa():
    return "Ana Sayfa"
@app.route("/hakimizda")
def hakkimizda():
    return "Hakkımızda"
@app.route("/makaleler")
def makaleler():
    return "makaleler"

if __name__ == "__main__":
    app.run(debug=True)