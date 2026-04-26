import streamlit as st
import random

# Game setup
choices = ["ROCK", "PAPER", "SCISSORS"]

win_map = {
    "ROCK": "SCISSORS",
    "SCISSORS": "PAPER",
    "PAPER": "ROCK"
}

# Initialize session state (important for web apps)
if "user_score" not in st.session_state:
    st.session_state.user_score = 0

if "computer_score" not in st.session_state:
    st.session_state.computer_score = 0


st.title("🎮 Rock Paper Scissors Game")
st.write("First to 2 wins the match 🏆")

# Buttons UI
col1, col2, col3 = st.columns(3)

user_choice = None

with col1:
    if st.button("🪨 Rock"):
        user_choice = "ROCK"

with col2:
    if st.button("📄 Paper"):
        user_choice = "PAPER"

with col3:
    if st.button("✂️ Scissors"):
        user_choice = "SCISSORS"


# Game logic
if user_choice:
    computer_choice = random.choice(choices)

    st.write(f"💻 Computer chose: **{computer_choice}**")

    if user_choice == computer_choice:
        st.info("😐 It's a Tie!")

    elif win_map[user_choice] == computer_choice:
        st.success("🎉 You Win this round!")
        st.session_state.user_score += 1

    else:
        st.error("💻 Computer wins this round!")
        st.session_state.computer_score += 1

    # Score display
    st.write(f"📊 Score → You: {st.session_state.user_score} | Computer: {st.session_state.computer_score}")


# Match result
if st.session_state.user_score == 2:
    st.balloons()
    st.success("🏆 You won the match!")

elif st.session_state.computer_score == 2:
    st.error("💻 Computer won the match!")

# Restart button
if st.button("🔄 Restart Game"):
    st.session_state.user_score = 0
    st.session_state.computer_score = 0
    st.rerun()