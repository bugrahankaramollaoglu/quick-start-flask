from flask import Flask
from flask import url_for

# To build a URL to a specific function, use the url_for() function.

app = Flask(__name__)


@app.route('/hello')
def hello():
    return 'Hello, Flask!'


@app.route('/user/<username>')
def profile(username):
    return f'User: {username}'


with app.test_request_context():
    url = url_for('hello')
    url2 = url_for('profile', username='johndoe')
    print(url)
    print(url2)

# usage
# http://127.0.0.1:5000/hello
# http://127.0.0.1:5000/user/mehmet


if __name__ == '__main__':
    app.run(debug=True)
