import streamlit as st
import random
from quiz_data import quiz

st.set_page_config(page_title="Tebak Unsur Kimia", page_icon="🧪", layout="centered")

st.title("🧪 Game Tebak Unsur Kimia")

if "score" not in st.session_state:
    st.session_state.score = 0
    st.session_state.question = random.choice(quiz)
    st.session_state.answered = False

st.markdown("Tebak nama unsur dari simbol kimia berikut:")

st.subheader(f"{st.session_state.question['symbol']}")

answer = st.text_input("Jawaban kamu (dalam huruf kecil):")

if st.button("Cek Jawaban") and not st.session_state.answered:
    correct = st.session_state.question["name"]
    if answer.lower() == correct:
        st.success("✅ Benar!")
        st.session_state.score += 1
    else:
        st.error(f"❌ Salah. Jawaban yang benar adalah: *{correct}*")
    st.session_state.answered = True

if st.session_state.answered:
    if st.button("Soal Berikutnya"):
        st.session_state.question = random.choice(quiz)
        st.session_state.answered = False
        st.experimental_rerun()

st.markdown(f"### Skor: {st.session_state.score}")
