class Restaurant:

    _all_restaurants = []

    def __init__(self, name ) :
        self.name = name 
        #self._reviews = []
        Restaurant._all_restaurants.append(self)

    def name(self):
        return self._name

    @classmethod
    def all(cls):
        return cls._all_restaurants

    def add_review(self, review):
        self._reviews.append(review)

    def reviews(self):
        return self._reviews

    def customers(self):
        unique_customers = set()
        for review in self._reviews:
            unique_customers.add(review.customer())
        return list(unique_customers)

    def average_star_rating(self):
        if not self._reviews:
            return 0
        total_ratings = sum(review.rating() for review in self._reviews)
        return total_ratings / len(self._reviews)