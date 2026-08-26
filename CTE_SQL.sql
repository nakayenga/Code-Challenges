with cte_website_metric as (
    select 
        c.email,
        cast(avg(sm.cpu_usage) as decimal(10,2)) as average_cpu_usage,
        cast(avg(sm.memory_usage) as decimal(10,2)) as average_memory_usage,
        cast(avg(sm.disk_usage) as decimal(10,2)) as average_disk_usage,
        case
            when avg(sm.cpu_usage) > 50.00 
              or avg(sm.memory_usage) > 50.00 
              or avg(sm.disk_usage) > 50.00 then 'Yes'
            else 'No'
        end as one_metric_greater_than_50
    from customers c
    join site_metrics sm on c.id = sm.customer_id
    group by c.email
) 
select
    email,
    average_cpu_usage,
    average_memory_usage,
    average_disk_usage
from cte_website_metric
where one_metric_greater_than_50 = 'Yes'
order by email;
