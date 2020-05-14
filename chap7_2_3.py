from flask import Flask

app = Flask(__name__)

@app.route("/") # 루트경로 만듬
def hello():
    return"<h1>Hello World! ;3 </h1>"

app.run(host='127.0.0.1',debug = True)
