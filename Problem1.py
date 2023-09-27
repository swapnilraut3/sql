# Databricks notebook source
# MAGIC %md 
# MAGIC ### SQL Problem:
# MAGIC **Write a query to find the count for New & Repeat Customers for each order date.**  
# MAGIC https://www.linkedin.com/feed/update/urn:li:activity:7112387045758529536/  
# MAGIC The scenario in working with one Table : 'repeat_table'  
# MAGIC The 'repeat_table' includes customer's id, order date and order amount.
# MAGIC
# MAGIC !(/assets/problem1.jpeg)
# MAGIC

# COMMAND ----------

# MAGIC %sql
# MAGIC CREATE TABLE IF NOT EXISTS REPEAT_TABLE(
# MAGIC 	order_id INTEGER,
# MAGIC   customer_id INTEGER,
# MAGIC   order_date DATE,
# MAGIC   order_amount FLOAT
# MAGIC );

# COMMAND ----------

# MAGIC %sql
# MAGIC
# MAGIC INSERT INTO REPEAT_TABLE 
# MAGIC VALUES
# MAGIC (1, 100, '01-01-2022', 2000.0),
# MAGIC (2, 200, '01-01-2022', 2500.0),
# MAGIC (3, 300, '01-01-2022', 2100),
# MAGIC (4, 100, '02-01-2022', 2000),
# MAGIC (5, 400, '02-01-2022', 2200),
# MAGIC (6, 500, '02-01-2022', 2700),
# MAGIC (7, 100, '03-01-2022', 3000),
# MAGIC (8, 400, '03-01-2022', 1000),
# MAGIC (9, 600, '03-01-2022', 3000);

# COMMAND ----------


