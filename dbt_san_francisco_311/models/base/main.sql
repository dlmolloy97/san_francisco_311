{{ config(materialized='table') }}

with source_data as (

    select
        *
    from `fluid-skyline-255211.san_francisco_311.311_service_requests`

)

select *
from source_data
