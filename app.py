from flask import Flask, request
from flask_sqlalchemy import SQLAlchemy

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///ecommerce.db'

db = SQLAlchemy(app)


class Product(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(120), nullable=False)  # não pode ser nulo
    price = db.Column(db.Float, nullable=False)
    # pode ou não ter description
    description = db.Column(db.Text, nullable=True)


@app.route('/api/products/add', methods=['POST'])
def add_product():
    data = request.json
    return data


if __name__ == '__main__':
    app.run(debug=True)
