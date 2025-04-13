import psycopg2

def get_connection():
    return psycopg2.connect(
        dbname="3plwinner",
        user="postgres",
        password="root",
        host="localhost",
        port="5432"
    )

def insert_data(df):
    conn = get_connection()
    cursor = conn.cursor()

    insert_query = """
    INSERT INTO shipwise_shipments (
        MarketId, TrackingNumber, PackageId, MasterAccountNumber, Department, CarrierCode, IntCode, CarrierService, 
        ActualWeight, ShippedWeight, DimmedWeight, ShipZone, Customer, ShiptoCity, ShiptoState, ShiptoZip, ShiptoCountry, 
        BaseCharge, TotalCharge, Surcharge,"TrackingURL", MarkupAmount, MarkupPercent, SUR_ResidentialAddress, SUR_FuelSurcharge, 
        SUR_DeliveryArea, SUR_SmartPostFuel, SUR_DeliveryAreaSurcharge, SUR_DeliveryAndReturns, SUR_SurePostDasCharge, 
        SUR_ResidentialDeliverySurcharge, SUR_FedExGroundFuel, SUR_DeliveryAreaSurchargeResidential
    ) VALUES (%s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s, %s)
    ON CONFLICT (TrackingNumber) DO NOTHING;
    """

    for _, row in df.iterrows():
        cursor.execute(insert_query, tuple(row))

    conn.commit()
    cursor.close()
    conn.close()
