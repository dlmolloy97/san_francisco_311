{{ config(materialized='table') }}

with source_data as (

    select
        source,
        count(*) as frequency
    from {{ ref('main_temporal')}}
    group by 1

)

select *
from source_data