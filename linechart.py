import streamlit as st
import pandas as dp
import numpy as np
import altair as alt

st.header('Line chart')

chart_data = dp.DataFrame(
    np.random.randn(200, 3),
    columns=['C1', 'C2', 'C3']
)

c = alt.Chart(chart_data).mark_point().encode(x="C1", y="C2", size="C3", tooltip=['C1', 'C2', 'C3'])


st.write(c)

