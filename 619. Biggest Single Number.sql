with table_ as (
    select num from MyNumbers group by num having count(num) = 1

) 

select max(num) as num from table_