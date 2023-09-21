import pandas as pd
import streamlit as st
import matplotlib.pyplot as plt
import seaborn as sns
import random
import csv
from faker import Faker
import os

fake = Faker()

# Check if the customer_data.csv file exists
if not os.path.exists("customer_data.csv"):
    st.info("The 'customer_data.csv' file does not exist. Please upload a CSV file.")
    uploaded_file = st.file_uploader("Upload a CSV file", type=["csv"])

    if uploaded_file is not None:
        # Read the uploaded CSV file
        data = pd.read_csv(uploaded_file)
    else:
        # Handle the case when no file is uploaded
        st.warning("No CSV file uploaded. Please upload a CSV file to proceed.")
        st.stop()  # Stop execution if no file is uploaded

else:
    # Read the existing customer_data.csv file
    data = pd.read_csv("customer_data.csv")

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

def main():
    st.title("Online Store Marketing Analysis")
    st.header("Key Performance Indicators (KPIs)")

    STYLE = """
    <style>
    img {
        max-width: 100%;
    }
    </style>
    """
    st.info(__doc__)
    st.markdown(STYLE, unsafe_allow_html=True)

    # Generate customer data and save to CSV
    if not os.path.exists("customer_data.csv"):
        generated_data = generate_customer_data()
        save_to_csv(generated_data, 'customer_data.csv')

    # Check if the "VisitDate" column is not null
    if "VisitDate" not in data.columns or data["VisitDate"].isnull().any():
        st.error("The 'VisitDate' column is missing or contains null values. Please check your data.")
        return

    # Calculate KPIs
    average_spending = data["TotalSpend"].mean()
    most_popular_category = data["ProductCategory"].mode().values[0]

    # Calculate Monthly Revenue Growth
    monthly_revenue = data.groupby(data["VisitDate"].str.slice(0, 7)).agg({"TotalSpend": "sum"})
    monthly_growth = monthly_revenue["TotalSpend"].pct_change()

    # Display KPIs
    st.write("Average Spending per Customer:", round(average_spending, 2))
    st.write("Most Popular Product Category:", most_popular_category)
    st.write("Monthly Revenue Growth:")
    st.write(monthly_growth)  # Display Monthly Revenue Growth as a table

    # Use Streamlit to display the line chart for Monthly Revenue Growth
    st.set_option('deprecation.showPyplotGlobalUse', False)

    st.subheader("Monthly Revenue Growth")
    st.line_chart(monthly_revenue)
    st.subheader("Monthly Growth Rate")
    st.line_chart(monthly_growth)

    # Calculate dynamic Marketing Optimization Suggestions based on KPIs
    suggestions = []

    if average_spending > 200:
        suggestions.append("Customers are spending more than average. Consider offering loyalty rewards.")
    else:
        suggestions.append("Average spending is in line with expectations. Monitor customer behavior for changes.")

    if most_popular_category == "Electronics":
        suggestions.append("Electronics products are very popular. Consider expanding the Electronics category.")
    else:
        suggestions.append(f"The most popular category is {most_popular_category}. Consider promoting related products.")

    # Marketing Optimization Suggestions
    st.header("Marketing Optimization Suggestions")
    for suggestion in suggestions:
        st.markdown(f"- {suggestion}")

    # Additional Graphs
    st.header("Additional Graphs")

    # Scatter Plot
    st.subheader("Scatter Plot of Total Spend vs. VisitDate")
    plt.figure()
    sns.scatterplot(x="VisitDate", y="TotalSpend", data=data)
    plt.xticks(rotation=45)
    st.pyplot()

    # Box Plot
    st.subheader("Box Plot of Total Spend")
    plt.figure()
    sns.boxplot(x="ProductCategory", y="TotalSpend", data=data)
    plt.xticks(rotation=45)
    st.pyplot()

    # Pair Plot
    st.subheader("Pair Plot of Numeric Columns")
    sns.pairplot(data, hue="ProductCategory")
    st.pyplot()

    # Countplot for ProductCategory
    st.subheader("Countplot of Product Categories")
    plt.figure()
    sns.countplot(x="ProductCategory", data=data)
    plt.xticks(rotation=45)
    st.pyplot()

    # Calculate top 5 users based on spending
    top_5_users = data.groupby("CustomerID")["TotalSpend"].sum().nlargest(5).reset_index()

    # Display top 5 users
    st.subheader("Top 5 Users Based on Spending")
    st.write(top_5_users)

    # Calculate top 10 customers based on average spending per customer
    top_10_avg_spending = data.groupby("CustomerID")["TotalSpend"].mean().nlargest(10).reset_index()

    # Display top 10 customers based on average spending per customer
    st.subheader("Top 10 Customers Based on Average Spending per Customer")
    st.write(top_10_avg_spending)

    # Calculate total revenue per category
    total_revenue_per_category = data.groupby("ProductCategory")["TotalSpend"].sum().reset_index()

    # Plot a pie chart for percentage distribution of total revenue per category
    st.subheader("Percentage Distribution of Total Revenue per Category")
    plt.figure()
    plt.pie(total_revenue_per_category["TotalSpend"], labels=total_revenue_per_category["ProductCategory"],
            autopct='%1.1f%%', startangle=140)
    plt.axis('equal')  # Equal aspect ratio ensures that pie is drawn as a circle.
    st.pyplot()

if __name__ == "__main__":
    main()