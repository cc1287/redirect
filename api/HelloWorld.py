from flask import *

app = Flask(__name__)


# Hello World
@app.route('/')
def root():
    return 'Hello World!'


app.run()
