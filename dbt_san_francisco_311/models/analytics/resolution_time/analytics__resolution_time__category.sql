-- Write a dbt model that calculates the time in days required to resolve a case, grouped by the category of the case. Use the same format as found in analytics__frequency__category.sql.
{{ config(materialized='table') }}

with source_data as (

    select
        category,
        avg(date_diff( created_date, closed_date,DAY)) as resolution_time
    from {{ ref('main_temporal')}}
    group by 1

)

select *
from source_data