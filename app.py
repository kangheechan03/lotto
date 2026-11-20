import streamlit as st
from lotto_utils import *

st.title('🎱로또번호생성기')
#123
@st.cache_data# CSV는처음한번만읽기
def get_counts():
    return load_counts('lotto.csv')

count = get_counts()
tab1, tab2, tab3 = st.tabs(['🎲자동뽑기', '📊번호별통계', '✋수동선택'])

with tab1:                          # ①자동뽑기
    n = st.number_input('몇게임할까요?', min_value=1, max_value=10, value=5)
    col1, col2 = st.columns(2)
    if col1.button('랜덤으로뽑기'): 
        st.session_state.games= make_games(n)
    if col2.button('자주나온번호로뽑기'):
        games = []
        for i in range(n):
            games.append(make_hot_game(count))
        st.session_state.games= games
    if 'games' in st.session_state:
        for i in range(len(st.session_state.games)):
            st.write(f'**{i+ 1}게임** : {to_text(st.session_state.games[i])}')



