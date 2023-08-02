-- Using the same format as analytics__frequency__year_opened.sql, write a dbt model that calculates the time in days required to resolve a case, grouped by the year the case was opened.

{{ config(
    materialized='table'
) }}

with source_data as (

    select
        opened_year,
        avg(date_diff(closed_date, created_date, DAY)) as resolution_time
    from {{ ref('main_temporal')}}
    group by 1
)

select *
from source_data