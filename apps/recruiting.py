import streamlit as st
import numpy as np
import pandas as pd
import altair as alt

from data.create_data import by_category


def app():
    st.title('Recruiting Stats')
    st.markdown("### Defensive Stats")
    players_dfs = by_category()
    df = players_dfs[2]
    _df = df[[
        'file_year',
        'totaltackles',
        'tacklespergame',
        'tackles',
        'assists',
        'tacklesforloss',
        'sacks',
        'gamesplayed'
    ]]

    st.altair_chart(create_defensive_charts(_df), use_container_width=True)

    st.markdown("### Passing Stats")
    df = players_dfs[-2]
    _df = df[[
        'file_year',
        'passingyards',
        'passingyardspergame',
        'passingcomp',
        'passingatt',
        'completionpercentage',
        'passingtd',
        'passingint',
        'qbrating',
        'gamesplayed'
    ]]

    st.altair_chart(create_passing_charts(_df), use_container_width=True)


def create_passing_charts(_df):
    passing_yards_c = alt.Chart(_df).mark_boxplot().encode(
        x='file_year:O',
        y='passingyards:Q'
    )

    passingyardspergame_c = alt.Chart(_df).mark_boxplot().encode(
        x='file_year:O',
        y='passingyardspergame:Q'
    )
    passingcomp_c = alt.Chart(_df).mark_boxplot().encode(
        x='file_year:O',
        y='passingcomp:Q'
    )
    passingatt_c = alt.Chart(_df).mark_boxplot().encode(
        x='file_year:O',
        y='passingatt:Q'
    )
    completionpercentage_c = alt.Chart(_df).mark_boxplot().encode(
        x='file_year:O',
        y='completionpercentage:Q'
    )
    passingtd_c = alt.Chart(_df).mark_boxplot().encode(
        x='file_year:O',
        y='passingtd:Q'
    )
    passingint_c = alt.Chart(_df).mark_boxplot().encode(
        x='file_year:O',
        y='passingint:Q'
    )
    qbrating_c = alt.Chart(_df).mark_boxplot().encode(
        x='file_year:O',
        y='qbrating:Q'
    )
    gamesplayed_c = alt.Chart(_df).mark_boxplot().encode(
        x='file_year:O',
        y='gamesplayed:Q'
    )


    mega_chart = (passing_yards_c | passingyardspergame_c | passingcomp_c | passingatt_c | completionpercentage_c) & (passingtd_c | passingint_c | qbrating_c | gamesplayed_c)

    return mega_chart
    

def create_defensive_charts(_df):
    totaltackles_c = alt.Chart(_df).mark_boxplot().encode(
        x='file_year:O',
        y='totaltackles:Q'
    )

    tacklespergame_c = alt.Chart(_df).mark_boxplot().encode(
        x='file_year:O',
        y='tacklespergame:Q'
    )
    tackles_c = alt.Chart(_df).mark_boxplot().encode(
        x='file_year:O',
        y='tackles:Q'
    )
    assists_c = alt.Chart(_df).mark_boxplot().encode(
        x='file_year:O',
        y='assists:Q'
    )
    tacklesforloss_c = alt.Chart(_df).mark_boxplot().encode(
        x='file_year:O',
        y='tacklesforloss:Q'
    )
    sacks_c = alt.Chart(_df).mark_boxplot().encode(
        x='file_year:O',
        y='sacks:Q'
    )
    gamesplayed_c = alt.Chart(_df).mark_boxplot().encode(
        x='file_year:O',
        y='gamesplayed:Q'
    )


    mega_chart = (totaltackles_c | tacklespergame_c | tackles_c | assists_c) & (
        tacklesforloss_c | sacks_c | gamesplayed_c)
    return mega_chart
