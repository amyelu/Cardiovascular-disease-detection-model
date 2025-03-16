# Cardiovascular Disease Risk Assessment Model
### Overview
This model is designed for early detection and risk assessment of cardiovascular diseases. It is interactive and accessible for both healthcare providers and individuals monitoring their health, providing real-time predictions based on user inputs.

**🔗 Try it live:** [Click here](https://cardiovascular-disease-detection-model.streamlit.app/)

### Dataset & Features
The dataset was sourced from Kaggle (by Svetlana Ulianova) and includes key medical predictor variables. The most important features used in the model are:

- ap_hi (Systolic Blood Pressure)
- ap_lo (Diastolic Blood Pressure)
- age
- Physically_Active
- Alcoholic_status
- Bp_category (Blood Pressure Category)
- cholesterol
- BMI (Body Mass Index)
- weight_kg
- glucose_level
- sys_dsys_ratio (Systolic/Diastolic Ratio)
- height_cm 

Categorical columns were engineered and encoded, while numerical values were scaled for linear models and SVM. Additional features such as blood pressure category and systolic/diastolic ratio were derived to enhance prediction accuracy.

### Model Development & Performance
Several models were tested, including:

- LogisticRegression
- SGDClassifier
- SVC
- XGBClassifier
- GradientBoostingClassifier
- BaggingClassifier
- AdaBoostClassifier
- DecisionTreeClassifier
- RandomForestClassifier
- ExtraTreesClassifier
  
Polynomial features were also explored to capture complex relationships within the data.

##### Evaluation Metrics Used:

- Accuracy
- Precision
- Recall
- F1-score
  
**The best-performing model was GradientBoostingClassifier, achieving:**

- Accuracy: 73.69%
- Precision: 75.97%
- Recall: 73.62%
- F1-Score: 73.59%
  
### Deployment & User Interaction
The model is currently deployed via Streamlit, where users input variables like blood pressure, age, weight, and physical activity. The system calculates BMI, blood pressure category, and systolic/diastolic ratio before predicting cardiovascular risk.

However, the model's size is 613.1 KB, making it feasible for deployment beyond Streamlit, such as through cloud-based services or mobile applications for wider accessibility.

Future Improvements
Although the model provides promising results, its performance could be significantly enhanced with a more robust dataset. A dataset with:
- More diverse patient records (covering different demographics and medical histories)
- Additional medical indicators such as smoking status, physical exam results, or genetic markers
- Longitudinal data (tracking patient outcomes over time)

These improvements will help refine predictions and reduce errors.

### Impact & Vision
This model aims to:
- Encourage early detection of cardiovascular diseases, helping individuals take their health seriously
- Assist healthcare professionals in risk assessment and patient monitoring
- Expand its reach beyond Streamlit to make cardiovascular risk assessment more accessible via web applications, APIs, or mobile health platforms

Ultimately, retraining the model with a more comprehensive dataset will make it more encompassing, improving predictive accuracy and clinical usefulness.
