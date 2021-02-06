import streamlit as st
import pandas as pd
import base64
import matplotlib.pyplot as plt
import seaborn as sns
import numpy as np



st.title('Football - Social Media Recruiting Assistance')


st.markdown("""
While many college athletic teams and related companies are dabbling in the social arena, many are
simply not doing it well. GT football would like a way to better utilize the social arena. This could include:

1. Character assessment: The stronger the character, the more attractive a prospect is as a potential
candidate. 

2. Candidate identification: Find football recruits that GT may not be aware of. Ex: interested in Georgia
Tech, football/related sports, engineering, Atlanta, etc.!

* **Python libraries:** base64, pandas, streamlit, numpy, matplotlib, seaborn
* **Data source:** [pro-football-reference.com](https://www.pro-football-reference.com/).
""")

dataframe = st.beta_container()



@st.cache
def get_data(filename):
    players_data = pd.read_csv(filename)
    return players_data


with dataframe:
    
    data = get_data('data/players.csv')

    st.header('Data as Per Student Year')
    Year = data['year'].unique()
    year_selected = st.multiselect('', Year)

    mask_years = data['year'].isin(year_selected)
    data = data[mask_years]
    st.write(data)

