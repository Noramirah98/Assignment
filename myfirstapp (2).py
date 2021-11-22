import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
from plotly.subplots import make_subplots
import plotly.graph_objects as go
import matplotlib.pyplot as plt

DATA_URL=("/content/total-number-of-prisoners-in-malaysia.zip")

def load_data():
    data=pd.read_csv(DATA_URL)
    return data

df=load_data()

st.dataframe(df)

st.sidebar.checkbox("Show Analysis by State", True, key=1)
select = st.sidebar.selectbox('Select a State',df['State'])


#get the state selected in the selectbox
state_data = df[df['State'] == select]
select_year = st.sidebar.radio("Year", ('2016','2017','2018','2019'))

def get_total_dataframe(dataset):
    total_dataframe = pd.DataFrame({
    'Year':['2016','2017','2018','2019'],
    'Number of prisoners':(dataset.iloc[0]['2016'],dataset.iloc[0]['2017'],dataset.iloc[0]['2018'], dataset.iloc[0]['2019'])})
    return total_dataframe

state_total = get_total_dataframe(state_data)

if st.sidebar.checkbox("Show Analysis by State", True, key=2):
    st.markdown("## **State level analysis**")
    st.markdown("### Total number of prisoners " + 
                " in %s from 2016-2019" % (select))
    if not st.checkbox('Hide Graph', False, key=1):
        state_total_graph = px.bar(
        state_total, 
        x='Year',
        y='Number of prisoners',
        labels={'Number of prisoners':'Number of prisoners in %s' % (select)},
        color='Year')
        st.plotly_chart(state_total_graph)

def get_table():
    datatable = df[['State', '2016', '2017', '2018','2019']].sort_values(by=['2016'], ascending=False)
    datatable = datatable[datatable['State'] != 'State Unassigned']
    return datatable

datatable = get_table()
st.markdown("### Total number of prisoners in Malaysia from 2016-2019")
st.markdown("The following table gives you a real-time analysis of the number of prisoners in Malaysia.")
st.table(datatable)
