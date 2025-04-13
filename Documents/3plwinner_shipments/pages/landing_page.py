import streamlit as st

def landing_page():
    st.title("📦 Welcome to the Shipment Uploader App")
    st.markdown("""
    ### How to Use This App

    1. **Prepare Your Report**  
       Export your carrier report (UPS, FedEx, DHL, or UPS Negotiated) as a **CSV file**.
       
    2. **Select the Carrier Page**  
       Use the sidebar to select the correct report type.
       
    3. **Upload and Preview**  
       Upload your CSV and review the data after processing.

    4. **Insert into Database**  
       If everything looks good, click **Insert** to add it to the PostgreSQL database.

    ### Notes:
    - The data must include required fields like `TrackingNumber`, `TotalCharge`, etc.
    - Duplicate `TrackingNumber` entries will be skipped automatically.
    - Each carrier report may have a different format. Be sure to upload them to the correct page.

    ---
    """)
    st.info("Use the sidebar on the left to get started 🚀")
