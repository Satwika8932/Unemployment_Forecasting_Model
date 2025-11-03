## What is Unemployment Forecasting Model?

Unemployment Forecasting Model is a data-driven web application (or command-line tool / model pipeline) that predicts future unemployment rates and trends using historical labour-market and macro-economic data. It helps analysts, policymakers, or business users anticipate shifts in unemployment, optimise resource planning, and generate insights into labour-market dynamics.

## Key Features

📊 **Data Ingestion & Pre-processing**

* Load and clean historical unemployment and labour-market datasets
* Engineer features (e.g., macro-indicators, time-series lags, seasonal factors)
* Handle missing data, outliers, and apply transformations

📈 **Forecasting & Model Training**

* Train time-series and machine-learning models (ARIMA, LSTM, Random Forest, etc)
* Evaluate forecasting performance (RMSE, MAE, MAPE)
* Compare multiple model types and pick best-performing one

🔍 **Insights & Visualisations**

* Plot historical vs-forecast unemployment rates
* Analyse feature importance and model behaviour
* Generate scenario-based forecasts (e.g., if macro-indicator X shifts)

🔧 **Deployment-Ready Pipeline**

* Automate training and prediction steps
* Export model for inference or integration
* (Optional) Provide REST API or web UI for end-users

## Tech Stack

**Backend / Core Modelling:**

* Python (Pandas, NumPy, Scikit-Learn, TensorFlow / PyTorch or statsmodels)
* Time-series frameworks (e.g., ARIMA, LSTM)
* Jupyter notebooks for exploration and prototyping


## Quick Start Guide

### Prerequisites

* Python 3.8+
* Git clone of the repository
* Required Python packages (listed in `requirements.txt`)
* Historical unemployment and economic indicator datasets

### Installation Steps

1. **Clone the repository**

   ```bash
   git clone https://github.com/Satwika8932/Unemployment_Forecasting_Model.git  
   cd Unemployment_Forecasting_Model  
   ```

2. **Set up virtual environment**

   ```bash
   python -m venv venv  
   source venv/bin/activate      # On Windows: venv\Scripts\activate  
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt  
   ```


4. **Now we check which is the best model among all the models (ARIMA, SARIMAX, ...) and we download the model as "model.pkl"**

5. **We upload the model (model.pkl) in app.py**

6. **Launch interface**

   ```bash
   python app.py
   ```


## Configuration Details

**Dataset Sources:**

* Historical unemployment data (e.g., from national labour agencies)
* Macro-economic indicators (GDP growth, inflation, job-openings, etc)
* Time-series features: lagged variables, seasonality indexing

**Model Settings & Hyperparameters:**

* Define in `config.yml` or `settings.py` (e.g., model type, hyperparameters, train/test split)
* For LSTM: sequence length, number of layers, dropout rate
* For ARIMA/Prophet: order (p,d,q), seasonal order

## Acknowledgments

Thanks to all the open-source libraries and frameworks:

* Pandas, NumPy, Scikit-Learn, TensorFlow / PyTorch
* Jupyter for interactive modelling
