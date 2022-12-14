import sys, os
sys.path.append(os.path.dirname(os.path.realpath(__file__)) + "/../")

import charts
import logic
import data

import streamlit as st
# https://docs.streamlit.io/library/api-reference?highlight=beta_page_config#streamlit.set_page_config

####################
# Init Model Params
####################

init_param = dict(
    s0=5,
    mu=4,
    theta=12,
    T=5,
    dt=1/252,
    sigma=0.5,
    sims=100
)

#######################
# Model inputs
#######################

try:
    params = st.session_state['params']
except:
    params = init_param

c1, c2 = st.columns(2)

with c1:
    params['s0'] = st.number_input('s0',value=params['s0'])
    params['mu'] = st.number_input('mu',value=params['mu'])
    params['theta'] = st.number_input('theta',value=params['theta'])
    params['T'] = st.number_input('T',min_value=1, max_value=10, value=params['T'])

with c2:
    dt = st.selectbox('dt',['daily', 'business days', 'weekly', 'monthly', 'annually'])
    params['sigma'] = st.number_input('sigma',value=params['sigma'])
    params['sims'] = st.number_input('sigma',value=params['sims'])
    params['dt'] = logic.convert_dt[dt]
    r = st.number_input('Fixed Rate (r)',0)

ir_method = st.radio('Pick DCF Method', ['Fixed Rate (r)', 'Interest Rate Curve'])

#######################
# save session state
#######################

st.session_state['params'] = params
st.session_state['dt'] = dt
st.session_state['test'] = 'state working'

#######################
# Run model
#######################

df = logic.sim_df(params)

#######################
# Cache Charts
#######################

fig_dict = charts.cached_plots(df)

#######################
# App Body
#######################

st.title("Template Streamlit Application")

st.write(
    """
    This is a template application for streamlit
    
    """
)

st.write(params)

ir = logic.get_ir(df.reset_index().index*logic.convert_dt[dt])

c3, c4 = st.columns(2)

with c3:
    st.table(ir[:10])

with c4: 
    st.plotly_chart(fig_dict['sims'])