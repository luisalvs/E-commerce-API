from flask import Flask, request, jsonify
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
    if 'name' in data and 'price' in data:
        product = Product(name=data['name'], price=data['price'],
                          # model do produto, atributo e nome do produto
                          description=data.get('description', ''))
        db.session.add(product)  # adicionando produto ao db
        db.session.commit()
        return jsonify({'message': 'Product added successfully'})
    return jsonify({'message': 'Invalid product data'}), 400


@app.route('/api/products/delete/<int:product_id>', methods=['DELETE'])
def delete_product(product_id):
    # recuperar o produta da base de dados
    product = Product.query.get(product_id)
    if product != None:
        db.session.delete(product)
        db.session.commit()  # para realizar a mudança na base
        return jsonify({'message': 'Product deleted successfully'})
    return jsonify({'message': 'Product not found'}), 404


@app.route('/api/products/<int:product_id>', methods=['GET'])
def get_products_details(product_id):
    product = Product.query.get(product_id)
    if product:
        return jsonify({
            'id': product.id,
            'name': product.name,
            'price': product.price,
            'description': product.description
        })
    return jsonify({'message': 'Product not found'}), 404


if __name__ == '__main__':
    app.run(debug=True)
