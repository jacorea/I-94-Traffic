import streamlit as st
import pandas as pd
from processors.dhl_processor import process_dhl_data
from db.db_utils import insert_data

def dhl_page():
    st.title("DHL Shipments Uploader")

    uploaded_file = st.file_uploader("Upload DHL CSV", type=["csv"])
    if uploaded_file:
        df = pd.read_csv(uploaded_file)
        df = process_dhl_data(df)

        st.subheader("Preview Data")
        st.write(df.head())

        if st.button("Insert DHL Shipments"):
            insert_data(df)
            st.success("DHL data inserted successfully!")
