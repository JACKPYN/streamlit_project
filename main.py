import streamlit as st
import numpy as np
import time

# 게임 보드 초기화
ROWS, COLS = 20, 10
if "board" not in st.session_state:
    st.session_state.board = np.zeros((ROWS, COLS), dtype=int)
if "current_pos" not in st.session_state:
    st.session_state.current_pos = [0, COLS // 2]

def draw_board(board):
    # 보드 그리기 (이모지 사용)
    display_board = ""
    for row in board:
        display_board += "".join("🟦" if cell else "⬛" for cell in row) + "\n"
    return display_board

def move_block(direction):
    # 블록 이동
    row, col = st.session_state.current_pos
    if direction == "left" and col > 0:
        st.session_state.current_pos[1] -= 1
    elif direction == "right" and col < COLS - 1:
        st.session_state.current_pos[1] += 1
    elif direction == "down" and row < ROWS - 1:
        st.session_state.current_pos[0] += 1

    # 보드 업데이트
    st.session_state.board = np.zeros((ROWS, COLS), dtype=int)
    r, c = st.session_state.current_pos
    st.session_state.board[r, c] = 1

# 게임 UI
st.title("Streamlit 테트리스 🎮")
st.text("간단한 블록 이동 게임입니다.")

# 버튼을 통한 블록 이동
col1, col2, col3 = st.columns(3)
with col1:
    if st.button("⬅️ 왼쪽"):
        move_block("left")
with col2:
    if st.button("⬇️ 아래"):
        move_block("down")
with col3:
    if st.button("➡️ 오른쪽"):
        move_block("right")

# 보드 그리기
st.markdown(f"```\n{draw_board(st.session_state.board)}\n```")
