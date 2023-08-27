class Review:
    #def __init__(self, rating, all ) :
    #    self.rating = rating
    #    self.all = all

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
        for customer in cls._all_customers:
            if customer.full_name() == name:
                return customer

    @classmethod
    def find_all_by_given_name(cls, given_name):
        matching_customers = []
        for customer in cls._all_customers:
            if customer.given_name() == given_name:
                matching_customers.append(customer)
        return matching_customers

    def num_reviews(self):
        return len(self._reviews)