import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestClassifier
import pickle

# Example dataset
data = {
    'user_id': [1, 2, 3, 4, 5, 6, 7, 8, 9, 10],
    'job': ['admin.', 'blue-collar', 'entrepreneur', 'housemaid', 'management', 'retired', 'self-employed', 'services', 'student', 'technician'],
    'marital': ['married', 'single', 'married', 'single', 'married', 'single', 'married', 'single', 'married', 'single'],
    'education': ['tertiary', 'secondary', 'tertiary', 'primary', 'tertiary', 'secondary', 'tertiary', 'primary', 'tertiary', 'secondary'],
    'default': ['no', 'yes', 'no', 'yes', 'no', 'yes', 'no', 'yes', 'no', 'yes'],
    'housing': ['yes', 'no', 'yes', 'no', 'yes', 'no', 'yes', 'no', 'yes', 'no'],
    'loan': ['no', 'yes', 'no', 'yes', 'no', 'yes', 'no', 'yes', 'no', 'yes'],
    'contact': ['cellular', 'telephone', 'cellular', 'telephone', 'cellular', 'telephone', 'cellular', 'telephone', 'cellular', 'telephone'],
    'month': ['jan', 'feb', 'mar', 'apr', 'may', 'jun', 'jul', 'aug', 'sep', 'oct'],
    'day_of_week': ['mon', 'tue', 'wed', 'thu', 'fri', 'mon', 'tue', 'wed', 'thu', 'fri'],
    'duration': [100, 200, 150, 300, 250, 400, 120, 350, 260, 130],
    'campaign': [1, 2, 1, 2, 1, 2, 1, 2, 1, 2],
    'pdays': [999, 6, 999, 6, 999, 6, 999, 6, 999, 6],
    'previous': [0, 1, 0, 1, 0, 1, 0, 1, 0, 1],
    'poutcome': ['nonexistent', 'failure', 'nonexistent', 'failure', 'nonexistent', 'failure', 'nonexistent', 'failure', 'nonexistent', 'failure'],
    'amount': [100, 2000, 150, 3000, 250, 4000, 120, 3500, 260, 130],
    'is_fraud': [0, 1, 0, 1, 0, 1, 0, 1, 0, 0]
}

df = pd.DataFrame(data)

# Convert categorical features to numeric
df = pd.get_dummies(df, columns=['job', 'marital', 'education', 'default', 'housing', 'loan', 'contact', 'month', 'day_of_week', 'poutcome'])

X = df.drop(['is_fraud'], axis=1)
y = df['is_fraud']

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

model = RandomForestClassifier()
model.fit(X_train, y_train)

# Save the model to a file
with open('fraud_detection_model.pkl', 'wb') as file:
    pickle.dump(model, file)
