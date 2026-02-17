import streamlit as st

# 1. Basic Page Configuration
st.set_page_config(page_title="For Eniola", page_icon="❤️")

# 2. Simple Header
st.title("Eniola,")
st.write("### You are never an option to me. You are the only choice.")

# 3. Interactive Buttons
col1, col2 = st.columns(2)

with col1:
    if st.button("YES"):
        st.balloons()
        st.success("Always you, Eniola. Always. ❤️")
        st.write("## I knew it!")

with col2:
    if st.button("NO"):
        st.error("Error 404: 'No' is not a valid choice for Eniola.")
        st.info("Try clicking the other button. 😉")

# 4. A Little Note at the bottom
st.write("---")
st.caption("Made with love.")
