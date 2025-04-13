import streamlit as st
import pandas as pd
from processors.shipments_processor import process_shipments_data
from db.db_utils import insert_data

def shipments_page():
    st.title("Shipwise Shipments Uploader")

    uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        df = process_shipments_data(df)

        st.subheader("Preview Data")
        st.write(df.head(50))

        if st.button("Insert Unique Shipments"):
            insert_data(df)
            st.success("Data inserted successfully!")
