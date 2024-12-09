import streamlit as st
from utils import process_cv, generate_recommendations

# App Title
st.set_page_config(page_title="AI Karriererådgiver", layout="wide")
st.title("AI-drevet Karriererådgivning og Opkvalificering")

# File Upload
uploaded_file = st.file_uploader("Upload dit CV (PDF eller DOCX)", type=["pdf", "docx"])

if uploaded_file:
    st.success("CV uploadet!")
    if st.button("Analyser CV"):
        with st.spinner("Analyserer..."):
            extracted_text = process_cv(uploaded_file)
            st.write("Færdigheder fundet:")
            st.write(extracted_text["skills"])

            if st.button("Få anbefalinger"):
                recommendations = generate_recommendations(extracted_text["skills"])
                st.write("Foreslåede jobmuligheder og kurser:")
                st.json(recommendations)
            )
