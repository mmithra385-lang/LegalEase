import streamlit as st
import requests

# Railway Backend URL
BACKEND_URL = "https://legalease-production-48e4.up.railway.app"

st.set_page_config(
    page_title="LegalEase AI",
    page_icon="⚖️"
)

st.title("⚖️ LegalEase AI")
st.write("Generate professional legal documents using AI.")

document_type = st.selectbox(
    "Document Type",
    [
        "Rental Agreement",
        "Employment Contract",
        "NDA",
        "Service Agreement"
    ]
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
            f"{BACKEND_URL}/generate",
            json=data,
            timeout=30
        )

        if response.status_code == 200:
            result = response.json()

            st.success("✅ Document Generated Successfully!")

            st.text_area(
                "Generated Document",
                result["document"],
                height=400
            )

        else:
            st.error(f"Error {response.status_code}")
            st.write(response.text)

    except requests.exceptions.ConnectionError:
        st.error("❌ Cannot connect to Railway Backend.")

    except requests.exceptions.Timeout:
        st.error("❌ Request timed out.")

    except Exception as e:
        st.error(f"❌ {e}")