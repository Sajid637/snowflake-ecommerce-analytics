with customers as (
    select * from {{ ref('stg_customers') }}
),
orders as (
    select
        customer_id,
        count(order_id)                     as total_orders,
        min(ordered_at)                     as first_order_date,
        max(ordered_at)                     as last_order_date
    from {{ ref('stg_orders') }}
    group by customer_id
)
select
    c.customer_id,
    c.customer_unique_id,
    c.city,
    c.state,
    c.zip_code,
    o.total_orders,
    o.first_order_date,
    o.last_order_date
from customers c
left join orders o on c.customer_id = o.customer_id