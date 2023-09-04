from flask import Flask

app = Flask(__name__)

@app.route('/')
def hello_world():
    return 'Hello, World!'

@app.route('/api/user')
def get_user():
    return 'Im a flask user'

if __name__ == '__main__':
    app.run(debug=True)

