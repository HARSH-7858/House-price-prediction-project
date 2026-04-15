# Machine Learning Projects Repository

This repository contains multiple machine learning projects with Jupyter notebooks and interactive Streamlit web applications.

---

## 1. House Price Prediction Using XGBoost

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Streamlit](https://img.shields.io/badge/Streamlit-Web%20App-red)
![XGBoost](https://img.shields.io/badge/XGBoost-Model-brightgreen)

**Predict California housing prices using XGBoost regression model with an interactive Streamlit dashboard.**

### Features

- **Interactive Web App**: Built with Streamlit for real-time predictions
- **Model**: XGBoost Regressor trained on California Housing Dataset
- **Input Sliders**: Adjust 8 housing features to get instant price predictions
- **Analytics Dashboard**: Correlation heatmap, performance metrics, and visualizations

### Project Files

- `House price prediction project.ipynb` - Jupyter notebook with full ML workflow
- `streamlit_app.py` - Interactive web application (Streamlit)

### Running the Streamlit App

```bash
streamlit run streamlit_app.py
```

The app will open at: **http://localhost:8501**

### Dataset

**California Housing Dataset** from scikit-learn:
- 20,640 samples
- 8 features: MedInc, HouseAge, AveRooms, AveBedrms, Population, AveOccup, Latitude, Longitude
- Target: Median house value (in $100,000 units)

### Model Performance

- **Training R² Score**: ~0.9
- **Test R² Score**: ~0.57
- **Evaluation Metric**: Mean Absolute Error (MAE)

### App Features

| Tab | Description |
|-----|------------|
| **Prediction** | Interactive sliders to input features and get price predictions |
| **Model Performance** | R² scores, MAE, and actual vs predicted scatter plots |
| **Data Analysis** | Correlation heatmap and dataset statistics |
| **About** | Model information and feature descriptions |

---

## 2. Diabetes Prediction Using Machine Learning

![Python](https://img.shields.io/badge/Python-3.x-blue)
![Jupyter Notebook](https://img.shields.io/badge/Jupyter-Notebook-orange)
![scikit-learn](https://img.shields.io/badge/scikit--learn-ML-f7931e)
![Status](https://img.shields.io/badge/Project-Notebook%20Based-success)

This project predicts whether a person is diabetic or not using a Support Vector Machine model trained on the `diabetes.csv` dataset. The full workflow is documented in the notebook and covers data loading, preprocessing, model training, evaluation, and sample predictions.

### Project Overview

- Dataset: `diabetes.csv`
- Notebook: `Diabetes prediction using ML.ipynb`
- Model: Support Vector Classifier (`SVC`) with a linear kernel
- Preprocessing: `StandardScaler`
- Train/test split: 80/20 with stratification

### Dataset Details

The dataset contains 768 rows and 9 columns:

- 8 input features: `Pregnancies`, `Glucose`, `BloodPressure`, `SkinThickness`, `Insulin`, `BMI`, `DiabetesPedigreeFunction`, `Age`
- 1 target column: `Outcome`

`Outcome = 0` means non-diabetic and `Outcome = 1` means diabetic.

### Workflow

The notebook performs the following steps:

1. Imports the required Python libraries.
2. Loads the diabetes dataset from the repository.
3. Explores the data using shape, summary statistics, class counts, and grouped means.
4. Separates input features and target labels.
5. Standardizes the feature values using `StandardScaler`.
6. Splits the data into training and testing sets.
7. Trains a linear SVM classifier.
8. Evaluates training and test accuracy.
9. Runs prediction examples on custom input values.

### Results

The saved notebook output reports:

- Training accuracy: `0.7727`
- Test accuracy: `0.7727`

These numbers come from the current notebook run stored in the file and may vary slightly if you retrain with different settings.

### Project Structure

```text
Machine Learning/
|-- Diabetes prediction using ML.ipynb
|-- diabetes.csv
|-- requirements.txt
|-- README.md
|-- .gitignore
|-- .gitattributes
```

- `Diabetes prediction using ML.ipynb` - main notebook for training and prediction
- `diabetes.csv` - input dataset
- `requirements.txt` - Python dependencies
- `README.md` - project documentation
- `.gitignore` - ignores virtual environments, notebook checkpoints, and local editor files
- `.gitattributes` - keeps line endings consistent for Git-tracked project files

## Setup

1. Create and activate a virtual environment.
2. Install dependencies:

```bash
pip install -r requirements.txt
```

## Run The Project

Start Jupyter and open the notebook:

```bash
jupyter notebook
```

Then open `Diabetes prediction using ML.ipynb` and run the cells from top to bottom.

## Notes

- The notebook now loads `diabetes.csv` using a repository-relative path, which makes the project portable after cloning from GitHub.
- The project is notebook-based and does not yet export the trained model as a separate file.
