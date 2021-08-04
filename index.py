#   imports
import csv, pandas as pd, statistics, math

#   code
framed_data = pd.read_csv(r"C:\Swarup\WhiteHat Jr\Python\Projects\StandardDeviation\data.csv")
framed_data_simplified = framed_data["Data"]
data_mean = statistics.mean(framed_data_simplified)
squared_values_addition = 0
squared_values_lsit = []

for items in framed_data_simplified:
    subtracted_values = items - data_mean
    squared_values = subtracted_values * subtracted_values
    squared_values_lsit.append(items)

for items in squared_values_lsit:
    squared_values_addition = squared_values_addition + items

variance = squared_values_addition/len(squared_values_lsit)
standard_deviation = math.sqrt(variance)
print("-------------------------------------------\n", "Standard Deviation is ", standard_deviation, "\n-------------------------------------------")
