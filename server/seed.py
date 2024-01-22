#!/usr/bin/env python3
from random import choice as rc
from faker import Faker
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from app import app
from models import db, Restaurant, Pizza, RestaurantPizza

with app.app_context():

# This will delete any existing rows
# so you can run the seed file multiple times without having duplicate entries in your database
    print("Deleting data...")
    Pizza.query.delete()
    Restaurant.query.delete()
    RestaurantPizza.query.delete()

    print("Creating restaurants...")
    shack = Restaurant(name = "Karen's Pizza Shack", address = 'address1')
    bistro = Restaurant(name = "Sanjay's Pizza", address = 'address2')
    palace = Restaurant(name = "Kiki's Pizza", address = 'address3')
    aubergene = Restaurant(name = "Mary's Pizza", address = 'address4')
    pizzahut = Restaurant(name = "Joe's Pizza", address = 'address5')
    restaurants = [shack, bistro, palace, aubergene, pizzahut]

    print("Creating pizzas...")


    cheese = Pizza(name = "cheese", ingredients = "Dough, Tomato Sauce, Cheese")
    pepperoni = Pizza(name = "pepperoni", ingredients = "Dough, Tomato Sauce, Cheese, Pepperoni")
    california = Pizza(name = "california", ingredients = "Dough, Sauce, Ricotta, Red peppers, Mustard")
    french = Pizza(name = "french", ingredients = "Dough, Onions, Cheese")
    pineapple = Pizza(name = "pineapple", ingredients = "Dough, Pineapples, Cheese")
    pizzas = [cheese, pepperoni, california, french, pineapple]

    print("Creating RestaurantPizza...")

    pr1 = RestaurantPizza(restaurant = shack, pizza = cheese, price = 1)
    pr2 = RestaurantPizza(restaurant = bistro, pizza  = pepperoni, price = 4)
    pr3 = RestaurantPizza(restaurant = palace, pizza = california, price = 5)
    pr4 = RestaurantPizza(restaurant = aubergene, pizza = french, price = 7)
    pr5 = RestaurantPizza(restaurant = pizzahut, pizza = pineapple, price = 9)
    restaurantPizzas = [pr1, pr2, pr3, pr4, pr5]
    db.session.add_all(restaurants)
    db.session.add_all(pizzas)
    db.session.add_all(restaurantPizzas)
    db.session.commit()

    print("Seeding done!")