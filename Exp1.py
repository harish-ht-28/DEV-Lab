import pandas as pd
import matplotlib.pyplot as plt
# Sample data (you can replace this with your own dataset)
data = {
'Name': ['John', 'Jane', 'Mike', 'Emily', 'Alex'],
'Age': [25, 30, 22, 28, 35],
'Score': [90, 85, 78, 95, 88]
}
# Create a DataFrame from the data
df = pd.DataFrame(data)
# Display the DataFrame
print("DataFrame:")
print(df)
# Data Analysis
print("\nData Analysis:")
print("Mean Age:", df['Age'].mean())
print("Maximum Score:", df['Score'].max())
print("Minimum Score:", df['Score'].min())
# Data Visualization
plt.figure(figsize=(8, 4))
plt.bar(df['Name'], df['Score'])
plt.xlabel('Name')
plt.ylabel('Score')
plt.title('Scores of Students')
plt.show()
