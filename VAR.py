import pandas as pd
import os

SYMBOLS = {
    "Apple" : "AAPL",
    "Adobe" : "ADBE",
    "Amazon" : "AMZN",
    "Google" : "GOOGL",
    "Ibm" : "IBM",
    "Intel" : "INTC",
    "Meta" : "META",
    "Microsoft" : "MSFT",
    "NVidia" : "NVDA",
    "Oracle" : "ORCL",
    }

def check_file_exists(file_path):
	return os.path.exists(file_path)

df = pd.read_csv("Data/AAPL.csv")

# print(df.info())

# print(check_file_exists("./keras_model.h"))