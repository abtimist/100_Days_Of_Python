import random
from flask import Flask, jsonify, render_template, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config["SQLALCHEMY_DATABASE_URI"] = "sqlite:///cafes.db"
db = SQLAlchemy(app)

API_KEY = "TopSecretAPIKey"


class Cafe(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(250), unique=True, nullable=False)
    map_url = db.Column(db.String(500), nullable=False)
    img_url = db.Column(db.String(500), nullable=False)
    location = db.Column(db.String(250), nullable=False)
    seats = db.Column(db.String(250), nullable=False)
    has_toilet = db.Column(db.Boolean, nullable=False)
    has_wifi = db.Column(db.Boolean, nullable=False)
    has_sockets = db.Column(db.Boolean, nullable=False)
    can_take_calls = db.Column(db.Boolean, nullable=False)
    coffee_price = db.Column(db.String(250), nullable=True)

    def to_dict(self):
        return {col.name: getattr(self, col.name) for col in self.__table__.columns}


with app.app_context():
    db.create_all()


@app.route("/")
def home():
    return render_template("index.html")


@app.route("/random")
def get_random():
    cafes = db.session.execute(db.select(Cafe)).scalars().all()
    if not cafes:
        return jsonify(error="No cafes in the database yet."), 404
    return jsonify(cafe=random.choice(cafes).to_dict())


@app.route("/all")
def get_all():
    cafes = db.session.execute(db.select(Cafe).order_by(Cafe.name)).scalars().all()
    return jsonify(cafes=[c.to_dict() for c in cafes])


@app.route("/search")
def search():
    loc = request.args.get("loc", "")
    results = db.session.execute(db.select(Cafe).where(Cafe.location == loc)).scalars().all()
    if not results:
        return jsonify(error={"Not Found": f"No cafes in '{loc}'."}), 404
    return jsonify(cafes=[c.to_dict() for c in results])


@app.route("/add", methods=["POST"])
def add_cafe():
    cafe = Cafe(
        name=request.form.get("name"),
        map_url=request.form.get("map_url"),
        img_url=request.form.get("img_url"),
        location=request.form.get("loc"),
        seats=request.form.get("seats"),
        has_toilet=bool(request.form.get("toilet")),
        has_wifi=bool(request.form.get("wifi")),
        has_sockets=bool(request.form.get("sockets")),
        can_take_calls=bool(request.form.get("calls")),
        coffee_price=request.form.get("coffee_price"),
    )
    db.session.add(cafe)
    db.session.commit()
    return jsonify(response={"success": "Cafe added."})


@app.route("/update-price/<int:cafe_id>", methods=["PATCH"])
def update_price(cafe_id):
    cafe = db.get_or_404(Cafe, cafe_id, description="Cafe not found.")
    cafe.coffee_price = request.args.get("new_price")
    db.session.commit()
    return jsonify(response={"success": "Price updated."})


@app.route("/report-closed/<int:cafe_id>", methods=["DELETE"])
def delete_cafe(cafe_id):
    if request.args.get("api-key") != API_KEY:
        return jsonify(error="Not authorized."), 403
    cafe = db.get_or_404(Cafe, cafe_id, description="Cafe not found.")
    db.session.delete(cafe)
    db.session.commit()
    return jsonify(response={"success": "Cafe removed."})


if __name__ == "__main__":
    app.run(debug=True)
