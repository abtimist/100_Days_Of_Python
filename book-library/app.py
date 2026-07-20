from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///books.db"
db = SQLAlchemy(app)


class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(250), nullable=False)
    author = db.Column(db.String(250), nullable=False)
    rating = db.Column(db.Float, nullable=False)

    def __repr__(self):
        return f"<Book {self.title}>"


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    books = db.session.execute(db.select(Book).order_by(Book.title)).scalars().all()
    return render_template("index.html", books=books)


@app.route("/add", methods=["GET", "POST"])
def add():
    if request.method == "POST":
        book = Book(
            title=request.form["title"],
            author=request.form["author"],
            rating=float(request.form["rating"]),
        )
        db.session.add(book)
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("add.html")


@app.route("/edit/<int:book_id>", methods=["GET", "POST"])
def edit(book_id):
    book = db.get_or_404(Book, book_id)
    if request.method == "POST":
        book.rating = float(request.form["rating"])
        db.session.commit()
        return redirect(url_for("home"))
    return render_template("edit_rating.html", book=book)


@app.route("/delete/<int:book_id>")
def delete(book_id):
    book = db.get_or_404(Book, book_id)
    db.session.delete(book)
    db.session.commit()
    return redirect(url_for("home"))


if __name__ == "__main__":
    app.run(debug=True)
