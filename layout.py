import streamlit as st
import pandas as pd
tab1, tab2 = st.tabs(['첫번째탭', '두번째탭'])

with tab1:                         # 첫번째탭안
    col1, col2 = st.columns(2)     # 나란히두칸
    if col1.button('왼쪽버튼'):
        st.write('왼쪽을눌렀다')
    if col2.button('오른쪽버튼'):
        st.write('오른쪽을눌렀다')
        
with tab2:                         # 두번째탭안
    fruits = st.multiselect('과일고르기', ['사과', '배', '감', '귤'],max_selections=2)
    st.write('고른과일:', ', '.join(fruits))
    st.bar_chart(pd.Series({'사과': 5, '배': 3, '감': 7}))