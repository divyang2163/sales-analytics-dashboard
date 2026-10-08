# 📊 Sales Analytics Dashboard

A sales analytics project built with Python, Pandas, MySQL, and Streamlit.

The dashboard analyzes sales performance, monthly revenue, product performance, customer activity, category trends, and regional revenue.

## 🚀 Features

- View total revenue
- View total orders
- Track units sold
- Calculate average order value
- Identify the top-selling product
- Analyze monthly revenue trends
- Compare revenue by category
- Compare revenue by region
- Analyze top products by revenue
- View top customers
- Explore the raw sales dataset

## 🛠️ Technologies Used

- Python
- Pandas
- MySQL
- SQL
- Streamlit
- Matplotlib
- MySQL Connector for Python

## 🗄️ Database

The project includes a MySQL database named:

```text
sales_dashboard
```

The database contains a `sales` table with order, customer, product, pricing, quantity, category, and region data.

The dashboard connects to the MySQL database locally and loads the sales records for analysis.

If the MySQL database is unavailable, the application can fall back to the included CSV dataset.

## 📁 Project Structure

```text
sales-analytics-dashboard/
│
├── app.py
├── database.sql
├── sales_data.csv
├── requirements.txt
└── README.md
```

### `app.py`
Runs the Streamlit dashboard and performs the sales analysis.

### `database.sql`
Creates the MySQL database, creates the sales table, and inserts sample sales records.

### `sales_data.csv`
Provides a CSV version of the sales dataset and acts as a fallback data source.

### `requirements.txt`
Contains the Python packages required to run the application.

## ▶️ How to Run

### 1. Install the required Python packages

```bash
python3 -m pip install -r requirements.txt
```

### 2. Create the MySQL database

Open `database.sql` in MySQL Workbench and run the script.

This will:

- Create the `sales_dashboard` database
- Create the `sales` table
- Insert the sample sales records

### 3. Set your MySQL password as an environment variable

On macOS:

```bash
export MYSQL_PASSWORD='YOUR_MYSQL_PASSWORD'
```

### 4. Start the dashboard

```bash
python3 -m streamlit run app.py
```

## 📈 Dashboard Metrics

The dashboard calculates:

```text
Total Revenue
Total Orders
Units Sold
Average Order Value
Top Product
Monthly Revenue
Revenue by Category
Revenue by Region
Top Products by Revenue
Top Customers
```

## 🧠 What I Learned

This project helped me strengthen my skills in:

- SQL database creation
- MySQL
- Python database connections
- Pandas data analysis
- Data aggregation
- Data visualization
- Streamlit dashboard development
- Working with multiple data sources

## 🔮 Future Improvements

- Add interactive filters
- Add date-range filtering
- Add product and region filters
- Add profit and margin analysis
- Add automated database updates
- Deploy the dashboard online
- Connect to a cloud-hosted database

## 👤 Author

**Divyang Parikh**