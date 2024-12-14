# Air Quality Prediction Project

This project leverages machine learning to predict Air Quality Index (AQI) values based on air quality measurements, using data from various regions in the United States. The objective is to develop a model capable of accurately forecasting AQI levels, allowing for insights into environmental and pollution patterns.

---

## Table of Contents

- [Project Overview](#project-overview)
- [Dataset](#dataset)
- [Project Structure](#project-structure)
- [Installation and Setup](#installation-and-setup)
- [Data Preprocessing](#data-preprocessing)
- [Exploratory Data Analysis](#exploratory-data-analysis)
- [Model Training and Evaluation](#model-training-and-evaluation)
- [Results and Analysis](#results-and-analysis)
- [Future Work](#future-work)
- [References](#references)

---

## Project Overview

Air quality plays a crucial role in public health and environmental monitoring. This project aims to predict AQI levels using historical air quality data, enabling proactive measures for air pollution management. The primary focus is on data preprocessing, feature engineering, and model training with a Random Forest Regressor to achieve accurate AQI predictions.

---

## Dataset

The dataset used in this project contains the following key columns:

- `date_local`: Date of measurement
- `state_name`, `county_name`, `city_name`: Location identifiers
- `parameter_name`: The pollutant type (e.g., Carbon monoxide)
- `units_of_measure`: Measurement units
- `arithmetic_mean`: Average concentration of the pollutant
- `aqi`: Air Quality Index, which is the target variable for prediction

---

# Data Preprocessing

## The preprocessing steps involved:
- Handling Missing Values: Missing values in numerical columns were replaced by the mean, while categorical missing values were filled with the mode.
- Encoding Categorical Variables: Converted categorical columns (e.g., state_name, county_name) to numerical values using label encoding.
- Scaling Features: Standardized numerical features to improve model performance and convergence.

# Exploratory Data Analysis
- Summary Statistics: Analyzed distributions, mean, median, and other statistical insights.
- Correlation Analysis: Visualized correlations between features to identify significant predictors for AQI.
- Feature Distributions: Plotted key features to inspect distributions and identify patterns.

# Model Training and Evaluation
A Random Forest Regressor was chosen as the model for AQI prediction. Here are the main steps taken:

- Train-Test Split: The dataset was split into training and testing sets.
- Model Training: A Random Forest model was trained on the training data.
- Evaluation: Model performance was evaluated using:
-- Mean Squared Error (MSE)
-- R-squared (R²)

# Model Performance
The model achieved the following results:

- Mean Squared Error (MSE): 0.0586
- R-squared (R²): 0.9541

# Results and Analysis
The model demonstrated high predictive accuracy, indicating that pollutant concentrations (arithmetic_mean) are strong predictors of AQI. Feature importance analysis identified the most influential factors, and the correlation matrix offered insights into feature relationships.

# Exporting Results
Results were saved in an Excel file (Air_Quality_Analysis_Results.xlsx) with the following sheets:

- Summary Statistics: Descriptive statistics for the dataset.
- Feature Importance: Top contributing features for the model’s AQI predictions.
- Model Evaluation: MSE and R² scores for model assessment.
- Correlation Matrix: Correlation values between features.

# Future Work
Potential improvements and expansions for the project include:
- Hyperparameter Tuning: Experimenting with different hyperparameters to improve model accuracy.
- Alternative Models: Testing models like Gradient Boosting, XGBoost, and Neural Networks for potentially better performance.
- Geographical Analysis: Incorporating geographic clustering to identify pollution trends across regions.
- Temporal Analysis: Analyzing seasonal and temporal trends in AQI changes.
