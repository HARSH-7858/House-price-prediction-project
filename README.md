# House Price Prediction Project

Machine learning project for predicting California housing prices using XGBoost regression in a Jupyter Notebook.

## Repository

GitHub: https://github.com/HARSH-7858/House-price-prediction-project.git

## Project Overview

This notebook-based project follows a complete regression workflow:

1. Loads the California Housing dataset from scikit-learn.
2. Performs exploratory analysis and correlation visualization.
3. Splits data into train and test sets.
4. Trains an XGBRegressor model.
5. Evaluates predictions with regression metrics.

Main notebook:
- House price prediction project.ipynb

## Tech Stack

- Python 3.10+
- NumPy
- Pandas
- Matplotlib
- Seaborn
- scikit-learn
- XGBoost
- Jupyter Notebook

## Setup and Run

1. Clone the repository

	git clone https://github.com/HARSH-7858/House-price-prediction-project.git
	cd House-price-prediction-project

2. Create and activate a virtual environment

	Windows PowerShell:
	python -m venv .venv
	.\.venv\Scripts\Activate.ps1

	macOS/Linux:
	python3 -m venv .venv
	source .venv/bin/activate

3. Install dependencies

	pip install -r requirements.txt

4. Launch notebook

	jupyter notebook

	Open House price prediction project.ipynb and run all cells.

## Evaluation Metrics

Regression metrics used in notebook:
- R-squared error
- Mean Absolute Error (MAE)

### F1 Score Evaluation

Because this project is regression, F1 is not directly defined on continuous prices.
To evaluate F1 meaningfully, prices were converted into two classes:

- Class 1: price >= median price
- Class 0: price < median price

Using the same train and test split as the notebook (test_size=0.2, random_state=2), the computed F1 score is:

- F1 score (binary): 0.8889
- Median threshold used: 1.797

## Push This Project to GitHub

If your local repo still points to an older remote, run:

git remote set-url origin https://github.com/HARSH-7858/House-price-prediction-project.git
git branch -M main
git add .
git commit -m "Add project README and update dependencies"
git push -u origin main

## Author

Harsh Raj Shrivastav
