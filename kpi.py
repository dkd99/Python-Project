import pandas as pd

# Load the customer data from the CSV file
customer_data = pd.read_csv("customer_data.csv")
customer_data['VisitDate'] = pd.to_datetime(customer_data['VisitDate'])

print(customer_data.info())

# Calculate Average Spending per Customer
average_spending = customer_data["TotalSpend"].mean()

# Find the Most Popular Product Category
most_popular_category = customer_data["ProductCategory"].mode().values[0]

# Calculate Monthly Revenue Growth
customer_data["VisitDate"] = pd.to_datetime(customer_data["VisitDate"])
customer_data.set_index("VisitDate", inplace=True)
monthly_revenue = customer_data.resample("M")["TotalSpend"].sum()
monthly_growth = monthly_revenue.pct_change()

# Marketing Optimization Suggestions
# You can add your marketing optimization suggestions based on the KPIs here.

# Display the KPIs and Suggestions
print("Key Performance Indicators (KPIs):")
print("Average Spending per Customer:", round(average_spending, 2))
print("Most Popular Product Category:", most_popular_category)
print("Monthly Revenue Growth:")
print(monthly_growth)