from Customer import Customer
from Review import Review
from Restaurant import Restaurant

def main():
    # Creating customers
    customer1 = Customer("Stevie", "Wanda")
    customer2 = Customer("Lisa ", "Monroe")

    # Creating restaurants
    restaurant1 = Restaurant("Chick fill ' A")
    restaurant2 = Restaurant("Smokin Beef")

    # Adding reviews
    customer1.add_review(restaurant1, 4)
    customer1.add_review(restaurant2, 5)
    customer2.add_review(restaurant1, 3)


    # Testing methods
  # Testing methods
    print("Customers:")
    for customer in Customer.all():
        print(customer.full_name())

    print("\nRestaurants:")
    for restaurant in Restaurant.all_restaurants:  # Use all_restaurants instead of all()
        print(restaurant.name())


    print("\nReviews for Restaurant A:")
    for review in restaurant1.reviews():
        print(f"Customer: {review.customer().full_name()}, Rating: {review.rating()}")

    print("\nCustomers who reviewed Restaurant A:")
    for customer in restaurant1.customers():
        print(customer.full_name())

    print("\nAverage rating for Restaurant A:", restaurant1.average_star_rating())

    print("\nNumber of reviews by Stevie Wanda:", customer1.num_reviews())

    found_customer = Customer.find_by_name("John Doe")
    if found_customer:
        print("\nFound customer by name:", found_customer.full_name())
    else:
        print("\nNo customer found by name.")

    customers_with_given_name = Customer.find_all_by_given_name("Jane")
    if customers_with_given_name:
        print("\nCustomers with given name 'Jane':")
        for customer in customers_with_given_name:
            print(customer.full_name())
    else:
        print("\nNo customers found with given name.")

if __name__ == "__main__":
    main()