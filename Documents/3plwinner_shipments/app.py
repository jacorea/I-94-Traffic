import streamlit as st
from pages.landing_page import landing_page
from pages.fedex_page import fedex_page
from pages.dhl_page import dhl_page
from pages.shipments_page import shipments_page
from pages.ups_page import ups_page
from pages.ups_negotiated_page import ups_negotiated_page

def main():
    st.sidebar.title("Navigation")
    page = st.sidebar.radio("Choose a Page", ["🏠 Home", "Shipments", "UPS", "FedEx", "DHL", "UPS Negotiated"])

    if page == "🏠 Home":
        landing_page()
    elif page == "Shipments":
        shipments_page()
    elif page == "UPS":
        ups_page()
    elif page == "FedEx":
        fedex_page()
    elif page == "DHL":
        dhl_page()
    elif page == "UPS Negotiated":
        ups_negotiated_page()

if __name__ == "__main__":
    main()

# import streamlit as st
# import pandas as pd
# import psycopg2
# import re

# # Database connection setup (Update credentials as needed)
# def get_connection():
#     return psycopg2.connect(
#         dbname="3plwinner",
#         user="postgres",
#         password="root",
#         host="localhost",  # Change if using a cloud DB
#         port="5432"
#     )

# # Function to clean and process data
# def process_data(df):
#     # Extracting MarkupAmount and MarkupPercent
#     # df[['MarkupAmount', 'MarkupPercent']] = df['MarkupTotal'].str.extract(r'([\d\.]+) \((\d+\.\d+)%\)').astype(float)
#     # Split the column into numeric value and percentage
#     df['MarkupAmount'] = df['MarkupTotal'].str.extract(r'([\d.]+)').astype(float)
#     df['MarkupPercent'] = df['MarkupTotal'].str.extract(r'(\d+\.?\d*)%').astype(float)
#     df['TrackingURL'] = df['TrackingURL'].str.extract(r'=([^=]+)$')

#     # Remove $ sign from multiple columns
#     df[['BaseCharge', 'TotalCharge', 'SurchargeCharge']] = df[['BaseCharge', 'TotalCharge', 'SurchargeCharge']].replace({'\$': ''}, regex=True).astype(float)
    
#     # Selecting required columns
#     selected_columns = [
#         "MarketId", "TrackingNumber", "PackageId", "MasterAccountNumber", "Department", "CarrierCode", "IntCode", 
#         "CarrierService", "ActualWeight", "ShippedWeight", "DimmedWeight", "ShipZone", "Customer", "ShipToCity", 
#         "ShipToState", "ShipToZip", "ShipToCountry", "BaseCharge", "TotalCharge", "SurchargeCharge","TrackingURL", "MarkupAmount", "MarkupPercent", 
#         "SUR:ResidentialAddress", "SUR:FuelSurcharge", "SUR:DeliveryArea", "SUR:SmartPost Fuel", "SUR:Delivery Area Surcharge", 
#         "SUR:Delivery and Returns", "SUR:Sure Post Das Charge", "SUR:Residential delivery surcharge", "SUR:FedEx Ground Fuel", 
#         "SUR:Delivery Area Surcharge Residential"
#     ]

    
#     df = df[selected_columns]
#     st.write(df.head())
#     st.write(len(df.columns))
    
#     return df

# # Function to insert data into PostgreSQL
# def insert_data(df):
#     conn = get_connection()
#     cursor = conn.cursor()
    
#     insert_query = """
#     INSERT INTO shipwise_shipments (
#         MarketId, TrackingNumber, PackageId, MasterAccountNumber, Department, CarrierCode, IntCode, CarrierService, 
#         ActualWeight, ShippedWeight, DimmedWeight, ShipZone, Customer, ShiptoCity, ShiptoState, ShiptoZip, ShiptoCountry, 
#         BaseCharge, TotalCharge, Surcharge,"TrackingURL", MarkupAmount, MarkupPercent, SUR_ResidentialAddress, SUR_FuelSurcharge, 
#         SUR_DeliveryArea, SUR_SmartPostFuel, SUR_DeliveryAreaSurcharge, SUR_DeliveryAndReturns, SUR_SurePostDasCharge, 
#         SUR_ResidentialDeliverySurcharge, SUR_FedExGroundFuel, SUR_DeliveryAreaSurchargeResidential
#     ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s,%s)
#     ON CONFLICT (TrackingNumber) DO NOTHING;
#     """
    
#     for _, row in df.iterrows():
#         cursor.execute(insert_query, tuple(row))
    
#     conn.commit()
#     cursor.close()
#     conn.close()

# # Streamlit UI
# def main():
#     st.title("Shipwise Shipments Uploader")
    
#     uploaded_file = st.file_uploader("Upload CSV File", type=["csv"])
#     if uploaded_file:
#         df = pd.read_csv(uploaded_file)
#         df = process_data(df)
        
#         st.subheader("Preview Data")
#         st.write(df.head(50))
        
#         if st.button("Insert Unique Shipments"):
#             insert_data(df)
#             st.success("Data inserted successfully!")

# if __name__ == "__main__":
#     main()
