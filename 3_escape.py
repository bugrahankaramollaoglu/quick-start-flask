from markupsafe import escape
from flask import Flask

app = Flask(__name__)

# If a user managed to submit the name <script>alert("bad")</script>,
# escaping causes it to be rendered as text, rather than running
# the script in the user’s browser.

@app.route("/<name>")
def hello(name):
    return f"Hello, {escape(name)}!"
