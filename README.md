# Cardiovascular-disease-detection-model
This dataset contains health records of individuals, providing key attributes essential for analyzing cardiovascular disease (CVD) risk and related health conditions. The dataset allows for exploratory data analysis (EDA) to uncover patterns, trends, and potential risk factors associated with CVD. Additionally, feature engineering will be applied to derive new insights and improve predictive modeling.

This data set was sourced from kaggle, Cardiovascular Disease dataset by Svetlana Ulianova

### Objective
The primary objective of this analysis is to build a classification model that predicts the presence or absence of cardiovascular disease. This involves:

- Performing exploratory data analysis (EDA) to understand feature distributions and relationships.
- Engineering new features such as BMI, pulse pressure, and blood pressure categories.
- Training and optimizing machine learning models to achieve high predictive accuracy.
  
### Dataset Features
**Demographics:**
- **Age:** Age of the individual (in years).
- **Gender:** Gender of the individual (Female, Male).
  
**Anthropometric Data:**
- **Height (cm):** Height of the individual.
- **Weight (kg):** Weight of the individual.
  
**Blood Pressure:**
- **Systolic Blood Pressure (ap_hi):** Upper value during a heartbeat.
- **Diastolic Blood Pressure (ap_lo):** Lower value between heartbeats.

**Health Indicators:**
- **Cholesterol:** Cholesterol levels categorized.
- **Glucose:** Blood glucose levels categorized.
- **Smoking:** Binary indicator for smoking status.
- **Alcohol Use:** Binary indicator for alcohol consumption.
- **Physical Activity:** Binary indicator for physical activity.

**Target Variable:**
- **Cardiovascular Disease:** Indicates the presence (1) or absence (0) of cardiovascular disease.
  
### Next Steps
- **Data Cleaning:** Handle missing values, outliers, and inconsistencies.
- **Feature Engineering:** Generate new features such as BMI, pulse pressure, and blood pressure categories.
- **Data Visualization:** Explore feature distributions and relationships with visualizations.
- **Model Training & Evaluation:** Train classification models, optimize hyperparameters, and evaluate performance.

### Summary
In this analysis, I explored a cardiovascular disease dataset, applying data preprocessing, feature engineering, and machine learning to predict the likelihood of cardiovascular disease.

#### Key steps included:

- **Data Cleaning:** Removed extreme and unattainable values while retaining medically plausible outliers.
- **Feature Engineering:** Derived new features such as BMI, pulse pressure, and blood pressure categories to enhance predictive power.
- **Exploratory Data Analysis (EDA):** Investigated feature distributions, correlations, and their impact on cardiovascular disease.
- **Model Training & Evaluation:** Tested multiple classification models, with Gradient Boosting Classifier performing the best.
**Hyperparameter Tuning:** Optimized model performance using GridSearchCV, improving precision and overall accuracy.
  
#### The final model achieved:

**Accuracy: 72.81%**
**Precision: 77.96%**
**Recall: 72.67%**
**F1-Score: 72.47%**

This project demonstrated the effectiveness of feature engineering and hyperparameter tuning in improving cardiovascular disease prediction. Future work could involve incorporating additional medical data, applying deep learning models, or exploring advanced feature selection techniques to further enhance predictive performance.
