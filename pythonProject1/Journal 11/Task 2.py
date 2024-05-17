import pandas as pd
from sklearn.naive_bayes import CategoricalNB
from sklearn.preprocessing import LabelEncoder

# Load the dataset
df = pd.read_csv('Data.csv')

# Drop the 'test_date' column as it's not needed for prediction
df = df.drop('test_date', axis=1)

# Handle missing values in 'age_60_and_above'
df['age_60_and_above'] = df['age_60_and_above'].fillna('None')

# Encode categorical variables
le_cough = LabelEncoder()
le_fever = LabelEncoder()
le_sore_throat = LabelEncoder()
le_shortness_of_breath = LabelEncoder()
le_head_ache = LabelEncoder()
le_corona_result = LabelEncoder()
le_age_60_and_above = LabelEncoder()
le_gender = LabelEncoder()
le_test_indication = LabelEncoder()

df['cough'] = le_cough.fit_transform(df['cough'])
df['fever'] = le_fever.fit_transform(df['fever'])
df['sore_throat'] = le_sore_throat.fit_transform(df['sore_throat'])
df['shortness_of_breath'] = le_shortness_of_breath.fit_transform(df['shortness_of_breath'])
df['head_ache'] = le_head_ache.fit_transform(df['head_ache'])
df['corona_result'] = le_corona_result.fit_transform(df['corona_result'])
df['age_60_and_above'] = le_age_60_and_above.fit_transform(df['age_60_and_above'])
df['gender'] = le_gender.fit_transform(df['gender'])
df['test_indication'] = le_test_indication.fit_transform(df['test_indication'])

# Separate features and target variable
X = df.drop('corona_result', axis=1)
y = df['corona_result']

# Initialize and fit the Naïve Bayes model
model = CategoricalNB()
model.fit(X, y)

# Define a test instance (example)
test_instance = pd.DataFrame({
    'cough': [1],
    'fever': [0],
    'sore_throat': [0],
    'shortness_of_breath': [0],
    'head_ache': [0],
    'age_60_and_above': ['None'],
    'gender': ['female'],
    'test_indication': ['Other']
})

# Encode the test instance using the same encoders
test_instance['cough'] = le_cough.transform(test_instance['cough'])
test_instance['fever'] = le_fever.transform(test_instance['fever'])
test_instance['sore_throat'] = le_sore_throat.transform(test_instance['sore_throat'])
test_instance['shortness_of_breath'] = le_shortness_of_breath.transform(test_instance['shortness_of_breath'])
test_instance['head_ache'] = le_head_ache.transform(test_instance['head_ache'])
test_instance['age_60_and_above'] = le_age_60_and_above.transform(test_instance['age_60_and_above'])
test_instance['gender'] = le_gender.transform(test_instance['gender'])
test_instance['test_indication'] = le_test_indication.transform(test_instance['test_indication'])

# Predict the class label for the test instance
predicted_class = model.predict(test_instance)
predicted_class_label = le_corona_result.inverse_transform(predicted_class)

print(f"The predicted class label for the test instance is: {predicted_class_label[0]}")
