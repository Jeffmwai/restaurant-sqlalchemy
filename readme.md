# Restaurant Review Domain

## Project Structure:


## Migrations:

Before working on the deliverables, create a migration for all tables.

- A `Review` belongs to a `Restaurant`, and a `Review` also belongs to a `Customer`. In your migration, create any columns your `reviews` table will need to establish these relationships.

The `reviews` table should also have:

- A `star_rating` column that stores an integer.

## Deliverables:

### Object Relationship Methods

#### Review

- `Review customer()`: Should return the `Customer` instance for this review
- `Review restaurant()`: Should return the `Restaurant` instance for this review

#### Restaurant

- `Restaurant reviews()`: Returns a collection of all the reviews for the `Restaurant`
- `Restaurant customers()`: Returns a collection of all the customers who reviewed the `Restaurant`

#### Customer

- `Customer reviews()`: Should return a collection of all the reviews that the `Customer` has left
- `Customer restaurants()`: Should return a collection of all the restaurants that the `Customer` has reviewed

Check that these methods work before proceeding.

### Aggregate and Relationship Methods

#### Customer

- `Customer full_name()`: Returns the full name of the customer, with the first name and the last name concatenated, Western style.
- `Customer favorite_restaurant()`: Returns the restaurant instance that has the highest star rating from this customer
- `Customer add_review(restaurant, rating)`: Takes a `restaurant` (an instance of the `Restaurant` class) and a rating. Creates a new review for the restaurant with the given `restaurant_id`
- `Customer delete_reviews(restaurant)`: Takes a `restaurant` (an instance of the `Restaurant` class) and removes **all** their reviews for this restaurant

#### Review

- `Review full_review()`: Should return a string formatted as follows: Review for {insert restaurant name} by {insert customer's full name}: {insert review star_rating} stars.

#### Restaurant

- `Restaurant fanciest()`: This method should be a class method. Returns _one_ restaurant instance for the restaurant that has the highest price
- `Restaurant all_reviews()`: Should return a list of strings with all the reviews for this restaurant formatted as follows:

```python
[
    "Review for {insert restaurant name} by {insert customer's full name}: {insert review star_rating} stars.",
    "Review for {insert restaurant name} by {insert customer's full name}: {insert review star_rating} stars.",
]
