import numpy as np
import streamlit as st
import plotly.express as px



fileName = "20210826Z111434.txt"
totalTimeInSeconds = 0.8446
numberOfDataPoints = 4224


xData = np.linspace(0, totalTimeInSeconds, numberOfDataPoints)
yData = np.loadtxt(fileName, delimiter=",")




fig = px.line(x=xData, y=yData)
st.plotly_chart(fig)
