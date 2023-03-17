1)  at 1:49:00 minute we have something interesting regarding order of paths

2)  serial will auto increment the values in id column by 1
![](2023-03-14-10-16-24.png)
3) this is how we set default values while creating a table
![](2023-03-14-10-19-37.png)
    
4) create a column with timestamp as now()
![](2023-03-14-10-46-48.png)

5) some useful queries
    - `select * from products where inventory >0 and price >20;`
    - `select * from products where inventory >0 or price >20;`
    - `select * from products where id in (1,2,3);`
    - `select * from products where name like 'TV%';`
        - all names with start 'TV'
        - `%e` will match all that end with 'e'
    - `select * from products where name not like '%en%'`
    - `select * from products order by inventory desc ,price`
        - for tie breaker in inventory we use price (price asc is by default)
    - `select * from products order by id limit 5 offset 2`
        - means it will give 5 entries skipping the first two entries (i,e 3-7)
- JWT
    - stored on frontend
    - if credentials are valid, we generated a token
    - so the client a request along with the token in header of request
    - JWT is not encrypted.
    - header+payload+secret => jwt token signing algo (SHA256)
    - ![](2023-03-15-13-22-02.png)

    - https://jwt.io/
    - sample token "eyJhbGciOiJIUzI1NiIsInR5cCI6IkpXVCJ9.eyJ1c2VyX2lkIjoxMSwiZXhwIjoxNjc4ODg5OTMzfQ._INJEAFnLbNvKASGU0ncH4L1B07wq15R7gAeUsezMwA"

    - how to access environment variables on a command line
        - echo %Path$
        ![](2023-03-16-08-40-13.png)

    - note: all the environment variable will come out as string
    - `select post.*,email from posts left join users on posts.owner_id=users.id;`

- middleware is a function that runs before every request