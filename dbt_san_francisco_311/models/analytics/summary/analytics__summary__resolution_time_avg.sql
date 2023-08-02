-- Using the same format as analytics__frequency__year_opened.sql, write a dbt model that calculates the time in days required to resolve a case, grouped by the year the case was opened.

{{ config(
    materialized='table'
) }}

with source_data as (

    select
        avg(date_diff( created_date, closed_date,DAY)) as resolution_time
    from {{ ref('main_temporal')}}
)

select
    resolution_time
from source_data