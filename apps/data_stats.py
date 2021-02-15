import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from plotly import graph_objs as go
from apps.home import get_data
import plotly.express as px
import plotly.graph_objects as go



def app():
    st.title('Data Visualization')

    # st.write("This is a sample data stats in the mutliapp.")
    # st.write("See `apps/data_stats.py` to know how to use it.")

    data = get_data('datasets/currenttwit.csv')


    # Total Count of Players Rating as per state
    fig = go.Figure()
    for name, group in data.groupby('state'):
        trace = go.Histogram()
        trace.name = name
        trace.x = group['Rating']
        fig.add_trace(trace)

    fig.update_layout(
        title_text = 'Total counts of Players Rating as per State',
        width=900,
        height=500
    )
    st.plotly_chart(fig)


    # Map View
    fig = go.Figure(data=go.Choropleth(
        locations = data['state'], # Spatial coordinates
        z = data['sentiment'].astype(float), # Data to be color-coded
        locationmode = 'USA-states', # set of locations match entries in `locations`
        colorscale = 'Magenta',
        colorbar_title = "Sentiment As per States",
    ))

    fig.update_layout(
        title_text = 'Football player Sentiment Values by State',
        geo_scope='usa', # limite map scope to USA
    )

    st.plotly_chart(fig)




    
    