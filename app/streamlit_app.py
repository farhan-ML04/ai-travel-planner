import sys
import os

sys.path.append(os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))


import streamlit as st
from agents.root_agent import plan_trip

st.title("✈️ AI Travel Planner")

destination = st.text_input("Enter Destination")
budget = st.text_input("Enter Budget")

if st.button("Generate Plan"):
    if destination and budget:
        with st.spinner("Planning..."):
            result = plan_trip(destination, budget)
            st.markdown(result)
    else:
        st.warning("Fill all fields")