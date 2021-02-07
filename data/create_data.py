import pandas as pd
import numpy as np
import seaborn as sns
import matplotlib.pyplot as plt
import plotly.express as px
import streamlit as st


def create_table(n=7):
    df = pd.DataFrame({"x": range(1, 11), "y": n})
    df['x*y'] = df.x * df.y
    return df


@st.cache                                                                         # Reading the CSV file
def get_data(filename):
    players_data = pd.read_csv(filename)
    return players_data


def by_category():
    players_dfs = [
        "datasets/category_players/players_offense,rushing.csv",
        "datasets/category_players/players_offense,total+yards.csv",
        "datasets/category_players/players_defense,tackles.csv",
        "datasets/category_players/players_offense,touchdowns.csv",
        "datasets/category_players/players_defense,sacks.csv",
        "datasets/category_players/players_offense,receiving.csv",
        "datasets/category_players/players_defense,interceptions.csv",
        "datasets/category_players/players_offense,passing.csv",
        "datasets/category_players/players_offense,scoring.csv"
    ]
    return [get_data(fname) for fname in players_dfs]



