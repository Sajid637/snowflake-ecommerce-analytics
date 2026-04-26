
  
    

create or replace transient table CURATED_DB.STAGING_MARTS.dim_products
    
    
    
    as (with products as (
    select * from CURATED_DB.STAGING_STAGING.stg_products
)
select
    product_id,
    category_name,
    weight_g,
    length_cm,
    height_cm,
    width_cm,
    photos_qty
from products
    )
;


  