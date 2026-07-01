from flask import Flask, render_template
import requests

app = Flask(__name__)
response=requests.get(url="https://api.npoint.io/dbc3a0f6d0a12c72b99a")

@app.route('/')
def home():
    posts = response.json()
    return render_template("index.html",posts=posts)

@app.route('/post/<int:id>')
def blog_post(id):
    posts = response.json()
    requested_post = None
    for post in posts:
        if post["id"] == id:
            requested_post = post
            break

    return render_template("post.html",
                           post_title=requested_post["title"],
                           post_body=requested_post["body"]
                           )



if __name__ == "__main__":
    app.run(debug=True)
