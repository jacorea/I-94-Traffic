import pandas as pd

def process_shipments_data(df):
    df['MarkupAmount'] = df['MarkupTotal'].str.extract(r'([\d.]+)').astype(float)
    df['MarkupPercent'] = df['MarkupTotal'].str.extract(r'(\d+\.?\d*)%').astype(float)
    df['TrackingURL'] = df['TrackingURL'].str.extract(r'=([^=]+)$')

    df[['BaseCharge', 'TotalCharge', 'SurchargeCharge']] = df[[
        'BaseCharge', 'TotalCharge', 'SurchargeCharge'
    ]].replace({'\$': ''}, regex=True).astype(float)

    selected_columns = [
        "MarketId", "TrackingNumber", "PackageId", "MasterAccountNumber", "Department", "CarrierCode", "IntCode", 
        "CarrierService", "ActualWeight", "ShippedWeight", "DimmedWeight", "ShipZone", "Customer", "ShipToCity", 
        "ShipToState", "ShipToZip", "ShipToCountry", "BaseCharge", "TotalCharge", "SurchargeCharge", "TrackingURL", 
        "MarkupAmount", "MarkupPercent", "SUR:ResidentialAddress", "SUR:FuelSurcharge", "SUR:DeliveryArea", 
        "SUR:SmartPost Fuel", "SUR:Delivery Area Surcharge", "SUR:Delivery and Returns", "SUR:Sure Post Das Charge", 
        "SUR:Residential delivery surcharge", "SUR:FedEx Ground Fuel", "SUR:Delivery Area Surcharge Residential"
    ]

    return df[selected_columns]
