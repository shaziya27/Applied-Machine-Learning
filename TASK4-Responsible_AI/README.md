# Responsible AI & Model Interpretation

## Task Information
## INTERNSPARK POWERED BY ALFIDOTECH
**Internship:** Artificial Intelligence

**Task Number:** 4

**Project Title:** Responsible AI Analysis and Model Interpretation for Customer Churn Prediction


## Objective

The objective of this project is to analyze the interpretability, fairness, and transparency of a machine learning model used for customer churn prediction.

The project focuses on:

* Feature Importance Analysis
* SHAP Explainability
* Fairness Assessment
* Bias Identification
* Mitigation Recommendations

## Dataset

**Dataset Name:** IBM Telco Customer Churn Dataset

**Records:** 7043

**Features:** 21

**Target Variable:** Churn

Target Classes:

* 0 → Customer Retained
* 1 → Customer Churned


## Technologies Used

* Python 3.11
* Jupyter Notebook
* NumPy
* Pandas
* Matplotlib
* Seaborn
* Scikit-Learn
* SHAP


## Project Workflow

1. Dataset Loading
2. Data Cleaning
3. Missing Value Handling
4. Label Encoding
5. Model Training (Logistic Regression)
6. Feature Importance Analysis
7. SHAP Explainability Analysis
8. Fairness Assessment
9. Bias Evaluation
10. Mitigation Recommendations


## Explainability Techniques Used

### Feature Importance

Feature importance was calculated using the coefficients of the Logistic Regression model.

This helps identify which features have the greatest influence on churn prediction.

### SHAP (SHapley Additive exPlanations)

SHAP was used to explain model predictions.

Benefits:

* Global Explainability
* Local Explainability
* Feature Contribution Analysis
* Improved Transparency


## Fairness Analysis

The following demographic groups were analyzed:

### Gender Fairness Analysis

Average churn probability by gender:

- Gender = 0 : 0.2692
- Gender = 1 : 0.2616

The difference is relatively small, indicating no significant gender-based bias.

### Senior Citizen Analysis

Average churn probability:

- Non-Senior : 0.2361
- Senior : 0.4168

Senior citizens show a higher predicted churn rate. This likely reflects underlying patterns in the dataset rather than intentional model bias, but continued fairness monitoring is recommended.


## Bias Mitigation Recommendations

The following recommendations were proposed:

1. Ensure balanced representation of demographic groups during model training.

2. Continuously monitor model performance across different customer groups.

3. Use explainability techniques such as SHAP for transparency.

4. Retrain the model periodically using updated customer data.

5. Evaluate fairness metrics before deployment.



## Environment Setup

Create and activate environment:

```bash
conda activate churn_project
```

Install required packages:

```markdown
### Package Versions

```bash
pip install pandas==2.3.1
pip install numpy==2.3.1
pip install matplotlib==3.10.3
pip install seaborn==0.13.2
pip install scikit-learn==1.7.1
pip install shap==0.48.0
pip install jupyter==1.1.1



## How to Run

### Step 1

Activate environment:

```bash
conda activate churn_project
```

### Step 2

Launch Jupyter Notebook:

```bash
jupyter notebook
```

### Step 3

Open:

```text
Responsible_AI_Interpretation.ipynb
```

### Step 4

Run all cells sequentially.



## Project Structure

```text
TASK4-ResponsibleAI/
│
├── Responsible_AI_Interpretation.ipynb
├── README.md
└── Task4_Report.pdf
```



## Output

The project generates:

* Feature Importance Table
* Feature Importance Plot
* SHAP Summary Plot
* SHAP Feature Importance Plot
* Gender Fairness Analysis
* Senior Citizen Fairness Analysis
* Bias Mitigation Recommendations

---

## Author

Shaziya Banu

INTERNSPARK AI Internship



## GitHub Repository

https://github.com/shaziya27/Applied-Machine-Learning/tree/main/TASK4-Responsible_AI
