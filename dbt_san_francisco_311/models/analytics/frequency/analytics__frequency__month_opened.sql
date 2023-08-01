-- Write a dbt model that calculates the frequency of each category in the 311 dataset, selecting from the model main_temporal. The model should have the following columns:
{{ config(materialized='table') }}

with source_data as (

    select
        opened_month_of_year,
        count(*) as frequency
    from {{ ref('main_temporal')}}
    group by 1

)

select *
from source_data