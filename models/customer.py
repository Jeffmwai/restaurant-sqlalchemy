from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import relationship
from sqlalchemy.orm.session import Session  
from . import Base
from models.review import Review 

class Customer(Base):
    __tablename__ = 'customers'

    id = Column(Integer, primary_key=True)
    first_name = Column(String)
    last_name = Column(String)

    reviews = relationship('Review', back_populates='customer')

    def full_name(self):
        return f"{self.first_name} {self.last_name}"

    def favorite_restaurant(self):
        return max([review.restaurant for review in self.reviews], key=lambda r: r.average_star_rating())

    def add_review(self, session: Session, restaurant, rating):
        review = Review(customer=self, restaurant=restaurant, star_rating=rating)
        self.reviews.append(review)
        session.add(review)
        session.commit()

    def delete_reviews(self, session: Session, restaurant):
        reviews_to_delete = [review for review in self.reviews if review.restaurant == restaurant]
        for review in reviews_to_delete:
            session.delete(review)
        session.commit()

    def get_all_reviews(self):
        return [review.full_review() for review in self.reviews]

    def get_all_restaurants(self):
        return [review.restaurant for review in self.reviews]
