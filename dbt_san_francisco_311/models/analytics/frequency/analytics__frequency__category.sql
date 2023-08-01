{{ config(materialized='table') }}

with source_data as (

    select
        category,
        count(*) as frequency
    from {{ ref('main_temporal')}}
    group by 1

)

select *
from source_data