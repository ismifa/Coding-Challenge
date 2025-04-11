select * from (
  select a.contest_id, hacker_id, name,
      sum(ifnull(total_submissions,0)) as ts, sum(ifnull(total_accepted_submissions,0)) as tas,
      sum(ifnull(total_views,0)) as tv, sum(ifnull(total_unique_views,0)) as tuv
  from contests a
  join colleges b on a.contest_id = b.contest_id
  join challenges c on b.college_id = c.college_id
  left join (
      select challenge_id, sum(total_views) as total_views, sum(total_unique_views) as total_unique_views
      from view_stats
      group by 1
  ) d on c.challenge_id = d.challenge_id
  left join (
      select challenge_id, sum(total_submissions) as total_submissions, sum(total_accepted_submissions) as total_accepted_submissions
      from submission_stats
      group by 1
  ) e on c.challenge_id = e.challenge_id
  group by 1,2,3
) subquery
where ts+tas+tv+tuv > 0
order by 1
;
