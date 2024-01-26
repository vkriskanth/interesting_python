import duckdb as db

db.sql("CREATE TABLE departments (department varchar, exmployee_count INT, average_salary INT,max_salary INT,min_salary INT)")

db.sql("INSERT INTO departments VALUES ('Sales', 300, 25000,40000,19000), ('HR',50, 22000,50000,18500)");

res = db.sql("SELECT * FROM departments")

print(res)

# exclude the average_salary and employee_count columns
res = db.sql("SELECT department, COLUMNS('m.*salary') FROM departments")

print(res)

res =db.sql("SELECT department, COLUMNS('m.*salary') FROM departments \
       WHERE COLUMNS('m.*salary') >= 19000")

print(res)

res = db.sql("SELECT MAX(COLUMNS('m.*salary')) FROM departments")

print(res)

db.sql("CREATE TABLE purchases (productID int, year INT, sales INT)")

db.sql("INSERT INTO purchases VALUES (12345, 2019, 15000), (12345,2020, 19500), (12345, 2021, 22000), (987654, 2019, 510), (987654,2020, 1900), (987654, 2021, 2100)");

db.sql("SELECT * FROM purchases")

db.sql("create table pivoted_purchases as PIVOT purchases ON year USING SUM(sales)  GROUP BY productID")
res = db.sql("SELECT * FROM pivoted_purchases")

print(res)

res = db.sql("UNPIVOT pivoted_purchases ON COLUMNS(* EXCLUDE productID) INTO NAME year VALUE sales")

print(res)

res = db.sql("SELECT 'I am a string' as col1 union select 100 union select 42.0")

print(res)

res = db.sql("SELECT 'The quick brown fox jumped over the lazy dog' AS my_text,\
substring(my_text, 17,3) AS my_text_substr,\
length(my_text) AS my_text_len,\
my_text_len * my_text_len AS my_text_calc")

print(res)

res = db.sql("SELECT [x*x for x in nums] as squares FROM (VALUES ([1,2,3,4,5,6,7,8,9])) t(nums)")

print(res)

res = db.sql("SELECT ([upper(x[1])||x[2:] for x in \
('the quick brown fox jumped over the lazy dog')\
.string_split(' ')]).list_aggr('string_agg',' ') as final_str")

print(res)

