import risktools as rt
import pandas as pd
import streamlit as st

import os
import time

def update_ir():
    # Path to the file/directory
    path = "ir.p"

    # Both the variables would contain time
    # elapsed since EPOCH in float
    ti_c = os.path.getctime(path)
    ti_m = os.path.getmtime(path)

    # Converting the time in seconds to a timestamp
    c_ti = time.ctime(ti_c)
    m_ti = time.ctime(ti_m)

    mdt = pd.to_datetime(max(c_ti, m_ti))

    st.write(f"The file located at the path {path} \
    was created/modified on {mdt}")

    try:
        ir = pd.read_pickle('ir.p')
    except:
        pass

    if mdt < pd.Timestamp.now().floor('D'):
        try:
            ir = rt.ir_df_us()
            ir.to_pickle('ir.p')
        except:
            pd.read_pickle('ir.p')

    return ir