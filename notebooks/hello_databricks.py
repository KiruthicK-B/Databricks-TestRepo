# Databricks notebook source
# MAGIC %md
# MAGIC # Hello from a Git-folder-synced notebook
# MAGIC
# MAGIC This notebook lives in GitHub (`Databricks-TestRepo`) and gets pulled into a
# MAGIC Databricks workspace as a **Git folder** -- edit here and pull in Databricks,
# MAGIC or edit in Databricks and push back to GitHub. Either direction works.

# COMMAND ----------

print("hello from a notebook synced via a Databricks Git folder")

# COMMAND ----------

# MAGIC %md
# MAGIC ## Try it
# MAGIC Run the cell above once this repo is connected as a Git folder, to see it
# MAGIC execute on real Databricks compute -- same file, now running, not just text.

# COMMAND ----------

# A plain SQL-over-Spark example -- works on any cluster, no catalog setup needed.
df = spark.range(5).toDF("n")
display(df)
