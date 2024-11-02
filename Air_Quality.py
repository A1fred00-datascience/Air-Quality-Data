#%% Importing Libraries
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_squared_error, r2_score
from sklearn.preprocessing import StandardScaler, LabelEncoder

#%% Step 1: Load the Dataset
# Adjust the file path if needed
data = pd.read_csv('/Users/alfredoserranofigueroa/Desktop/Github/Air_Quality_Data/epa_air_quality.csv')

# Display the first few rows of the dataset
print(data.head())

#%% Step 2: Data Exploration
# Summary of the dataset
print(data.info())
print(data.describe())

# Check for missing values
print("Missing values per column:\n", data.isnull().sum())

#%% Step 3: Data Preprocessing
# Handle missing values
# Fill missing values for numeric columns with the column mean
numeric_cols = data.select_dtypes(include=[np.number]).columns
data[numeric_cols] = data[numeric_cols].apply(lambda x: x.fillna(x.mean()), axis=0)

# Encoding categorical variables
label_encoders = {}
for col in data.select_dtypes(include=['object']).columns:
    le = LabelEncoder()
    data[col] = le.fit_transform(data[col].astype(str))  # Ensure all values are string type for encoding
    label_encoders[col] = le

# Scaling features
scaler = StandardScaler()
scaled_features = scaler.fit_transform(data[numeric_cols])
data_scaled = pd.DataFrame(scaled_features, columns=numeric_cols)

#%% Step 4: Feature Selection and Train-Test Split
# Define the target variable
target_column = 'aqi'  # Assuming 'aqi' is the target variable; adjust if necessary
X = data_scaled.drop(columns=[target_column])
y = data_scaled[target_column]

# Split data into training and testing sets
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)

#%% Step 5: Model Training
# Using a Random Forest Regressor as an example
model = RandomForestRegressor(n_estimators=100, random_state=42)
model.fit(X_train, y_train)

#%% Step 6: Model Evaluation
y_pred = model.predict(X_test)
mse = mean_squared_error(y_test, y_pred)
r2 = r2_score(y_test, y_pred)

print('Model Performance:')
print(f'Mean Squared Error: {mse:.4f}')
print(f'R-squared: {r2:.4f}')

#%% Step 7: Feature Importance
importances = model.feature_importances_
indices = np.argsort(importances)[-10:]  # Top 10 features

plt.figure(figsize=(12, 6))
plt.barh(range(len(indices)), importances[indices], align='center')
plt.yticks(range(len(indices)), [X.columns[i] for i in indices])
plt.xlabel('Feature Importance')
plt.title('Top 10 Feature Importances in RandomForest Model')
plt.show()

#%% Step 8: Visualizing Predictions
plt.figure(figsize=(10, 6))
plt.scatter(y_test, y_pred, alpha=0.5)
plt.xlabel("Actual Values")
plt.ylabel("Predicted Values")
plt.title("Actual vs Predicted Air Quality Index")
plt.show()

# Exporting analysis results to an Excel file
with pd.ExcelWriter('Air_Quality_Analysis_Results.xlsx') as writer:
    # Save basic summary statistics
    data.describe().to_excel(writer, sheet_name='Summary Statistics')
    
    # Save feature importance
    feature_importance = pd.DataFrame({
        'Feature': X.columns,
        'Importance': model.feature_importances_
    }).sort_values(by='Importance', ascending=False)
    feature_importance.to_excel(writer, sheet_name='Feature Importance', index=False)
    
    # Save model evaluation metrics
    model_metrics = pd.DataFrame({
        'Metric': ['Mean Squared Error', 'R-squared'],
        'Value': [mse, r2]
    })
    model_metrics.to_excel(writer, sheet_name='Model Evaluation', index=False)
    
    # Export Correlation Matrix
    correlation_matrix = data.corr()
    correlation_matrix.to_excel(writer, sheet_name='Correlation Matrix')

print("Analysis and model insights have been exported to 'Air_Quality_Analysis_Results.xlsx'")
