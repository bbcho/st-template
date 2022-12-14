import streamlit as st
import risktools as rt
import plotly.express as px

def plot_sims(df, plotly=True):
    df = df.iloc[:,:100].copy()

    if plotly:
        fig = px.line(df)
        fig.update_layout(showlegend=False)

        return fig
    
    return df.plot(legend=False)

@st.cache(hash_funcs={dict: lambda _: None}) 
def cached_plots(df):

    fig_dict = {
        'sims':plot_sims(df)
    }



    return fig_dict
