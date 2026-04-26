import streamlit as st
import random

st.title("🎯 Number Guessing Game")

# Initialize session state
if "secret_num" not in st.session_state:
    st.session_state.secret_num = random.randint(1, 100)

if "attempt" not in st.session_state:
    st.session_state.attempt = 0

if "max_attempt" not in st.session_state:
    st.session_state.max_attempt = 5

if "game_over" not in st.session_state:
    st.session_state.game_over = False


st.write("Guess a number between 1 and 100")
st.write(f"Attempts left: {st.session_state.max_attempt - st.session_state.attempt}")

guess = st.number_input("Enter your guess:", min_value=1, max_value=100, step=1)

if st.button("Submit Guess") and not st.session_state.game_over:
    st.session_state.attempt += 1

    if guess > st.session_state.secret_num:
        st.warning("TOO HIGH!")
    elif guess < st.session_state.secret_num:
        st.warning("TOO LOW!")
    else:
        st.success(f"You guessed it correct in {st.session_state.attempt} attempts!")
        st.session_state.game_over = True

    if st.session_state.attempt >= st.session_state.max_attempt and not st.session_state.game_over:
        st.error(f"Out of attempts! The number was {st.session_state.secret_num}")
        st.session_state.game_over = True


if st.button("Play Again"):
    st.session_state.secret_num = random.randint(1, 100)
    st.session_state.attempt = 0
    st.session_state.game_over = False