from flask import Flask , render_template
import random as rm
from datetime import datetime
import requests

app = Flask(__name__)

BLOG_URL = "https://api.npoint.io/5631f6c4f10eccba7763"

@app.route("/")
def home():
    response = requests.get(BLOG_URL)
    response.raise_for_status()
    all_posts = response.json()
    return render_template("index.html" , posts = all_posts)

@app.route("/blog/<int:num>/")
def get_blog(num):
    response = requests.get(BLOG_URL)
    response.raise_for_status()
    all_posts = response.json()

    blog_post = next((post for post in all_posts if post["id"] == num), None)

    return render_template("post.html" , post = blog_post)

    


@app.route("/about")
def about():
    return render_template("about.html")

@app.route("/contact")
def contact():
    return render_template("contact.html")

@app.route("/post")
def post():
    return render_template("post.html")



if __name__ == "__main__" :
    app.run(debug=True  )
