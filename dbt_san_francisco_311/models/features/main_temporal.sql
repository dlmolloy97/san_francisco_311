{{ config(materialized='table') }}

with source_data as (

    select
        *,
        --Add columns for the day of the week, hour of the day, month of the year and year for both the opened and closed dates
        EXTRACT(DAYOFWEEK FROM created_date) as opened_day_of_week,
        EXTRACT(HOUR FROM created_date) as opened_hour_of_day,
        EXTRACT(MONTH FROM created_date) as opened_month_of_year,
        EXTRACT(YEAR FROM created_date) as opened_year,
        EXTRACT(DAYOFWEEK FROM closed_date) as closed_day_of_week,
        EXTRACT(HOUR FROM closed_date) as closed_hour_of_day,
        EXTRACT(MONTH FROM closed_date) as closed_month_of_year,
        EXTRACT(YEAR FROM closed_date) as closed_year
    from {{ ref('main')}}

)

select *
from source_data
