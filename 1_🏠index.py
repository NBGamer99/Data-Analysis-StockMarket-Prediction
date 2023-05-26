import streamlit as st
import os

st.set_page_config(
	page_title="Index",
	page_icon="🏠",
	layout="centered",
	initial_sidebar_state="expanded",
	menu_items={
		# 'Get Help': 'no help',
		# 'Report a bug': "we don't have bugs what do you mean ? 🐛",
		'About': """
				# Best Team Ever
				![](https://i.ibb.co/fCsNPvm/photooo.gif)
		"""
	}
)

os.chdir(os.path.dirname(os.path.realpath(__file__)))


st.title("Stock Market Analysis Project")

url = 'https://www.youtube.com/embed/p7HKvqRI_Bo'
st.video(url)

st.subheader("Abstraction:")
tab1, tab2 = st.tabs(["Abstraction", "Schematic"])
tab1.write(r"""Data analytics is the process of examining large and complex data sets to uncover hidden patterns, insights, and trends that can inform business decisions. It involves using statistical and computational techniques to identify meaningful patterns and relationships within the data, and then using this information to guide strategic decision-making.""")
tab1.write(r"""Data analytics can be used in a wide range of fields, from finance and marketing to healthcare and social sciences. It can involve the analysis of structured data, such as that found in databases and spreadsheets, as well as unstructured data, such as text and images.""")
tab2.image('./assets/schema.png')
st.markdown("---")
st.subheader("Stock Market:")
st.write(r"""The stock market is a public marketplace where publicly traded companies list their stocks for purchase and sale by individual and institutional investors. It provides a means for companies to raise capital by selling ownership stakes in the company to investors.""")
st.write(r"""Investors buy and sell stocks in the stock market with the goal of generating a return on their investment. They can make money by buying a stock at a low price and selling it at a higher price, or by receiving dividends, which are payments made by companies to their shareholders.""")
st.write("VHere are some commonly used keywords in the context of the stock market: ")
st.markdown("- ***Open***: Refers to the opening price of a stock, which is the price at which the first trade is executed when the market opens for trading.")
st.markdown("- ***Close***: refers to the closing price of a stock, which is the final price at which a stock is traded when the market closes for the day.")
st.markdown("- ***High***: refers to the highest price at which a stock was traded during a particular trading session (Day).")
st.markdown("- ***Low***: refers to the lowest price at which a stock was traded during a particular trading session (Day).")
st.markdown("- ***Volume***: Refers to the total number of shares or contracts that were traded during a particular trading session or over a given period of time. ")

st.subheader("Data Set")
st.image('./assets/dataset.png')
st.markdown("---")

st.subheader("ETL :")
st.write("ETL – Extraction, Transformation and Loading, is a trilogy of processes that collects varied source data from heterogeneous databases and transforms them into disparate data warehouses.")
st.markdown("### Extract :")
st.markdown("""
    - Reads data from multiple data sources and extracts required set of data
    - Recovers necessary data with optimum usage of resources
    - Should not disturb data sources, performance and functioning
""")
st.markdown("### Transform :")
st.markdown("""
    - Filtration, cleansing and preparation of data extracted, with lookup tables
    - Authentication of records, refutation and integration of data
    - Data to be sorted, filtered, cleared, standardized, translated or verified for consistency
""")
st.markdown("### Load :")
st.markdown("""
    - Writing data output, after extraction and transformation to a data warehouse
    - Either physical insertion of record as a new row in database table or link processes for each record from the main source
""")
st.image('./assets/ETL.png')
st.markdown("---")