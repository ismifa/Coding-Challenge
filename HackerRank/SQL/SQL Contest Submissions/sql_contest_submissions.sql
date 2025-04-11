select d1.submission_date, unq_hacker, d2.hacker_id, name
from (
    select submission_date, count(distinct hacker_id) as unq_hacker
    from (
        select submission_date, hacker_id, 
          row_number() over(partition by hacker_id order by submission_date) as rn1, 
          dense_rank() over(order by submission_date) as rn2
        from (
            select distinct submission_date, hacker_id
            from submissions
        ) d11
    ) d12
    where rn1 = rn2
    group by submission_date
) d1
left join (
    select *
    from (
        select *, row_number() over(partition by submission_date order by total_subs desc, hacker_id asc) as rn 
        from (
            select submission_date, hacker_id, count(*) as total_subs
            from submissions
            group by submission_date, hacker_id
        ) d21
    ) d22
    where rn = 1
) d2 on d1.submission_date = d2.submission_date
left join hackers d3 on d2.hacker_id = d3.hacker_id
order by d1.submission_date
;
