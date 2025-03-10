# created from response - used to create database and project
#  should run without error
#  if not, check for decimal, indent, or import issues

import decimal

import logging



logging.getLogger('sqlalchemy.engine.Engine').disabled = True  # remove for additional logging

import sqlalchemy



from sqlalchemy.sql import func  # end imports from system/genai/create_db_models_inserts/create_db_models_prefix.py

from logic_bank.logic_bank import Rule

from sqlalchemy import create_engine, Column, Integer, String, Float, DateTime, ForeignKey, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker, relationship
from datetime import datetime, timedelta

Base = declarative_base()
DATABASE_URI = 'sqlite:///system/genai/temp/create_db_models.sqlite'
engine = create_engine(DATABASE_URI)

# Defining data models

class Customer(Base):
    """description: Represents a customer in the system with balance and credit limit."""
    __tablename__ = 'customers'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    balance = Column(Float, default=0.0)
    credit_limit = Column(Float, default=1000.0)


class Order(Base):
    """description: Contains information about customer orders, including the order total and notes."""
    __tablename__ = 'orders'
    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)
    amount_total = Column(Float, default=0.0)
    date_shipped = Column(DateTime, nullable=True)
    notes = Column(String, nullable=True)


class Item(Base):
    """description: Details each item within an order, including its unit price and calculated amount."""
    __tablename__ = 'items'
    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey('orders.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    quantity = Column(Integer, nullable=False, default=1)
    unit_price = Column(Float, nullable=False, default=0.0)
    amount = Column(Float, default=0.0)  # calculated as quantity * unit_price


class Product(Base):
    """description: Represents a product available in the system with its base unit price."""
    __tablename__ = 'products'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    unit_price = Column(Float, nullable=False)


class Supplier(Base):
    """description: A supplier that provides products to the inventory."""
    __tablename__ = 'suppliers'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    contact_info = Column(String, nullable=True)


class Inventory(Base):
    """description: Tracks the quantity of each product in stock."""
    __tablename__ = 'inventory'
    id = Column(Integer, primary_key=True, autoincrement=True)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    quantity_in_stock = Column(Integer, default=0)


class OrderStatus(Base):
    """description: Represents various statuses an order can have."""
    __tablename__ = 'order_status'
    id = Column(Integer, primary_key=True, autoincrement=True)
    status_name = Column(String, nullable=False)


class Payment(Base):
    """description: Details the methods of payment received for orders."""
    __tablename__ = 'payments'
    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey('orders.id'), nullable=False)
    payment_date = Column(DateTime, nullable=False)
    amount = Column(Float, nullable=False)
    method = Column(String, nullable=False)


class CustomerSupport(Base):
    """description: Tracks customer support requests and issues."""
    __tablename__ = 'customer_support'
    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)
    issue_description = Column(String, nullable=False)
    resolved = Column(Boolean, default=False)


class Shipment(Base):
    """description: Manages outbound shipments and their statuses."""
    __tablename__ = 'shipments'
    id = Column(Integer, primary_key=True, autoincrement=True)
    order_id = Column(Integer, ForeignKey('orders.id'), nullable=False)
    shipment_date = Column(DateTime, nullable=False)
    delivered = Column(Boolean, default=False)


class Review(Base):
    """description: Captures customer reviews and ratings for products."""
    __tablename__ = 'reviews'
    id = Column(Integer, primary_key=True, autoincrement=True)
    customer_id = Column(Integer, ForeignKey('customers.id'), nullable=False)
    product_id = Column(Integer, ForeignKey('products.id'), nullable=False)
    rating = Column(Integer, nullable=False)
    comment = Column(String, nullable=True)


class Promotion(Base):
    """description: Details promotional offers for products."""
    __tablename__ = 'promotions'
    id = Column(Integer, primary_key=True, autoincrement=True)
    name = Column(String, nullable=False)
    discount_percentage = Column(Float, nullable=False)


# Create all tables
Base.metadata.create_all(engine)

# Sample data insertion
Session = sessionmaker(bind=engine)
session = Session()

# Sample Customers
customers = [
    Customer(name="Alice", balance=200.0, credit_limit=500.0),
    Customer(name="Bob", balance=300.0, credit_limit=700.0),
    Customer(name="Charlie", balance=50.0, credit_limit=400.0)
]

# Sample Products
products = [
    Product(name="Widget", unit_price=10.0),
    Product(name="Gadget", unit_price=20.0),
    Product(name="Thingamajig", unit_price=30.0)
]

# Sample Orders and Items
orders = [
    Order(customer_id=1, amount_total=0.0, date_shipped=datetime.now() - timedelta(days=1), notes="Fast delivery"),
    Order(customer_id=2, amount_total=0.0, date_shipped=None, notes="Pending items availability"),
    Order(customer_id=3, amount_total=0.0, date_shipped=datetime.now(), notes="Delayed shipment")
]

items = [
    Item(order_id=1, product_id=1, quantity=2, unit_price=10.0, amount=20.0),
    Item(order_id=2, product_id=2, quantity=1, unit_price=20.0, amount=20.0),
    Item(order_id=3, product_id=3, quantity=3, unit_price=30.0, amount=90.0)
]

# More sample data
suppliers = [
    Supplier(name="Supplier A", contact_info="contact@supplierA.com"),
    Supplier(name="Supplier B", contact_info="contact@supplierB.com")
]

inventory = [
    Inventory(product_id=1, quantity_in_stock=100),
    Inventory(product_id=2, quantity_in_stock=150),
    Inventory(product_id=3, quantity_in_stock=200)
]

order_statuses = [
    OrderStatus(status_name="Pending"),
    OrderStatus(status_name="Shipped"),
    OrderStatus(status_name="Delivered")
]

payments = [
    Payment(order_id=1, payment_date=datetime.now() - timedelta(days=2), amount=20.0, method="Credit Card"),
    Payment(order_id=2, payment_date=datetime.now() - timedelta(days=1), amount=20.0, method="PayPal")
]

customer_supports = [
    CustomerSupport(customer_id=1, issue_description="Item not delivered", resolved=False),
    CustomerSupport(customer_id=2, issue_description="Order delayed", resolved=True)
]

shipments = [
    Shipment(order_id=1, shipment_date=datetime.now() - timedelta(days=1), delivered=True),
    Shipment(order_id=3, shipment_date=datetime.now(), delivered=False)
]

reviews = [
    Review(customer_id=1, product_id=1, rating=5, comment="Excellent product!"),
    Review(customer_id=2, product_id=2, rating=4, comment="Very useful."),
    Review(customer_id=3, product_id=3, rating=3, comment="Average quality.")
]

promotions = [
    Promotion(name="Summer Sale", discount_percentage=15.0),
    Promotion(name="Black Friday", discount_percentage=30.0)
]

# Adding the data to the session and committing
session.add_all(customers + products + orders + items + suppliers +
                inventory + order_statuses + payments + customer_supports +
                shipments + reviews + promotions)
session.commit()

# LogicBank Rule Implementation
def declare_logic():
    Rule.sum(derive=Customer.balance, as_sum_of=Order.amount_total, where=lambda row: row.date_shipped is None)
    Rule.sum(derive=Order.amount_total, as_sum_of=Item.amount)
    Rule.formula(derive=Item.amount, as_expression=lambda row: row.quantity * row.unit_price)
    Rule.copy(derive=Item.unit_price, from_parent=Product.unit_price)
    Rule.constraint(validate=Customer,
                    as_condition=lambda row: row.balance <= row.credit_limit,
                    error_msg="Customer balance ({row.balance}) exceeds credit limit ({row.credit_limit})")

# Closing session
session.close()
