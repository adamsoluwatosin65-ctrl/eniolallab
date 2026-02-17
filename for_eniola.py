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
    # Adding a unique key ensures the button styling stays consistent
    if st.button("YES", type="primary"):
        # This triggers the 'falling' animation effect
        st.balloons() 
        
        # Displaying the big love heart as requested
        st.markdown("<h1 style='text-align: center; font-size: 100px;'>❤️</h1>", unsafe_allow_all_html=True)
        
        st.success("I knew it. Always you. ❤️")
        st.write("### Decision Confirmed.")

with col2:
    if st.button("NO"):
        st.error("Error: 'No' is not an option for Eniola.")
        st.info("Please select the correct choice (Hint: It's the gold button).")
