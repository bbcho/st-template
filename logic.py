import risktools as rt
import pandas as pd
import streamlit as st
from scipy.interpolate import CubicSpline
import utils
import os
import time

IR = utils.update_ir()

@st.cache(suppress_st_warning=True)
def sim_df(params: dict):

    df = rt.simOU(**params)
    today = pd.Timestamp.now().floor('D').strftime('%Y-%m-%d')
    freq = st.session_state['dt']
    freq = convert_dt_freq[freq]

    dr = pd.date_range(today, freq=freq, periods=df.shape[0])
    df.index = dr

    return df

@st.cache(suppress_st_warning=True)
def get_ir(periods):

    ir = IR.copy()

    cv = CubicSpline(ir.maturity, ir.discountfactor)

    return pd.Series(cv(periods))


convert_dt = {
    'daily':1/365,
    'business days':1/252,
    'weekly':1/52,
    'monthly':1/12,
    'annually':1
}

convert_dt_freq = {
    'daily':'D',
    'business days':'B',
    'weekly':'W',
    'monthly':'MS',
    'annually':'YS'
}