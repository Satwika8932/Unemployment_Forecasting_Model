from flask import Flask, render_template, request, redirect, url_for
import pandas as pd
import numpy as np
from prophet import Prophet
import plotly.express as px
import pickle
with open(r"model.pkl", "rb") as f:
    model=pickle.load(f)
app=Flask(__name__)
@app.route('/')
def index():
    return render_template('index.html')
@app.route('/inspect', methods=['GET','POST'])
def inspect():
    if request.method=='POST':
        try:
            input_date_str=request.form['date']
            input_date=pd.to_datetime(input_date_str)
            future_date=pd.DataFrame({'ds':[input_date]})
            forecast=model.predict(future_date)
            predicted_value=np.exp(forecast['yhat'].values[0])
            fig=px.line(forecast,x='ds',y='yhat',title='Insurance Forecast')
            graph=fig.to_html(full_html=False)
            return render_template('output.html',prediction=np.round(predicted_value),date=input_date_str,graph=graph)
        except Exception as e:
            return render_template('output.html', error=f"An error occurred: {str(e)}")
    return render_template('inspect.html')
@app.route('/output')
def output():
    return redirect(url_for('index'))
if __name__=='__main__':
    app.run(debug=True)