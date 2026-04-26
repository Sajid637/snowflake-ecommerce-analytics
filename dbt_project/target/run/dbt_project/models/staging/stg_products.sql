
  create or replace   view CURATED_DB.STAGING_STAGING.stg_products
  
  
  
  
  as (
    with source as (
    select * from RAW_DB.ECOMMERCE.RAW_PRODUCTS
),
renamed as (
    select
        product_id,
        product_category_name     as category_name,
        product_weight_g          as weight_g,
        product_length_cm         as length_cm,
        product_height_cm         as height_cm,
        product_width_cm          as width_cm,
        product_photos_qty        as photos_qty
    from source
)
select * from renamed
  );

