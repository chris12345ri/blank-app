import streamlit as st
from io import BytesIO
from PyPDF2 import PdfReader
import openai

# Streamlit App Configuration
st.set_page_config(page_title="AI Karriererådgiver", layout="wide")
st.title("AI-drevet Karriererådgivning og Opkvalificering")

# OpenAI API Key (erstat med din egen nøgle)
OPENAI_API_KEY = "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"
openai.api_key = OPENAI_API_KEY

# Funktion til at læse og analysere CV
def process_cv(file):
    if file.type == "application/pdf":
        pdf_reader = PdfReader(file)
        text = ""
        for page in pdf_reader.pages:
            text += page.extract_text()
    elif file.type in ["application/vnd.openxmlformats-officedocument.wordprocessingml.document", "application/msword"]:
        text = file.getvalue().decode("utf-8")
    else:
        text = None
    return text

# Funktion til at generere anbefalinger
def generate_recommendations(cv_text):
    prompt = f"Analyser følgende CV: {cv_text}\nHvilke jobmuligheder og kurser passer til dette CV? Returner resultaterne som en liste."
    response = openai.Completion.create(
        engine="text-davinci-003",
        prompt=prompt,
        max_tokens=300
    )
    return response.choices[0].text.strip()

# Upload CV
uploaded_file = st.file_uploader("Upload dit CV (PDF eller DOCX)", type=["pdf", "docx"])

if uploaded_file:
    st.success("CV uploadet!")
    if st.button("Analyser CV"):
        with st.spinner("Analyserer..."):
            cv_text = process_cv(uploaded_file)
            if cv_text:
                st.write("Analyseret CV-tekst:")
                st.write(cv_text[:1000] + "...")  # Viser en kort version af CV'et
                recommendations = generate_recommendations(cv_text)
                st.write("Anbefalinger:")
                st.write(recommendations)
            else:
                st.error("Kunne ikke analysere CV'et. Prøv venligst med et andet format.")
