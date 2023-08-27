class Review:
    _all_reviews = []
    
    def __init__(self, customer, restaurant, rating):
        self._customer = customer
        self._restaurant = restaurant
        self._rating = rating
        Review._all_reviews.append(self)

    def rating(self):
        return self._rating

    @classmethod
    def all(cls):
        return cls._all_reviews

    def customer(self):
        return self._customer

    def restaurant(self):
        return self._restaurant

    @classmethod
    def find_by_name(cls, name):
        for review in cls._all_reviews:
            if review.customer().full_name() == name:
                return review

    @classmethod
    def find_all_by_given_name(cls, given_name):
        matching_reviews = []
        for review in cls._all_reviews:
            if review.customer().given_name() == given_name:
                matching_reviews.append(review)
        return matching_reviews

    def num_reviews(self):
        count = 0
        for review in Review._all_reviews:
            if review.customer() == self._customer:
                count += 1
        return count
