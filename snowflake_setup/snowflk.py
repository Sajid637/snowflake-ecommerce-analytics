# # import snowflake.connector as sf

# # connection = sf.connect(
# #     user='SAJIDABBAS98',
# #     password='Sajidabbas@89110',
# #     account='OBMMPPB-XH72957'
# # )

# # cursor = connection.cursor()
# # cursor.execute("SELECT CURRENT_USER(), CURRENT_ACCOUNT(), CURRENT_ROLE()")
# # result = cursor.fetchone()

# # print("✅ Connected Successfully!")
# # print(f"   User    : {result[0]}")
# # print(f"   Account : {result[1]}")
# # print(f"   Role    : {result[2]}")

# # cursor.close()
# # connection.close()


# import snowflake.connector as sf
# from dotenv import load_dotenv
# import os

# load_dotenv()

# connection = sf.connect(
#     user=os.getenv('SNOWFLAKE_USER'),
#     password=os.getenv('SNOWFLAKE_PASSWORD'),
#     account=os.getenv('SNOWFLAKE_ACCOUNT'),
#     warehouse='LOAD_WH',
#     database='RAW_DB',
#     schema='ECOMMERCE',
#     role='DATA_ENGINEER_ROLE'
# )

# cursor = connection.cursor()

# tables = {

# "RAW_ORDERS": """
#     CREATE TABLE IF NOT EXISTS RAW_ORDERS (
#         order_id                      STRING,
#         customer_id                   STRING,
#         order_status                  STRING,
#         order_purchase_timestamp      TIMESTAMP_NTZ,
#         order_approved_at             TIMESTAMP_NTZ,
#         order_delivered_carrier_date  TIMESTAMP_NTZ,
#         order_delivered_customer_date TIMESTAMP_NTZ,
#         order_estimated_delivery_date TIMESTAMP_NTZ
#     )""",

# "RAW_CUSTOMERS": """
#     CREATE TABLE IF NOT EXISTS RAW_CUSTOMERS (
#         customer_id              STRING,
#         customer_unique_id       STRING,
#         customer_zip_code_prefix STRING,
#         customer_city            STRING,
#         customer_state           STRING
#     )""",

# "RAW_ORDER_ITEMS": """
#     CREATE TABLE IF NOT EXISTS RAW_ORDER_ITEMS (
#         order_id            STRING,
#         order_item_id       NUMBER,
#         product_id          STRING,
#         seller_id           STRING,
#         shipping_limit_date TIMESTAMP_NTZ,
#         price               FLOAT,
#         freight_value       FLOAT
#     )""",

# "RAW_PRODUCTS": """
#     CREATE TABLE IF NOT EXISTS RAW_PRODUCTS (
#         product_id                 STRING,
#         product_category_name      STRING,
#         product_name_lenght        NUMBER,
#         product_description_lenght NUMBER,
#         product_photos_qty         NUMBER,
#         product_weight_g           FLOAT,
#         product_length_cm          FLOAT,
#         product_height_cm          FLOAT,
#         product_width_cm           FLOAT
#     )""",

# "RAW_SELLERS": """
#     CREATE TABLE IF NOT EXISTS RAW_SELLERS (
#         seller_id              STRING,
#         seller_zip_code_prefix STRING,
#         seller_city            STRING,
#         seller_state           STRING
#     )""",

# "RAW_ORDER_PAYMENTS": """
#     CREATE TABLE IF NOT EXISTS RAW_ORDER_PAYMENTS (
#         order_id             STRING,
#         payment_sequential   NUMBER,
#         payment_type         STRING,
#         payment_installments NUMBER,
#         payment_value        FLOAT
#     )""",

# "RAW_ORDER_REVIEWS": """
#     CREATE TABLE IF NOT EXISTS RAW_ORDER_REVIEWS (
#         review_id               STRING,
#         order_id                STRING,
#         review_score            NUMBER,
#         review_comment_title    STRING,
#         review_comment_message  STRING,
#         review_creation_date    TIMESTAMP_NTZ,
#         review_answer_timestamp TIMESTAMP_NTZ
#     )"""
# }

# print("\n🚀 Creating RAW tables in Snowflake...\n")

# for table_name, ddl in tables.items():
#     try:
#         cursor.execute(ddl)
#         print(f"   ✅ {table_name} created successfully")
#     except Exception as e:
#         print(f"   ❌ {table_name} failed: {e}")

# # Verify all tables exist
# print("\n📊 Verifying tables...\n")
# cursor.execute("SHOW TABLES IN SCHEMA RAW_DB.ECOMMERCE")
# rows = cursor.fetchall()
# for row in rows:
#     print(f"   📁 {row[1]}")

# print("\n🎉 All RAW tables ready!")

# cursor.close()
# connection.close()



import snowflake.connector as sf

conn = sf.connect(
    user='SAJIDABBAS98',
    password='Sajidabbas@89110',
    account='OBMMPPB-XH72957',
    warehouse='TRANSFORM_WH',
    database='CURATED_DB',
    schema='STAGING',
    role='DATA_ENGINEER_ROLE'
)
print('✅ Connected!')
conn.close()