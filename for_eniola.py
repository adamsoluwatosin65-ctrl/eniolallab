import streamlit as st

# Setup the page
st.set_page_config(page_title="For Eniola", page_icon="❤️")

# Big Title
st.title("Eniola,")

# The Main Message
st.header("You are never an option to me.")
st.subheader("You are the only choice.")

# Create two columns for buttons
col1, col2 = st.columns(2)

with col1:
    if st.button("YES"):
        st.balloons()
        st.success("I knew it. Always you. ❤️")
        st.write("### Decision Confirmed.")

with col2:
    if st.button("NO"):
        # Since we can't move buttons easily on web, we use a funny error
        st.error("Error: 'No' is not an option for Eniola.")
        st.info("Please select the correct choice (Hint: It's the gold button).")
