import snowflake.connector as sf
from dotenv import load_dotenv
import os

load_dotenv()

connection = sf.connect(
    user=os.getenv('SNOWFLAKE_USER'),
    password=os.getenv('SNOWFLAKE_PASSWORD'),
    account=os.getenv('SNOWFLAKE_ACCOUNT'),
    warehouse='LOAD_WH',
    database='RAW_DB',
    schema='ECOMMERCE',
    role='DATA_ENGINEER_ROLE'
)

cursor = connection.cursor()

# File → Table mapping
files = {
    "olist_orders_dataset.csv":         "RAW_ORDERS",
    "olist_customers_dataset.csv":      "RAW_CUSTOMERS",
    "olist_order_items_dataset.csv":    "RAW_ORDER_ITEMS",
    "olist_products_dataset.csv":       "RAW_PRODUCTS",
    "olist_sellers_dataset.csv":        "RAW_SELLERS",
    "olist_order_payments_dataset.csv": "RAW_ORDER_PAYMENTS",
    "olist_order_reviews_dataset.csv":  "RAW_ORDER_REVIEWS",
}

DATA_DIR = r"C:\Users\LENOVO\Documents\data\raw"

print("\n🚀 Starting data ingestion...\n")

for filename, table in files.items():
    filepath = os.path.abspath(os.path.join(DATA_DIR, filename))

    if not os.path.exists(filepath):
        print(f"   ⚠️  File not found: {filename} — skipping")
        continue

    print(f"📦 Loading {filename} → {table}")

    try:
        # PUT file into Snowflake internal stage
        put_cmd = f"PUT file://{filepath} @%{table} OVERWRITE=TRUE AUTO_COMPRESS=TRUE"
        cursor.execute(put_cmd)
        print(f"   ✅ PUT complete")

        # COPY INTO table from stage
        copy_cmd = f"""
            COPY INTO {table}
            FROM @%{table}
            FILE_FORMAT = (
                TYPE = 'CSV'
                FIELD_OPTIONALLY_ENCLOSED_BY = '"'
                SKIP_HEADER = 1
                NULL_IF = ('', 'NULL', 'null')
                EMPTY_FIELD_AS_NULL = TRUE
                TIMESTAMP_FORMAT = 'YYYY-MM-DD HH24:MI:SS'
            )
            ON_ERROR = 'CONTINUE'
        """
        cursor.execute(copy_cmd)
        print(f"   ✅ COPY INTO complete\n")

    except Exception as e:
        print(f"   ❌ Failed: {e}\n")

print("🎉 Ingestion complete!")
cursor.close()
connection.close()