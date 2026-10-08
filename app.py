import os

import matplotlib.pyplot as plt
import mysql.connector
import pandas as pd
import streamlit as st


st.set_page_config(
    page_title="Sales Analytics Dashboard",
    page_icon="📊",
    layout="wide"
)


# --------------------------------------------------
# LOAD DATA FROM MYSQL
# --------------------------------------------------

def load_mysql_data():
    connection = mysql.connector.connect(
        host="127.0.0.1",
        user="root",
        password=os.getenv("MYSQL_PASSWORD"),
        database="sales_dashboard"
    )

    query = """
        SELECT
            Order_ID,
            Order_Date,
            Customer,
            Category,
            Product,
            Quantity,
            Unit_Price,
            Region
        FROM sales
        ORDER BY Order_Date;
    """

    df = pd.read_sql(query, connection)

    connection.close()

    return df


# --------------------------------------------------
# LOAD DATA
# --------------------------------------------------

@st.cache_data
def load_data():
    """
    Try loading data from MySQL first.
    If MySQL is unavailable, use the CSV file instead.
    """

    try:
        data = load_mysql_data()
        source = "MySQL Database"

    except Exception:
        data = pd.read_csv("sales_data.csv")
        source = "CSV File"

    return data, source


df, data_source = load_data()


# --------------------------------------------------
# PREPARE DATA
# --------------------------------------------------

df["Order_Date"] = pd.to_datetime(df["Order_Date"])

df["Revenue"] = (
    df["Quantity"] *
    df["Unit_Price"]
)


# --------------------------------------------------
# HEADER
# --------------------------------------------------

st.title("📊 Sales Analytics Dashboard")

st.write(
    "Analyze sales performance, product trends, customer activity, "
    "and regional revenue using Python, Pandas, MySQL, and Streamlit."
)

st.caption(f"Data Source: {data_source}")

st.divider()


# --------------------------------------------------
# KPI METRICS
# --------------------------------------------------

total_revenue = df["Revenue"].sum()

total_orders = df["Order_ID"].nunique()

total_units = df["Quantity"].sum()

average_order_value = (
    total_revenue / total_orders
)


top_product = (
    df.groupby("Product")["Quantity"]
    .sum()
    .sort_values(ascending=False)
    .index[0]
)


col1, col2, col3, col4, col5 = st.columns(5)


with col1:
    st.metric(
        "Total Revenue",
        f"${total_revenue:,.2f}"
    )


with col2:
    st.metric(
        "Total Orders",
        total_orders
    )


with col3:
    st.metric(
        "Units Sold",
        total_units
    )


with col4:
    st.metric(
        "Avg. Order Value",
        f"${average_order_value:,.2f}"
    )


with col5:
    st.metric(
        "Top Product",
        top_product
    )


st.divider()


# --------------------------------------------------
# MONTHLY REVENUE
# --------------------------------------------------

st.subheader("📈 Monthly Revenue")


monthly_revenue = (
    df.groupby(
        df["Order_Date"].dt.to_period("M")
    )["Revenue"]
    .sum()
)


monthly_revenue.index = (
    monthly_revenue.index.astype(str)
)


fig, ax = plt.subplots(
    figsize=(10, 4)
)


ax.plot(
    monthly_revenue.index,
    monthly_revenue.values,
    marker="o"
)


ax.set_xlabel("Month")

ax.set_ylabel("Revenue ($)")

ax.set_title(
    "Monthly Sales Revenue"
)


plt.xticks(
    rotation=45
)


plt.tight_layout()


st.pyplot(
    fig,
    use_container_width=True
)


st.divider()


# --------------------------------------------------
# CATEGORY AND REGION ANALYSIS
# --------------------------------------------------

left_col, right_col = st.columns(2)


with left_col:

    st.subheader(
        "🛍️ Revenue by Category"
    )

    category_revenue = (
        df.groupby("Category")["Revenue"]
        .sum()
        .sort_values(
            ascending=False
        )
    )

    st.bar_chart(
        category_revenue
    )


with right_col:

    st.subheader(
        "🌎 Revenue by Region"
    )

    region_revenue = (
        df.groupby("Region")["Revenue"]
        .sum()
        .sort_values(
            ascending=False
        )
    )

    st.bar_chart(
        region_revenue
    )


st.divider()


# --------------------------------------------------
# PRODUCT ANALYSIS
# --------------------------------------------------

st.subheader(
    "🏆 Top Products by Revenue"
)


product_revenue = (
    df.groupby("Product")["Revenue"]
    .sum()
    .sort_values(
        ascending=False
    )
)


st.bar_chart(
    product_revenue
)


st.divider()


# --------------------------------------------------
# TOP CUSTOMERS
# --------------------------------------------------

st.subheader(
    "👥 Top Customers"
)


customer_revenue = (
    df.groupby("Customer")["Revenue"]
    .sum()
    .sort_values(
        ascending=False
    )
    .head(10)
)


customer_table = (
    customer_revenue.reset_index()
)


customer_table.columns = [
    "Customer",
    "Total Revenue"
]


customer_table[
    "Total Revenue"
] = customer_table[
    "Total Revenue"
].map(
    "${:,.2f}".format
)


st.dataframe(
    customer_table,
    use_container_width=True,
    hide_index=True
)


st.divider()


# --------------------------------------------------
# RAW DATA
# --------------------------------------------------

with st.expander(
    "View Sales Data"
):

    st.dataframe(
        df,
        use_container_width=True,
        hide_index=True
    )