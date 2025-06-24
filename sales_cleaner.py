
import pandas as pd

# Load the data
df = pd.read_csv("Sales_April_2019.csv")

# Drop missing values
df.dropna(how='any', inplace=True)

# Convert columns
df['Quantity Ordered'] = pd.to_numeric(df['Quantity Ordered'], errors='coerce')
df['Price Each'] = pd.to_numeric(df['Price Each'], errors='coerce')
df['Order Date'] = pd.to_datetime(df['Order Date'], errors='coerce')

# Feature engineering
df['Month'] = df['Order Date'].dt.month
df['Sales'] = df['Quantity Ordered'] * df['Price Each']
df['City'] = df['Purchase Address'].apply(lambda x: x.split(',')[1].strip())

# Save cleaned data
df.to_csv("Clean_Sales_Data.csv", index=False)
