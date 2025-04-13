import streamlit as st
import pandas as pd
from processors.fedex_processor import process_fedex_data
from db.db_utils import insert_data

def ups_negotiated_page():
    st.title("FedEx Shipments Uploader")

    uploaded_file = st.file_uploader("Upload FedEx CSV", type=["csv"])
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        df = process_fedex_data(df)

        st.subheader("Preview Data")
        st.write(df.head())

        if st.button("Insert FedEx Shipments"):
            insert_data(df)
            st.success("FedEx data inserted successfully!")