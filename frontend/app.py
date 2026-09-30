import streamlit as st
import requests

st.set_page_config(page_title="LegalEase AI", page_icon="⚖️")

st.title("⚖️ LegalEase AI")
st.write("Generate professional legal documents using AI.")

document_type = st.selectbox(
    "Document Type",
    ["Rental Agreement", "Employment Contract", "NDA", "Service Agreement"]
)

parties = st.text_area("Parties")
terms = st.text_area("Terms & Conditions")
effective_date = st.date_input("Effective Date")

if st.button("Generate Document"):

    data = {
        "document_type": document_type,
        "parties": parties,
        "terms": terms,
        "effective_date": str(effective_date)
    }

    try:
        response = requests.post(
            "http://127.0.0.1:8000/generate",
            json=data
        )

        if response.status_code == 200:
            st.success("Document Generated Successfully!")
            st.text_area(
                "Generated Document",
                response.json()["document"],
                height=400
            )
        else:
            st.error(response.text)

    except Exception as e:
        st.error(f"Cannot connect to backend: {e}")