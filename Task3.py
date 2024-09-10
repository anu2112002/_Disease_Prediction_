import pandas as pd
import numpy as np

# Define the number of patients and features
n_patients = 1000
n_features = 10

# Generate synthetic data
data = np.random.rand(n_patients, n_features)

# Create a pandas dataframe
df = pd.DataFrame(data, columns=[f'feature_{i}' for i in range(n_features)])

# Add a disease label column
df['disease'] = np.random.choice(['flu', 'pneumonia', 'cancer'], size=n_patients)

# Add some missing values
df.iloc[10:20, 2:5] = np.nan

# Create a categorical column for symptoms
symptoms = ['fever', 'headache', 'fatigue', 'cough']
df['symptoms'] = np.random.choice(symptoms, size=n_patients)

# Create a categorical column for medical history
medical_history = ['diabetes', 'hypertension', 'none']
df['medical_history'] = np.random.choice(medical_history, size=n_patients)

# Print the first few rows of the dataset
print(df.head())
