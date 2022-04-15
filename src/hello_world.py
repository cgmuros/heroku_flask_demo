from flask import Flask

app = Flask(__name__)

@app.route('/')
def index():
    return 'This is an example'

app.run(host='0.0.0.0', port=81)
