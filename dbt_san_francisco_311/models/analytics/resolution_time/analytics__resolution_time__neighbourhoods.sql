-- Using the same format as analytics__frequency__neighbourhoods.sql, write a dbt model that calculates the time in days required to resolve a case, grouped by the neighbourhood of the case.

{{ config(
    materialized='table'
) }}

with source_data as (

    select
        neighborhood,
        avg(date_diff( created_date, closed_date,DAY)) as resolution_time
    from {{ ref('main_temporal')}}
    group by 1
)

select *
from source_data