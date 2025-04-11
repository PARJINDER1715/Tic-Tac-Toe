import streamlit as st

def init_game_state():
    if 'board' not in st.session_state:
        st.session_state.board = [""] * 9
        st.session_state.turn = "X"
        st.session_state.result = ""
        st.session_state.scores = {"Player": 0, "AI": 0, "Draw": 0}
    if 'difficulty' not in st.session_state:
        st.session_state.difficulty = "Hard"
    if 'last_click' not in st.session_state:
        st.session_state.last_click = False
