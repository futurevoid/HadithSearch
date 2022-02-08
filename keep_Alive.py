from flask import Flask
from threading import Thread
from waitress import serve

app = Flask('')

@app.route('/')
def home():
    return "I'm alive"

if __name__ == "__main__":
    serve(app.run, host="0.0.0.0", port=8080)
#def run():
  #app.run(host='0.0.0.0',port=8080)

def keep_alive():
    t = Thread(target=serve)
    t.start()
