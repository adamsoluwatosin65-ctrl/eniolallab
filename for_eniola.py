import streamlit as st

# Basic setup that works every time
st.set_page_config(page_title="For Eniola", page_icon="❤️")

# The Message
st.title("Eniola,")
st.header("You are never an option to me.")
st.subheader("You are the only choice.")

# Two columns for the buttons
col1, col2 = st.columns(2)

with col1:
    if st.button("YES"):
        st.balloons()
        st.success("Always you, Eniola. Always. ❤️")
        st.write("### I knew it!")

with col2:
    if st.button("NO"):
        st.error("Error: 'No' is not a valid choice.")
        st.info("Try the other button! 😉")
