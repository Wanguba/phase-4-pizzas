from flask import Flask, jsonify, request
from flask_sqlalchemy import SQLAlchemy
from sqlalchemy.exc import IntegrityError
from models import db, Restaurant, Pizza, RestaurantPizza
from flask_migrate import Migrate
from flask_cors import CORS

app = Flask(__name__)
CORS(app) 


app.config['SQLALCHEMY_DATABASE_URI'] = 'sqlite:///pizza_restaurants.db'
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
app.json.compact =False


migrate = Migrate(app,db)
db.init_app(app)

@app.route('/restaurants', methods=['GET'])
def get_restaurants():
    restaurants = Restaurant.query.all()
    result = [
        {"id": restaurant.id, "name": restaurant.name, "address": restaurant.address}
        for restaurant in restaurants
    ]
    return jsonify(result)

@app.route('/restaurants/<int:id>', methods=['GET'])
def get_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if restaurant:
        pizzas = [
            {"id": restaurant_pizza.pizza.id, "name": restaurant_pizza.pizza.name, "ingredients": restaurant_pizza.pizza.ingredients}
            for restaurant_pizza in restaurant.restaurant_pizzas
        ]
        result = {
            "id": restaurant.id,
            "name": restaurant.name,
            "address": restaurant.address,
            "pizzas": pizzas,
        }
        return jsonify(result)
    else:
        return jsonify({"error": "Restaurant not found"}), 404

@app.route('/restaurants/<int:id>', methods=['DELETE'])
def delete_restaurant(id):
    restaurant = Restaurant.query.get(id)
    if restaurant:
        # Delete associated RestaurantPizzas
        RestaurantPizza.query.filter_by(restaurant_id=id).delete()
        db.session.delete(restaurant)
        db.session.commit()
        return '', 204
    else:
        return jsonify({"error": "Restaurant not found"}), 404

@app.route('/pizzas', methods=['GET'])
def get_pizzas():
    pizzas = Pizza.query.all()
    result = [
        {"id": pizza.id, "name": pizza.name, "ingredients": pizza.ingredients}
        for pizza in pizzas
    ]
    return jsonify(result)

@app.route('/restaurant_pizzas', methods=['POST'])
def create_restaurant_pizza():
    data = request.get_json()
    try:
        new_pizza = RestaurantPizza(
            price=data['price'],
            pizza_id=data['pizza_id'],
            restaurant_id=data['restaurant_id'],
        )
        db.session.add(new_pizza)
        db.session.commit()
        pizza = Pizza.query.get(data['pizza_id'])
        return jsonify({
            "id": pizza.id,
            "name": pizza.name,
            "ingredients": pizza.ingredients
        }), 201
    except IntegrityError:
        db.session.rollback()
        return jsonify({"errors": ["Validation errors"]}), 400


if __name__ == '__main__':
    app.run(port=5555, debug=True)


