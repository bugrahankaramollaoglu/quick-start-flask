from markupsafe import escape
from flask import Flask

app = Flask(__name__)


@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return f'User --> {escape(username)}'


@app.route('/post/<int:post_id>')
def show_post(post_id):
    # show the post with the given id, the id is an integer
    return f'Post --> {post_id}'


if __name__ == '__main__':
    app.run(debug=True)


# kullanmak için açılan 127.0.0.1:500 sayfasında
# http://127.0.0.1:5000/user/bkaramol
# http://127.0.0.1:5000/post/123
