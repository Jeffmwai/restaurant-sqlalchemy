from sqlalchemy.orm import Session
from models.customer import Customer  # Import Customer model
from models.restaurant import Restaurant  # Import Restaurant model
from models.review import Review  # Import Review model
from models import Base
from sqlalchemy import create_engine

# Update the database URL with a random SQLite URL
DATABASE_URL = 'sqlite:///example.db'
engine = create_engine(DATABASE_URL)

# Bind the engine to the Base class. This makes the Base class aware of the database engine.
Base.metadata.create_all(bind=engine)

# Create a session to interact with the database
session = Session(engine)

# Seed data example

# Create customers
customer1 = Customer(first_name='John', last_name='Doe')
customer2 = Customer(first_name='Jane', last_name='Smith')

session.add_all([customer1, customer2])
session.commit()

# Create restaurants
restaurant1 = Restaurant(name='Restaurant A', price=3)
restaurant2 = Restaurant(name='Restaurant B', price=2)

session.add_all([restaurant1, restaurant2])
session.commit()

# Create reviews
review1 = Review(star_rating=4, customer=customer1, restaurant=restaurant1)
review2 = Review(star_rating=5, customer=customer2, restaurant=restaurant1)
review3 = Review(star_rating=3, customer=customer1, restaurant=restaurant2)

session.add_all([review1, review2, review3])
session.commit()

# Close the session
session.close()
