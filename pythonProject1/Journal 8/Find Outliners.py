import pandas as pd
import matplotlib.pyplot as plt

# Function to remove outliers using IQR
def remove_outliers(df, column):
    Q1 = df[column].quantile(0.25)
    Q3 = df[column].quantile(0.75)
    IQR = Q3 - Q1
    lower_bound = Q1 - 1.5 * IQR
    upper_bound = Q3 + 1.5 * IQR
    outliers_removed = df[(df[column] >= lower_bound) & (df[column] <= upper_bound)]
    outliers_count = len(df) - len(outliers_removed)
    print(f"Number of outliers removed in '{column}': {outliers_count}")
    return outliers_removed

# Function to plot boxplots
def plot_boxplots(df, columns):
    plt.figure(figsize=(10, 6))
    for col in columns:
        plt.boxplot(df[col], labels=[col])
        plt.title(f'Boxplot of {col}')
        plt.show()

# Load the data
data = pd.read_csv("OnlineRetail.csv", encoding='latin1')

# Visualize outliers in the original data
plot_boxplots(data, ['Quantity', 'UnitPrice'])

# Remove outliers from 'Quantity' and 'UnitPrice'
cleaned_data = remove_outliers(data, 'Quantity')
cleaned_data = remove_outliers(cleaned_data, 'UnitPrice')

# Visualize cleaned data
plot_boxplots(cleaned_data, ['Quantity', 'UnitPrice'])

# Display summary of cleaned data
print("\nSummary statistics of cleaned data:")
print(cleaned_data.describe())
