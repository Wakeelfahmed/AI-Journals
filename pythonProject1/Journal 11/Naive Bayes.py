import pandas as pd
from sklearn.naive_bayes import CategoricalNB
from sklearn.preprocessing import LabelEncoder

# Define the dataset
data = {
    'Age': ['<=30', '<=30', '31...40', '>40', '>40', '>40', '31...40', '<=30', '<=30', '>40', '<=30', '31...40', '31...40', '>40'],
    'Income': ['high', 'high', 'high', 'medium', 'low', 'low', 'low', 'medium', 'low', 'medium', 'medium', 'medium', 'high', 'medium'],
    'Student': ['no', 'no', 'no', 'no', 'yes', 'yes', 'yes', 'no', 'yes', 'yes', 'no', 'no', 'yes', 'no'],
    'Credit_rating': ['fair', 'excellent', 'fair', 'fair', 'fair', 'excellent', 'excellent', 'fair', 'fair', 'fair', 'excellent', 'fair', 'fair', 'excellent'],
    'Buys': ['no', 'no', 'yes', 'yes', 'yes', 'no', 'yes', 'no', 'yes', 'yes', 'yes', 'yes', 'yes', 'no']
}

# Convert the data into a DataFrame
df = pd.DataFrame(data)

# Separate the features and the target variable
X = df.drop('Buys', axis=1)
y = df['Buys']

# Encode the categorical variables for features
le_age = LabelEncoder()
le_income = LabelEncoder()
le_student = LabelEncoder()
le_credit_rating = LabelEncoder()

X['Age'] = le_age.fit_transform(X['Age'])
X['Income'] = le_income.fit_transform(X['Income'])
X['Student'] = le_student.fit_transform(X['Student'])
X['Credit_rating'] = le_credit_rating.fit_transform(X['Credit_rating'])

# Encode the target variable
le_buys = LabelEncoder()
y_encoded = le_buys.fit_transform(y)

# Initialize and fit the Naïve Bayes model
model = CategoricalNB()
model.fit(X, y_encoded)

# Define the test instance
test_instance = pd.DataFrame({
    'Age': ['<=30'],
    'Income': ['medium'],
    'Student': ['yes'],
    'Credit_rating': ['fair']
})

# Encode the test instance using the same encoders
test_instance['Age'] = le_age.transform(test_instance['Age'])
test_instance['Income'] = le_income.transform(test_instance['Income'])
test_instance['Student'] = le_student.transform(test_instance['Student'])
test_instance['Credit_rating'] = le_credit_rating.transform(test_instance['Credit_rating'])

# Predict the class label for the test instance
predicted_class = model.predict(test_instance)
predicted_class_label = le_buys.inverse_transform(predicted_class)

print(f"The predicted class label for the test instance is: {predicted_class_label[0]}")
