import streamlit as st
from lotto_utils import *
st.title('🎱로또번호생성기')
n = st.number_input('몇게임할까요?', min_value=1, max_value=10, value=5)
if st.button('번호뽑기'):
    games = make_games(n)
    for i in range(n):
        st.write(f'**{i + 1}게임** : {to_text(games[i])}')