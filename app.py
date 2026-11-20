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
# 1111
with tab2:                          # ②번호별당첨횟수
    st.write('1회~ 1250회당첨번호6개기준(보너스제외)')
    st.bar_chart(pd.Series(count, name='당첨횟수'))
    top10 = top_numbers(count, 10)
    st.write('자주나온번호TOP 10 :', to_text(top10))

with tab3:                          # ③수동선택+ 자동채우기
    picked = st.multiselect('번호를고르세요(최대6개)', list(range(1, 46)),
                            max_selections=6,
                            format_func=lambda x: f'{x}번({count[x]}회)')
    if st.button('나머지자동으로채우기'):
        st.success(to_text(fill_game(picked)))


