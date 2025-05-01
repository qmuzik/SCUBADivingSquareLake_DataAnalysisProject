# SCUBA Diving in Square Lake 2021 - 2024: Bottom Time by Quincy Muzik 4/28/2025
# Calculates the mean, variance, median, mode, and Sum (Minutes & Hours) of the bottom time occured while SCUBA diving in Square Lake
# Data recorded on Mares Puck Pro Dive Computer

import pandas as pd
import matplotlib.pyplot as plt

# Load the CSV File with custom parameters
dfScubaData = pd.read_csv(r'J:\Statistical Analysis\Diving in Sqaure Lake\Data\Dive Log.csv')

# Inspect the dataframe (optional/used for testing)
#print(dfScubaData.head())

# Calculate the Mean, Variance, Median, Mode, and Sum of the Bottom Time
columnToCalculate = 'Bottom Time:'
meanValue = dfScubaData[columnToCalculate].mean()
varianceValue = dfScubaData[columnToCalculate].var()
medianValue = dfScubaData[columnToCalculate].median()
modeValue = dfScubaData[columnToCalculate].mode()
sumValue = dfScubaData[columnToCalculate].sum()

# Print out the Mean, Variance, Median, Mode, and Sum (Minutes & Hours) of the Bottom Time
print("Mean:\n", meanValue)
print("Variance:\n", varianceValue)
print("Median:\n", medianValue)
print("Mode:\n", modeValue)
print("Sum (Minutes):\n", sumValue)
print("Sum (Hours):\n", sumValue / 60)

# Plot the data for Dive
plt.plot(dfScubaData[columnToCalculate],label='Quincys Bottom Time')
plt.legend()

# Create the Layout of the Graph
plt.title('SCUBA Diving in Square Lake September 2021 - September 2024: Bottom Time')
plt.xlabel('Dive Number')
plt.ylabel('Time in Minutes')
plt.grid()

# Show the Graph
plt.show() 
