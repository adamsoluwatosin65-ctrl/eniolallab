import streamlit as st

# 1. Page Config
st.set_page_config(page_title="For Eniola", page_icon="❤️")

# 2. Simple Styling (Clean & Direct)
st.markdown("""
<style>
    .stApp {
        background-color: #0a0a0a;
        color: #d4af37;
        text-align: center;
    }
    h1 { font-family: 'Georgia', serif; color: #d4af37; }
</style>
""", unsafe_allow_all_html=True)

# 3. The Message
st.title("Eniola,")
st.write("### You are never an option to me. You are the only choice.")

# 4. Interactive Buttons
col1, col2 = st.columns(2)

with col1:
    if st.button("YES"):
        st.balloons()
        st.success("Always you, Eniola. Always. ❤️")
        st.confetti() # This adds an extra spark!

with col2:
    if st.button("NO"):
        st.error("Error 404: 'No' is not a valid choice for Eniola.")
        st.info("Try clicking the other button. 😉")