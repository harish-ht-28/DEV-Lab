import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# Sample data (you can replace this with your own dataset)
data = {
    'sender': ['alice@example.com', 'bob@example.com', 'alice@example.com'],
    'receiver': ['bob@example.com', 'alice@example.com', 'carol@example.com'],
    'subject': ['Hello', 'Meeting Reminder', 'Project Update'],
    'timestamp': ['2023-08-01 10:00:00', '2023-08-02 14:30:00', '2023-08-03 09:15:00'],
    'content': ['Hi Bob,\n\nHow are you?', 'Hi Alice,\n\nDon\'t forget the meeting at 3 PM.',
                'HiCarol,\n\nHere\'s the latest project update.']
}

# Create a DataFrame from the data
df = pd.DataFrame(data)

# Convert timestamp to datetime objects
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Save the DataFrame to a CSV file
df.to_csv('emails.csv', index=False)

print("""CSV file created
successfully.""")

# Load the data from the CSV file
df = pd.read_csv("emails.csv")

# Convert timestamp to datetime objects after loading from CSV because
# reading from CSV might convert it back to string
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Display DataFrame information
print(df.info())

# PERFORM EXPLORATORY DATA ANALYSIS (EDA)

# Drop rows with missing values
df.dropna(inplace=True)

# Calculate email length
df['email_length'] = df['content'].apply(len)

# Data Visualization: Distribution of Email Lengths
plt.figure(figsize=(10, 6))
sns.histplot(data=df, x='email_length', bins=30, kde=True)
plt.xlabel('Email Length')
plt.ylabel('Count')
plt.title('Distribution of Email Lengths')
plt.show()

# Data Visualization: Top 10 Email Senders
top_senders = df['sender'].value_counts()[:10]
plt.figure(figsize=(12, 6))
sns.barplot(x=top_senders.index, y=top_senders.values)
plt.xticks(rotation=45)
plt.xlabel('Sender')
plt.ylabel('Number of Emails')
plt.title('Top 10 Email Senders')
plt.tight_layout()
plt.show()

# Data Visualization: Top 10 Email Receivers (Added this visualization)
top_receivers = df['receiver'].value_counts()[:10]
plt.figure(figsize=(12, 6))
sns.barplot(x=top_receivers.index, y=top_receivers.values)
plt.xticks(rotation=45)
plt.xlabel('Receiver')
plt.ylabel('Number of Emails')
plt.title('Top 10 Email Receivers')
plt.tight_layout()
plt.show()


# Data Visualization: Email Activity Over Time
df['year_month'] = df['timestamp'].dt.strftime('%Y-%m').astype('period[M]')
email_activity = df.groupby('year_month').size()
plt.figure(figsize=(12, 6))
email_activity.plot(kind='line')
plt.xlabel('Year-Month')
plt.ylabel('Number of Emails')
plt.title('Email Activity Over Time')
plt.xticks(rotation=45)
plt.tight_layout()
plt.show()
