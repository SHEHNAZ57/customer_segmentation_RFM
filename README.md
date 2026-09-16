# Customer Segmentation using RFM + K-Means

A customer analytics project that combines **RFM (Recency, Frequency, Monetary) analysis** with **K-Means clustering** to identify meaningful customer segments and translate them into business actions.

The project uses the **UCI Online Retail** dataset and includes an interactive **Streamlit dashboard** for customer-level and segment-level analysis.

---

## 1. Project Overview

The goal is to answer a practical business question:

> **How can historical customer purchasing behavior be used to identify distinct customer groups and support targeted marketing decisions?**

The project follows this workflow:

**Online Retail Data → Data Cleaning → RFM Analysis → RFM Scoring → K-Means Clustering → Customer Segments → Business Insights → Streamlit Dashboard**

---

## 2. Dataset

The project uses the **Online Retail** dataset.

The raw dataset contains **541,909 transaction rows** and 8 columns:

- `InvoiceNo`
- `StockCode`
- `Description`
- `Quantity`
- `InvoiceDate`
- `UnitPrice`
- `CustomerID`
- `Country`

The transaction period is approximately **December 2010 to December 2011**.

`InvoiceNo` values beginning with `C` represent cancellations.

---

## 3. Data Cleaning

The cleaning process was designed to create a purchase-based dataset suitable for customer-level RFM analysis.

Key steps included:

- Removed exact duplicate transaction rows.
- Removed transactions without `CustomerID`.
- Removed cancellation/negative-quantity transactions from the purchase dataset.
- Removed zero-quantity transactions.
- Removed negative `UnitPrice` records.
- Investigated zero-price transactions before filtering.
- Retained zero-price lines that belonged to genuine paid invoices.
- Investigated special/non-product descriptions such as postage, manual entries, bank charges and fees rather than automatically deleting them.
- Verified the final purchase dataset with sanity checks.

The final RFM table contains **4,338 customers**.

---

## 4. RFM Analysis

RFM represents three dimensions of customer purchasing behavior:

### Recency

**How recently did the customer purchase?**

Lower recency values indicate more recent activity.

### Frequency

**How often did the customer purchase?**

Frequency is measured as the number of unique invoices associated with the customer.

### Monetary

**How much did the customer spend?**

Monetary value is calculated as:

`Quantity × UnitPrice`

and then summed for each customer.

The final RFM table contains:

- `Recency`
- `Frequency`
- `Monetary`

The reference date is one day after the latest purchase date in the dataset.

---

## 5. RFM Scoring

Each RFM dimension was converted into a score from **1 to 5** using quantile-based scoring.

For Recency:

- Higher score = more recent customer

For Frequency and Monetary:

- Higher score = more frequent / higher-value customer

The combined `RFM_Score` is a **customer profile code**, not a single numerical magnitude.

For example, `555` means the customer received the highest score in all three RFM dimensions.

---

## 6. Rule-Based Baseline

Before clustering, rule-based segments were created as a baseline.

The baseline included:

- **High-Value Engaged**
- **At Risk - High Value**
- **New / Promising**
- **Low-Engagement**
- **Other**

This baseline provides an interpretable reference for comparing the later unsupervised clustering results.

---

## 7. K-Means Clustering

K-Means was applied to the original RFM variables rather than the RFM score codes.

Because customer monetary and frequency values are highly skewed, the preprocessing pipeline was:

**RFM → `log1p` transformation → StandardScaler → K-Means**

Values of **K = 2 through K = 10** were evaluated.

Two main diagnostics were used:

- Elbow / inertia analysis
- Silhouette score

The silhouette results showed that **K=2 had the strongest numerical separation**, while K=3 and K=4 were also examined in detail.

**K=4 was selected for the final business segmentation because it produced four interpretable and actionable customer groups.**

This is a business-oriented modeling decision rather than a claim that K=4 is mathematically optimal.

---

## 8. Final Customer Segments

The final K=4 segmentation contains:

| Segment | Customers | Customer Share | Purchase Value Share |
|---|---:|---:|---:|
| High-Value Engaged | 713 | 16.44% | 64.89% |
| Moderate / Regular | 1,166 | 26.88% | 23.64% |
| Recent / Low-Frequency | 837 | 19.29% | 5.25% |
| Inactive / Low-Value | 1,622 | 37.39% | 6.22% |

### High-Value Engaged

Customers with very recent activity, high purchase frequency and high monetary value.

**Business direction:** retention and relationship-building.

### Moderate / Regular

Customers with moderate recency, regular purchasing behavior and meaningful monetary contribution.

**Business direction:** upselling, cross-selling and loyalty initiatives.

### Recent / Low-Frequency

Customers who have purchased recently but have relatively low purchase frequency.

**Business direction:** encourage repeat purchases and increase engagement.

### Inactive / Low-Value

Customers with relatively high recency and low frequency/monetary contribution.

**Business direction:** use selective reactivation strategies and avoid treating all inactive customers equally.

---

## 9. Key Business Finding

Customer value is highly concentrated.

Approximately:

**16.4% of customers generate 64.9% of total purchase value.**

The High-Value Engaged and Moderate / Regular groups together represent about **43.3% of customers and 88.5% of purchase value**.

This makes customer prioritization important when allocating retention, loyalty and growth efforts.

---

## 10. Interactive Dashboard

The project includes a Streamlit dashboard called **Customer Intelligence**.

The dashboard contains:

### Overview

- Customer and purchase-value KPIs
- Customer value concentration
- Segment performance
- Executive interpretation

### Customers

- Individual customer lookup
- Recency, Frequency and Monetary profile
- RFM score
- Assigned segment
- Customer-level interpretation and suggested action

### Segments

- Segment-level customer counts
- Customer share
- Purchase value share
- RFM characteristics
- Business interpretation

### Insights

- Executive snapshot
- Key findings
- Business priorities
- RFM takeaway
- Analytics notes

---

## 11. Project Structure

```text
customer_segmentation/
│
├── app.py
├── customer_segmentation_RFM.ipynb
├── Online Retail.xlsx
├── final_customer_segments.csv
├── kmeans_model.pkl
├── scaler.pkl
│
└── .streamlit/
    └── config.toml
```

`.ipynb_checkpoints` may also be created automatically by Jupyter.

---

## 12. How to Run

### Install dependencies

The project requires Python with the following main packages:

```bash
pip install pandas numpy scikit-learn matplotlib seaborn openpyxl joblib streamlit altair
```

### Run the Streamlit dashboard

Open Command Prompt in the project folder:

```bash
cd OneDrive\customer_segmentation
```

Then:

```bash
streamlit run app.py
```

The dashboard will open in the browser.

---

## 13. Saved Model Artifacts

The project saves:

### `kmeans_model.pkl`

The trained final K-Means model with **4 clusters**.

### `scaler.pkl`

The fitted `StandardScaler` used after the `log1p` transformation.

The saved model and scaler were reloaded and validated against the final customer dataset. The resulting cluster predictions matched the saved cluster assignments.

---

## 14. Limitations and Assumptions

- The dataset represents historical transactions from 2010–2011, so the customer behavior is not current.
- RFM captures purchase behavior but does not include demographic, product-category, channel or customer-service information.
- Special/non-product transaction descriptions were investigated and retained, meaning Monetary value can include some non-product transaction values.
- Cancellations and negative-quantity transactions were excluded from the purchase-based RFM dataset.
- Quantile scoring is affected by ties and therefore uses ranking before `qcut`.
- K-Means assumes distance-based cluster structure and is sensitive to preprocessing.
- K=4 was selected primarily for business interpretability/actionability after comparing K=2–10, while K=2 produced the highest silhouette score.
- The segmentation is unsupervised; the resulting labels describe behavioral groups and do not automatically prove causal customer behavior.

---

## 15. Technologies Used

- Python
- Pandas
- NumPy
- Scikit-learn
- Matplotlib
- Altair
- Joblib
- Jupyter Notebook
- Streamlit

---

## 16. Project Outcome

This project demonstrates an end-to-end customer analytics workflow:

**Raw transaction data → data quality investigation → RFM feature engineering → behavioral segmentation → model validation → business interpretation → interactive dashboard**

The emphasis is not only on creating clusters, but on turning customer behavior into interpretable business segments and actionable insights.
