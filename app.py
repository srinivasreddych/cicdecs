from flask import Flask
app = Flask(__name__)

@app.route('/app')
def hello_world():
    return 'Hello World Guys/Gals'

if __name__ == '__main__':
    app.run(debug=True,host='0.0.0.0')
