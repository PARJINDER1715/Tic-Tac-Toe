import streamlit as st
from game import is_winner, is_draw, best_move
from state import init_game_state

init_game_state()

# === UI Styling ===
st.markdown("""
    <style>
    div[data-testid="column"] button {
        height: 60px;
        font-size: 28px;
    }
    div[data-testid="column"] button:hover {
        background-color: #f0f0f0;
        border: 2px solid #888;
    }
    </style>
""", unsafe_allow_html=True)

# === Sidebar ===
st.sidebar.title("Settings")
difficulty = st.sidebar.radio("Choose Difficulty:", ["Easy", "Medium", "Hard"])
st.session_state.difficulty = difficulty

mode = st.sidebar.radio("Game Mode:", ["AI", "Local Multiplayer"])
st.session_state.mode = mode

# Developer Credit in Sidebar
st.sidebar.markdown("---")
st.sidebar.markdown(
    "👨‍💻 Developed by **PARJINDER SINGH** "
    "[LinkedIn](https://www.linkedin.com/in/parjinder-singh)"
)

# === AI Move ===
def make_ai_move():
    move = best_move(st.session_state.board, st.session_state.difficulty)
    if move != -1:
        st.session_state.board[move] = "O"
        st.session_state.turn = "X"

        if is_winner(st.session_state.board, "O"):
            st.session_state.result = "AI Wins!"
            st.session_state.scores["AI"] += 1
        elif is_draw(st.session_state.board):
            st.session_state.result = "It's a Draw!"
            st.session_state.scores["Draw"] += 1

# === Title & Info ===
st.title("🎮 Tic-Tac-Toe")

if st.session_state.mode == "AI":
    st.subheader("You (❌) vs AI (⭕)")
else:
    st.subheader("Player 1 (❌) vs Player 2 (⭕)")

st.markdown(f"*Difficulty:* {st.session_state.difficulty if st.session_state.mode == 'AI' else 'N/A'}")

st.markdown(
    f"""<div style='margin-top:10px; font-size:16px;'>
        <b>Scores:</b><br>
        You: <span style='color:#00cc00'>{st.session_state.scores['Player']}</span> |
        AI: <span style='color:#ff3333'>{st.session_state.scores['AI']}</span> |
        Draws: <span style='color:#999999'>{st.session_state.scores['Draw']}</span>
    </div>""",
    unsafe_allow_html=True
)

# === Game Board ===
emoji_map = {"X": "❌", "O": "⭕", "": " "}
cols = st.columns(3)

for i in range(3):
    for j in range(3):
        idx = i * 3 + j
        with cols[j]:
            button_label = emoji_map[st.session_state.board[idx]]
            if st.button(button_label, key=idx,
                         disabled=(st.session_state.board[idx] != "" or 
                                   st.session_state.result != "" or
                                   (st.session_state.turn == "O" and st.session_state.mode == "AI")),
                         use_container_width=True):
                st.session_state.board[idx] = st.session_state.turn

                if is_winner(st.session_state.board, st.session_state.turn):
                    st.session_state.result = "You Win!" if st.session_state.mode == "AI" else f"{st.session_state.turn} Wins!"
                    if st.session_state.mode == "AI" and st.session_state.turn == "X":
                        st.session_state.scores["Player"] += 1
                elif is_draw(st.session_state.board):
                    st.session_state.result = "It's a Draw!"
                    st.session_state.scores["Draw"] += 1
                else:
                    st.session_state.turn = "O" if st.session_state.turn == "X" else "X"
                    if st.session_state.mode == "AI" and st.session_state.turn == "O":
                        make_ai_move()

# === Result Display ===
if st.session_state.result:
    st.success(st.session_state.result)
    if "Win" in st.session_state.result:
        st.balloons()
    elif "Draw" in st.session_state.result:
        st.toast("Game tied!")

# === Restart Button ===
if st.button("Restart Game"):
    st.session_state.board = [""] * 9
    st.session_state.turn = "X"
    st.session_state.result = ""


