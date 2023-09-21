# project

>>complete.py -- Generates Data and provides a streamlit dashboard.
>>final.py- Takes csv as input from user and then provides a streamlit dashboard.
>>main.py--contains script for generating data and saves the csv file in the folder with name customer_data.csv.
>>read_uploadcsv.py presents report based on the output csv file of main.py. If customer_data.csv(which is output of main.py) is not present it takes input from user. 
>>kpi.py--uses the saved csv file to present some kpi's.

# Online Store Marketing Analysis
This Python application analyzes data from an online store to derive key performance indicators (KPIs) and provide marketing optimization suggestions. The application is built using Streamlit.
# How to Run the Application

# Installation
1. Clone the repository to your local machine or download the code as a ZIP file and extract it.
2. Open a terminal or command prompt and navigate to the project directory.
3. Create a virtual environment.
python -m venv myenv
4. Activate the venv
.\myenv\Scripts\activate
5. Install the required dependencies using pip:
pip install -r requirements.txt
# Running the Application:
1.Run the Streamlit application
# streamlit run final.py
2. A new browser window or tab should open, displaying the Streamlit web application. You will be prompted to upload a CSV file containing your online store data.

# Once you have uploaded the CSV file, the application will perform the following tasks:

a. Check for missing or null values in the "VisitDate" column. If any are found, it will drop the corresponding rows with missing dates.

b. Calculate and display various key performance indicators (KPIs) based on the data, including average spending per customer, the most popular product category, and monthly revenue growth.

c. Provide dynamic marketing optimization suggestions based on the calculated KPIs.

d. Display additional data visualizations, including line charts, scatter plots, box plots, pair plots, and count plots, to help you explore the dataset.

e. Calculate and display the top 5 users based on spending and the top 10 customers based on average spending per customer.

f. Calculate the total revenue per product category and present the percentage distribution of total revenue per category in a pie chart.

# Note: 
a. The application uses Python libraries such as Pandas, Matplotlib, Seaborn, and Streamlit to perform data analysis and visualization.

b. Make sure to provide a CSV file with appropriate columns for customer data, including "CustomerID," "VisitDate," "TotalSpend," and "ProductCategory."

![image](https://github.com/dkd99/Python-Project/assets/103329032/ed1c94bd-b549-4445-95cb-7b28398934fb)


![image](https://github.com/dkd99/Python-Project/assets/103329032/8489d3e4-99e4-42aa-a6e6-bacfb7b8495d)

![image](https://github.com/dkd99/Python-Project/assets/103329032/0290ad05-acc7-4784-807e-1f6ec439999d)

![image](https://github.com/dkd99/Python-Project/assets/103329032/7a40e896-d939-4c0c-87ef-0a9e5edbe3c5)



