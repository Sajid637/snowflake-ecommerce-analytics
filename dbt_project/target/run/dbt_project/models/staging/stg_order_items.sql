
  create or replace   view CURATED_DB.STAGING_STAGING.stg_order_items
  
  
  
  
  as (
    with source as (
    select * from RAW_DB.ECOMMERCE.RAW_ORDER_ITEMS
),
renamed as (
    select
        order_id,
        order_item_id,
        product_id,
        seller_id,
        shipping_limit_date,
        price,
        freight_value,
        price + freight_value     as total_item_value
    from source
)
select * from renamed
  );

