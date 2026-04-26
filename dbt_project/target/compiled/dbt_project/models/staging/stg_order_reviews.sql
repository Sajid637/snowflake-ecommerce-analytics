with source as (
    select * from RAW_DB.ECOMMERCE.RAW_ORDER_REVIEWS
),
renamed as (
    select
        review_id,
        order_id,
        review_score,
        review_comment_title      as comment_title,
        review_comment_message    as comment_message,
        review_creation_date      as created_at,
        review_answer_timestamp   as answered_at
    from source
)
select * from renamed