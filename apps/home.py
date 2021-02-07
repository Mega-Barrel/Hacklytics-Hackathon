import streamlit as st
import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px

st.set_option('deprecation.showPyplotGlobalUse', False)                            # To remove Warnings Messages


@st.cache                                                                         # Reading the CSV file
def get_data(filename):
    players_data = pd.read_csv(filename)
    return players_data


def app():
    st.title('Football - Social Media Recruiting Assistance')                          # Set Title for the Web App


    data = get_data('datasets/currenttwit.csv')

    st.header('Data as State')
    States = data['state'].unique()
    state_selected = st.multiselect('', States)

    state_years = data['state'].isin(state_selected)
    data = data[state_years]
    st.write(data)



    '''
    Intercorrelation Heatmap for Viz.
    '''
    # if st.button('Intercorrelation Heatmap'):
    st.header('HeatMap for the Dataset')
    data = get_data('datasets/currenttwit.csv')

    corr = data.corr()
    mask = np.zeros_like(corr)
    with sns.axes_style("white"):
        f, ax = plt.subplots(figsize=(15, 10))
        ax = sns.heatmap(corr, mask=mask, vmax=1, square=True,  annot=True)
    st.pyplot()


    '''
    BarPlot for Viz.
    '''
    # if st.button('Histogram'):
    data = get_data('datasets/currenttwit.csv')

    plt.figure(figsize=(15,10))
    fig = px.histogram(data, x='Position', title="Histogram based on Position Count")
    st.plotly_chart(fig)