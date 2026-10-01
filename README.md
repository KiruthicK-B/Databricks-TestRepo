# Databricks-TestRepo

Sandbox repo for testing Databricks **Git folders** (formerly "Repos") -- connecting a GitHub repo directly into a Databricks workspace for live, synced notebook development.

## What's here

- `notebooks/hello_databricks.py` -- a minimal Databricks notebook, in the exact file format Git folders (and Databricks' notebook import/export) expect: a `# Databricks notebook source` header and `# COMMAND ----------` cell separators. Any plain `.py` file with those markers is treated as a multi-cell notebook by Databricks, not a single script.

## Why this exists

Git folders let you edit notebooks from GitHub -- version control, PR review, CI -- while still running them natively on Databricks compute, instead of exporting/importing notebooks by hand between GitHub and the workspace.

## How to connect it

1. Databricks workspace sidebar -> **Workspace** -> navigate to `Shared` (or your own user folder)
2. **Create** -> **Git folder**
3. Paste this repo's URL: `https://github.com/KiruthicK-B/Databricks-TestRepo`
4. Pick `main` branch -> Databricks clones it in

Open `notebooks/hello_databricks.py` inside Databricks afterward -- it renders as a real multi-cell notebook, runnable on any cluster/warehouse, not as flat text.
