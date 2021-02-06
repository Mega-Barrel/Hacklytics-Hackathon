import streamlit as st
import pandas as pd
import numpy as np
from data.create_data import create_table
import seaborn as sns
import matplotlib.pyplot as plt

def app():
    st.title('Home')
    st.title('Football - Social Media Recruiting Assistance')                          # Set Title for the Web App

    st.write("""While many college athletic teams and related companies are dabbling in the social arena, many are
simply not doing well. Georgia Tech football would like a way to better sift through the social arena. This could include:

1. Character assessment: The stronger the character, the more attractive a prospect is as a potential
candidate. 

2. Candidate identification: Find football recruits that GT may not be aware of. For example: athletes interested in Georgia
Tech, football/related sports, engineering, Atlanta, etc.!

* **Python libraries:** base64, pandas, streamlit, numpy, matplotlib, seaborn
* **Data source:** [pro-football-reference.com](https://www.pro-football-reference.com/).
""")


st.write('Navigate to `Data Stats` page to visualize the data')

st.set_option('deprecation.showPyplotGlobalUse', False)                            # To remove Warnings Messages


dataframe = st.beta_container()                                                   # Creating A Container for dataframe


@st.cache                                                                         # Reading the CSV file
def get_data(filename):
    players_data = pd.read_csv(filename)
    return players_data


with dataframe:                                                                   # Displaying the DataFrame with options to show data Student Year wise.
    data = get_data('datasets/players.csv')

    st.header('Data as Per Student Year')
    Year = data['year'].unique()
    year_selected = st.multiselect('', Year)

    mask_years = data['year'].isin(year_selected)
    data = data[mask_years]
    st.write(data)



'''
Intercorrelation Heatmap for Viz.
'''

if st.button('Intercorrelation Heatmap'):
    st.header('Inter correlation HeatMap')
    data = get_data('datasets/players.csv')

    corr = data.corr()
    mask = np.zeros_like(corr)
    # mask[np.triu_indices_from(mask)] = True
    with sns.axes_style("white"):
        f, ax = plt.subplots(figsize=(7, 5))
        ax = sns.heatmap(corr, mask=mask, vmax=1, square=True)
    st.pyplot()


'''
BarPlot for Viz.
'''

if st.button('Barplot'):
    st.header('Barplot')
    data = get_data('datasets/players.csv')

    with sns.axes_style("white"):
        f, ax = plt.subplots(figsize=(7, 5))
        ax = sns.barplot(x = 'gamesplayed', y = 'high_school', data = data)
    st.pyplot()