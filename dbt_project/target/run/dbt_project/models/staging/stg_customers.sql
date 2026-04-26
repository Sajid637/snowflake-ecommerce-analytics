
  create or replace   view CURATED_DB.STAGING_STAGING.stg_customers
  
  
  
  
  as (
    with source as (
    select * from RAW_DB.ECOMMERCE.RAW_CUSTOMERS
),
renamed as (
    select
        customer_id,
        customer_unique_id,
        customer_zip_code_prefix  as zip_code,
        customer_city             as city,
        customer_state            as state
    from source
)
select * from renamed
  );

