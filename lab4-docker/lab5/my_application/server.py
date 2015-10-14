from flask import Flask
app = Flask(__name__)

@app.route("/hello")
def hello():
    return "Hello World!"

@app.route("/")
def index():
    return "Index Page"

@app.route("/user/<username>")
def show_user(username):
    return "User %s" % username

@app.route("/post/<int:post_id>")
def show_port(post_id):
    return "Post %d" % post_id


if __name__ == "__main__":
    app.run(host="0.0.0.0",debug=True)
