# Customer Churn Prediction using Machine Learning

## Task Information
## INTERNSPARK POWERED BY ALFIDOTECH
**Internship:** Artificial Intelligence

**Task Number:** 1

**Project Title:** Customer Churn Prediction using Machine Learning


## Objective

The objective of this project is to build and evaluate machine learning models capable of predicting customer churn based on customer demographic information, account details, and service usage patterns.

The project compares compare multiple classification algorithms using train-test evaluation and cross validation and selects the best-performing model based on evaluation metrics.

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



## Project Workflow

1. Data Loading
2. Data Cleaning
3. Missing Value Handling
4. Feature Encoding
5. Exploratory Data Analysis (EDA)
6. Train-Test Split
7. Model Training
8. Model Evaluation
9. Cross Validation
10. Model Saving


## Models Used

### Logistic Regression

A statistical classification algorithm used for binary classification tasks.

### Random Forest Classifier

An ensemble learning algorithm that combines multiple decision trees for classification.


## Results

### Logistic Regression

| Metric    | Value  |

| Accuracy  | 0.8169 |
| Precision | 0.6803 |
| Recall    | 0.5818 |
| F1 Score  | 0.6272 |
| ROC-AUC   | 0.8615 |

### Random Forest

| Metric    | Value  |

| Accuracy  | 0.7956 |
| Precision | 0.6592 |
| Recall    | 0.4718 |
| F1 Score  | 0.5500 |
| ROC-AUC   | 0.8370 |

### Cross Validation

Average Cross Validation Accuracy:

0.8031 (80.31%)



## Best Model

Based on evaluation metrics and cross-validation results, **Logistic Regression** was selected as the final model.



## Environment Setup

Create and activate the conda environment:

```bash
conda create -n churn_project python=3.11
conda activate churn_project
```

### Package Versions

```bash
pip install pandas==2.3.1
pip install numpy==2.3.1
pip install matplotlib==3.10.3
pip install seaborn==0.13.2
pip install scikit-learn==1.7.1
pip install jupyter==1.1.1
```


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
Customer_Churn_Classification_Final.ipynb
```

### Step 4

Run all cells sequentially.

## Project Structure

```text
TASK1-Classification/
│
├── dataset/
│   └── ChurnDataset.csv
│
├── model/
│   └── churn_model.pkl
│
├── Customer_Churn_Classification_Final.ipynb
│
├── README.md
│
└── Task1_Report.pdf
└── requirements.txt
```


## Output

The project generates:

* Customer churn predictions
* Evaluation metrics
* Feature visualizations
* Cross-validation results
* Saved model file (`churn_model.pkl`)



## Author

Shaziya Banu

INTERNSPARK AI Internship


## GitHub Repository

Example:

https://github.com/shaziya27/Applied-Machine-Learning/tree/main/TASK1-Classification
