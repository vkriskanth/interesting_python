import sqlglot as sg

databricks_query = "SELECT * FROM Customer LIMIT 10"

#transpiling between different dialects
tsql_query = sg.transpile(databricks_query, read="databricks", write="tsql")[0]
print(tsql_query)

tsql_query = "SELECT TOP 10 * FROM Customer"

print(sg.transpile(tsql_query, read="tsql", write="databricks")[0])

tsql_query = """
-- Get 10 Customers
SELECT TOP 10 * FROM Customer
"""

print(sg.transpile(tsql_query, read="tsql", write="databricks")[0])

#pretty formatting
print(sg.transpile(tsql_query, read="tsql", write="databricks", pretty = True)[0])

sql = """
WITH baz AS (SELECT a, c FROM foo WHERE a = 1) SELECT f.a, b.b, baz.c, CAST("b"."a" AS REAL) d FROM foo f JOIN bar b ON f.a = b.a LEFT JOIN baz ON f.a = baz.a
"""

print(sg.transpile(sql, write="databricks", identify=True, pretty=True)[0])

#getting metadata of the query
# SQL query
sql = """
with cte1 as (
    SELECT a.col1, a.col2, b.col3, b.col4, c.col5
    FROM Table_A a LEFT JOIN Table_B b ON a.id = b.id
)
SELECT *
FROM cte1 LEFT JOIN Table_C c on cte1.col1 = c.col1
"""

# Function to extract table names
parsed = sg.parse_one(sql)

print("I am now displaying the parsed SQL")
print(parsed)

#get list of all tables that are referenced
for table_exp in parsed.find_all(sg.exp.Table):
    print(table_exp)

ctes = set()

for cte in parsed.find_all(sg.exp.CTE):
    ctes.add(cte.alias)

print(ctes)

tables = set()

for table_exp in parsed.find_all(sg.exp.Table):
    table_name = table_exp.text("this")
    if table_name not in ctes:
        tables.add(table_name)

print(tables)

#query optimization
bad_sql = sg.parse_one("""
SELECT *
FROM my_table
WHERE a=1 OR (b=2 OR (c=3 AND d=4))
""")
good_sql = sg.optimizer.optimize(bad_sql)
print(good_sql.sql(pretty=True))

