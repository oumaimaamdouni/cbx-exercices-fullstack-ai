import streamlit as st
import requests
import json

st.set_page_config(page_title="CV Extractor - CBX Group", layout="centered")

st.title("📄 Extracteur de CV Full Stack AI")
st.info("Uploadez un CV pour extraire automatiquement les informations (Sans IA)")

uploaded_file = st.file_uploader("Choisissez un fichier PDF ou DOCX", type=["pdf", "docx"])

if uploaded_file is not None:
    if st.button("Analyser le CV"):
        with st.spinner("Extraction des données en cours..."):
            files = {"file": (uploaded_file.name, uploaded_file.getvalue())}
            
            try:
                response = requests.post("http://backend:8000/api/v1/upload-cv", files=files)
                
                if response.status_code == 200:
                    st.session_state['cv_data'] = response.json()
                    st.success("Analyse terminée avec succès !")
                else:
                    st.error(f"Erreur du serveur : {response.status_code}")
            except Exception as e:
                st.error(f"Erreur de connexion au Backend : {e}")
if 'cv_data' in st.session_state:
    st.divider()
    st.subheader("📝 Vérification des informations")
    
    data = st.session_state['cv_data']
    
    col1, col2 = st.columns(2)
    
    with col1:
        first_name = st.text_input("Prénom", value=data.get("first_name", ""))
        last_name = st.text_input("Nom", value=data.get("last_name", ""))
        email = st.text_input("Email", value=data.get("email", ""))

    with col2:
        phone = st.text_input("Téléphone", value=data.get("phone", ""))
        degree = st.text_input("Diplôme principal", value=data.get("degree", ""))

    final_json = {
        "first_name": first_name,
        "last_name": last_name,
        "email": email,
        "phone": phone,
        "degree": degree
    }
    
    st.download_button(
        label=" Télécharger le JSON final",
        data=json.dumps(final_json, indent=4, ensure_ascii=False),
        file_name="cv_extrait.json",
        mime="application/json"
    )