with lat_data as(
    select lat_n, row_number() over(order by lat_n) as rn, count(*) over() as total_rows
    from station
)
select round(avg(lat_n),4) as median
from lat_data
where rn in (floor((total_rows+1)/2), ceil((total_rows+1)/2))
;
