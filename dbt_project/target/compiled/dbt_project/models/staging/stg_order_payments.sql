with source as (
    select * from RAW_DB.ECOMMERCE.RAW_ORDER_PAYMENTS
),
renamed as (
    select
        order_id,
        payment_sequential,
        payment_type,
        payment_installments,
        payment_value
    from source
)
select * from renamed