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

tables = {
    "RAW_ORDERS":         "order_id",
    "RAW_CUSTOMERS":      "customer_id",
    "RAW_ORDER_ITEMS":    "order_id",
    "RAW_PRODUCTS":       "product_id",
    "RAW_SELLERS":        "seller_id",
    "RAW_ORDER_PAYMENTS": "order_id",
    "RAW_ORDER_REVIEWS":  "review_id",
}

print("\n📊 Data Validation Report")
print("=" * 55)

all_passed = True

for table, pk_col in tables.items():

    # Row count
    cursor.execute(f"SELECT COUNT(*) FROM {table}")
    row_count = cursor.fetchone()[0]

    # Null check on primary key
    cursor.execute(f"SELECT COUNT(*) FROM {table} WHERE {pk_col} IS NULL")
    null_count = cursor.fetchone()[0]

    # Duplicate check
    cursor.execute(f"""
        SELECT COUNT(*) FROM (
            SELECT {pk_col}, COUNT(*)
            FROM {table}
            GROUP BY {pk_col}
            HAVING COUNT(*) > 1
        )
    """)
    duplicate_count = cursor.fetchone()[0]

    status = "✅ PASS" if row_count > 0 and null_count == 0 else "❌ FAIL"
    if status == "❌ FAIL":
        all_passed = False

    print(f"{status} | {table:<25} | Rows: {row_count:>7} | Nulls: {null_count} | Dupes: {duplicate_count}")

print("=" * 55)
print("✅ All validations passed!" if all_passed else "❌ Some checks failed!")

cursor.close()
connection.close()