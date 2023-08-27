class Restaurant:
    all_restaurants = []

    def __init__(self, name):
        self.name_ = name
        self.reviews_ = []
        Restaurant.all_restaurants.append(self)

    def name(self):
        return self.name_

    def add_review(self, review):
        self.reviews_.append(review)

    def reviews(self):
        return self.reviews_

    def customers(self):
        return list(set([review.customer() for review in self.reviews_]))

    def average_star_rating(self):
        if self.reviews_:
            total_rating = sum([review.rating() for review in self.reviews_])
            return total_rating / len(self.reviews_)
        else:
            return 0.0
