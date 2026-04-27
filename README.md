# 🏗️ Snowflake E-Commerce Analytics Platform

An end-to-end data engineering project built on Snowflake, dbt, Python, and GitHub Actions CI/CD.

## 🏛️ Architecture
Raw CSVs → Python Ingestion → Snowflake RAW Layer
→ dbt Transformations → Staging → Marts (Star Schema)
→ GitHub Actions CI/CD (automated testing on every push)
## 🛠️ Tech Stack
- **Snowflake** — Data warehouse (RBAC, Zero-Copy Cloning, Time Travel, Masking)
- **dbt** — Data transformations and testing
- **Python** — Data ingestion and validation
- **GitHub Actions** — CI/CD automation

## 📁 Project Structure
├── snowflake_setup/     # Warehouses, DBs, RBAC, Masking policies
├── ingestion/           # Python scripts to load CSVs into Snowflake
└── dbt_project/
└── models/
├── staging/     # 7 staging views (stg_orders, stg_customers...)
└── marts/       # 4 mart tables (fct_orders, dim_customers...)

## 🔐 Security & Governance
- Role-Based Access Control (RBAC) with 4 role hierarchy
- Dynamic Data Masking on sensitive columns
- Zero-Copy Cloning for DEV/PROD isolation

## 📊 dbt Models
| Layer | Models | Type |

|---|---|---|
| Staging | stg_orders, stg_customers, stg_products, stg_sellers, stg_order_items, stg_order_payments, stg_order_reviews | Views |
| Marts | fct_orders, dim_customers, dim_products, dim_sellers | Tables |

## ✅ dbt Tests
- 13 automated tests (not_null, unique, relationships)
- All tests run automatically via GitHub Actions on every push

## 🚀 CI/CD Pipeline
Every push to `main` automatically:
1. Installs dbt
2. Connects to Snowflake
3. Runs `dbt run` — builds all models
4. Runs `dbt test` — validates data quality

## 📦 Dataset
Brazilian E-Commerce dataset by Olist (100K+ orders)
Source: https://www.kaggle.com/datasets/olistbr/brazilian-ecommerce


## 📊 Power BI Dashboard

### Page 1 — Sales Overview
<img width="857" height="486" alt="image" src="https://github.com/user-attachments/assets/4fdb2413-08ce-45bb-b754-5fb5393b104b" />


### Page 2 — Customer Analysis  
<img width="876" height="484" alt="image" src="https://github.com/user-attachments/assets/4a3897b3-feb5-4e78-b813-c8d316671324" />


### Page 3 — Product Performance
![Product Performance]
<img width="862" height="529" alt="image" src="https://github.com/user-attachments/assets/fa476a71-6f9c-4d3a-89b2-8298deddbe6d" />

