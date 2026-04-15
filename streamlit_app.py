import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import sklearn.datasets
from sklearn.model_selection import train_test_split
from xgboost import XGBRegressor
from sklearn import metrics

# Set page config
st.set_page_config(page_title="House Price Predictor", layout="wide")

st.title("🏠 House Price Prediction")
st.markdown("Predict California housing prices using XGBoost")

# Load and prepare data
@st.cache_resource
def load_model_and_data():
    # Load dataset
    house_price_dataset = sklearn.datasets.fetch_california_housing()
    house_price_dataframe = pd.DataFrame(
        house_price_dataset.data, 
        columns=house_price_dataset.feature_names
    )
    house_price_dataframe['price'] = house_price_dataset.target
    
    # Split data
    X = house_price_dataframe.drop(['price'], axis=1)
    Y = house_price_dataframe['price']
    X_train, X_test, Y_train, Y_test = train_test_split(X, Y, test_size=0.2, random_state=2)
    
    # Train model
    model = XGBRegressor()
    model.fit(X_train, Y_train)
    
    return model, X_train, X_test, Y_train, Y_test, house_price_dataframe

model, X_train, X_test, Y_train, Y_test, house_price_dataframe = load_model_and_data()

# Create tabs
tab1, tab2, tab3, tab4 = st.tabs(["Prediction", "Model Performance", "Data Analysis", "About"])

# Tab 1: Prediction
with tab1:
    st.subheader("Make a Prediction")
    col1, col2 = st.columns(2)
    
    with col1:
        medinc = st.slider("Median Income", float(X_train['MedInc'].min()), float(X_train['MedInc'].max()), 
                          float(X_train['MedInc'].median()))
        houseage = st.slider("House Age", float(X_train['HouseAge'].min()), float(X_train['HouseAge'].max()), 
                            float(X_train['HouseAge'].median()))
        averoom = st.slider("Average Rooms", float(X_train['AveRooms'].min()), float(X_train['AveRooms'].max()), 
                           float(X_train['AveRooms'].median()))
        avebdrm = st.slider("Average Bedrooms", float(X_train['AveBedrms'].min()), float(X_train['AveBedrms'].max()), 
                           float(X_train['AveBedrms'].median()))
    
    with col2:
        population = st.slider("Population", float(X_train['Population'].min()), float(X_train['Population'].max()), 
                              float(X_train['Population'].median()))
        aveoccup = st.slider("Average Occupancy", float(X_train['AveOccup'].min()), float(X_train['AveOccup'].max()), 
                            float(X_train['AveOccup'].median()))
        latitude = st.slider("Latitude", float(X_train['Latitude'].min()), float(X_train['Latitude'].max()), 
                            float(X_train['Latitude'].median()))
        longitude = st.slider("Longitude", float(X_train['Longitude'].min()), float(X_train['Longitude'].max()), 
                             float(X_train['Longitude'].median()))
    
    # Make prediction
    input_data = np.array([[medinc, houseage, averoom, avebdrm, population, aveoccup, latitude, longitude]])
    prediction = model.predict(input_data)[0]
    
    st.markdown("---")
    col_pred1, col_pred2 = st.columns(2)
    with col_pred1:
        st.metric(label="Predicted Price", value=f"${prediction*100000:.2f}")
    with col_pred2:
        st.info(f"💡 Price estimate in units: **${prediction:.4f}**\n\n(Multiply by 100,000 for actual USD)")

# Tab 2: Model Performance
with tab2:
    st.subheader("Model Performance Metrics")
    
    # Training metrics
    training_prediction = model.predict(X_train)
    train_r2 = metrics.r2_score(Y_train, training_prediction)
    train_mae = metrics.mean_absolute_error(Y_train, training_prediction)
    
    # Testing metrics
    test_prediction = model.predict(X_test)
    test_r2 = metrics.r2_score(Y_test, test_prediction)
    test_mae = metrics.mean_absolute_error(Y_test, test_prediction)
    
    col_metric1, col_metric2, col_metric3, col_metric4 = st.columns(4)
    
    with col_metric1:
        st.metric("Training R² Score", f"{train_r2:.4f}")
    with col_metric2:
        st.metric("Training MAE", f"{train_mae:.4f}")
    with col_metric3:
        st.metric("Testing R² Score", f"{test_r2:.4f}")
    with col_metric4:
        st.metric("Testing MAE", f"{test_mae:.4f}")
    
    st.markdown("---")
    
    # Visualization
    col_viz1, col_viz2 = st.columns(2)
    
    with col_viz1:
        st.subheader("Training Set: Actual vs Predicted")
        fig1, ax1 = plt.subplots()
        ax1.scatter(Y_train, training_prediction, alpha=0.5)
        ax1.plot([Y_train.min(), Y_train.max()], [Y_train.min(), Y_train.max()], 'r--', lw=2)
        ax1.set_xlabel("Actual Prices")
        ax1.set_ylabel("Predicted Prices")
        st.pyplot(fig1)
    
    with col_viz2:
        st.subheader("Testing Set: Actual vs Predicted")
        fig2, ax2 = plt.subplots()
        ax2.scatter(Y_test, test_prediction, alpha=0.5, color='orange')
        ax2.plot([Y_test.min(), Y_test.max()], [Y_test.min(), Y_test.max()], 'r--', lw=2)
        ax2.set_xlabel("Actual Prices")
        ax2.set_ylabel("Predicted Prices")
        st.pyplot(fig2)

# Tab 3: Data Analysis
with tab3:
    st.subheader("Dataset Overview")
    
    col_info1, col_info2, col_info3 = st.columns(3)
    with col_info1:
        st.metric("Total Samples", len(house_price_dataframe))
    with col_info2:
        st.metric("Features", len(house_price_dataframe.columns) - 1)
    with col_info3:
        st.metric("Training Samples", len(X_train))
    
    st.markdown("---")
    
    st.subheader("Feature Correlation Heatmap")
    correlation = house_price_dataframe.corr()
    fig, ax = plt.subplots(figsize=(10, 8))
    sns.heatmap(correlation, cbar=True, square=True, fmt='.2f', annot=True, 
                annot_kws={'size': 8}, cmap='Blues', ax=ax)
    st.pyplot(fig)
    
    st.markdown("---")
    st.subheader("Dataset Statistics")
    st.dataframe(house_price_dataframe.describe())

# Tab 4: About
with tab4:
    st.subheader("About This App")
    st.markdown("""
    ### California Housing Price Predictor
    
    **Dataset:** California Housing Dataset from scikit-learn
    
    **Model:** XGBoost Regressor
    
    **Features (8):**
    - **MedInc:** Median income in block
    - **HouseAge:** Median house age in block
    - **AveRooms:** Average number of rooms per household
    - **AveBedrms:** Average number of bedrooms per household
    - **Population:** Block population
    - **AveOccup:** Average occupancy per household
    - **Latitude:** Latitude of block
    - **Longitude:** Longitude of block
    
    **Target:** Median house value (in $100,000 units)
    
    **Model Performance:**
    - Uses train-test split (80-20)
    - Evaluates with R² Score and Mean Absolute Error (MAE)
    - Provides interactive predictions
    
    **How to Use:**
    1. Go to the "Prediction" tab
    2. Adjust the sliders for each feature
    3. View the predicted house price instantly
    """)
