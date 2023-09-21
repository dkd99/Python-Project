import pandas as pd
from faker import Faker
import random
import csv

fake = Faker()

def generate_customer_data(num_records=500):
    data = []

    for _ in range(num_records):
        customer_id = fake.unique.random_number()
        visit_date = fake.date_between(start_date='-1y', end_date='today')
        total_spend = round(random.uniform(10, 500), 2)
        product_category = fake.random_element(elements=('Electronics', 'Clothing', 'Books', 'Toys'))

        # Ensure visit_date is a valid datetime
        visit_date = visit_date.strftime('%Y-%m-%d')  # Format the date as 'YYYY-MM-DD'

        data.append([customer_id, visit_date, total_spend, product_category])

    return data

def save_to_csv(data, filename):
    with open(filename, 'w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['CustomerID', 'VisitDate', 'TotalSpend', 'ProductCategory'])
        writer.writerows(data)

if __name__ == "__main__":
    generated_data = generate_customer_data()
    save_to_csv(generated_data, 'customer_data.csv')