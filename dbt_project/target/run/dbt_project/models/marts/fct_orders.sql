
  
    

create or replace transient table CURATED_DB.STAGING_MARTS.fct_orders
    
    
    
    as (with orders as (
    select * from CURATED_DB.STAGING_STAGING.stg_orders
),
order_items as (
    select
        order_id,
        count(order_item_id)                as total_items,
        sum(price)                          as total_price,
        sum(freight_value)                  as total_freight,
        sum(total_item_value)               as total_order_value
    from CURATED_DB.STAGING_STAGING.stg_order_items
    group by order_id
),
payments as (
    select
        order_id,
        sum(payment_value)                  as total_payment,
        count(distinct payment_type)        as payment_methods
    from CURATED_DB.STAGING_STAGING.stg_order_payments
    group by order_id
),
reviews as (
    select
        order_id,
        avg(review_score)                   as avg_review_score
    from CURATED_DB.STAGING_STAGING.stg_order_reviews
    group by order_id
)
select
    o.order_id,
    o.customer_id,
    o.order_status,
    o.ordered_at,
    o.approved_at,
    o.shipped_at,
    o.delivered_at,
    o.estimated_delivery_at,
    oi.total_items,
    oi.total_price,
    oi.total_freight,
    oi.total_order_value,
    p.total_payment,
    p.payment_methods,
    r.avg_review_score,
    datediff('day', o.ordered_at, o.delivered_at) as delivery_days
from orders o
left join order_items oi  on o.order_id = oi.order_id
left join payments p      on o.order_id = p.order_id
left join reviews r       on o.order_id = r.order_id
    )
;


  