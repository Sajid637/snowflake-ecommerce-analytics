with sellers as (
    select * from CURATED_DB.STAGING_STAGING.stg_sellers
),
seller_stats as (
    select
        seller_id,
        count(distinct order_id)            as total_orders,
        sum(price)                          as total_revenue,
        avg(price)                          as avg_price
    from CURATED_DB.STAGING_STAGING.stg_order_items
    group by seller_id
)
select
    s.seller_id,
    s.city,
    s.state,
    s.zip_code,
    ss.total_orders,
    ss.total_revenue,
    ss.avg_price
from sellers s
left join seller_stats ss on s.seller_id = ss.seller_id