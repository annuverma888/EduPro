Care Transition Efficiency & Placement Outcome Analytics
Project Overview

Care Transition Efficiency & Placement Outcome Analytics is a data analytics project designed to evaluate the efficiency of the Unaccompanied Alien Children (UAC) care and reunification pipeline.

The project analyzes how children move through different stages of the care system:

Apprehension & CBP Custody → Transfer to HHS → HHS Care → Discharge & Sponsor Placement

Instead of focusing only on the number of children in custody, this project focuses on process efficiency, flow balance, backlog pressure, discharge performance, and outcome stability.

Problem Statement

Aggregate custody counts do not provide enough information about how efficiently children move through the care pipeline.

This project attempts to answer questions such as:

How efficiently are children transferred from CBP to HHS?
Are HHS discharges keeping pace with transfers?
When does backlog pressure increase?
Are placement outcomes improving or deteriorating?
Are there periods of prolonged stagnation?
Are transition patterns different on weekdays and weekends?
How stable are discharge outcomes over time?
Project Objectives
Primary Objectives
Measure CBP → HHS transfer efficiency.
Evaluate HHS discharge effectiveness.
Measure overall pipeline throughput.
Identify backlog accumulation periods.
Detect potential bottlenecks.
Analyze placement outcome trends.
Measure outcome stability.
Secondary Objectives
Support faster reunification.
Improve case-management workflows.
Identify periods requiring operational attention.
Provide data-driven insights for process improvement.
Support policy-level decision making.
Care Pipeline

The UAC care pipeline is represented as:

Apprehension
     |
     v
CBP Custody
     |
     | Transfer
     v
HHS Care
     |
     | Discharge
     v
Sponsor Placement / Reunification

The analysis evaluates the flow between these stages using aggregate daily reporting data.

Dataset

The project uses the UAC dataset provided for the analysis.

Dataset Columns
Column	Description
Date	Reporting date
Children apprehended and placed in CBP custody	Daily intake volume
Children in CBP custody	Active CBP care load
Children transferred out of CBP custody	Flow into HHS system
Children in HHS Care	Active HHS care load
Children discharged from HHS Care	Successful exits / sponsor placements
Analytical Methodology

The project follows this workflow:

Dataset
   |
   v
Data Loading
   |
   v
Data Cleaning
   |
   v
Exploratory Data Analysis
   |
   v
Feature Engineering
   |
   v
KPI Calculation
   |
   v
Temporal Analysis
   |
   v
Backlog Detection
   |
   v
Bottleneck Detection
   |
   v
Outcome Stability Analysis
   |
   v
Insights & Recommendations
   |
   v
Streamlit Dashboard
Key Performance Indicators
1. Transfer Efficiency Ratio

The Transfer Efficiency Ratio measures transfers relative to the reported CBP custody population.

Transfer Efficiency Ratio =
Transfers / CBP Custody

Python implementation:

df["transfer_efficiency_ratio"] = (
    df["transferred"] /
    (df["cbp_custody"] + 1e-9)
)

A higher ratio indicates greater transfer activity relative to the reported CBP custody population.

2. Discharge Effectiveness Index

This metric measures discharge activity relative to the reported HHS care population.

Discharge Effectiveness =
Discharges / HHS Care

Python implementation:

df["discharge_effectiveness_index"] = (
    df["discharged"] /
    (df["hhs_care"] + 1e-9)
)

This is an analytical indicator of discharge activity relative to the active HHS care load.

3. Pipeline Throughput Rate

Pipeline throughput measures the relationship between HHS exits and transfers into HHS.

Pipeline Throughput =
Discharges / Transfers

Python implementation:

df["pipeline_throughput_rate"] = (
    df["discharged"] /
    (df["transferred"] + 1e-9)
)

A lower value may indicate that transfers are occurring faster than discharges during the selected period.

4. HHS Net Flow

HHS Net Flow compares transfers with discharges.

HHS Net Flow =
Transfers - Discharges

Python implementation:

df["hhs_net_flow"] = (
    df["transferred"] -
    df["discharged"]
)

Interpretation:

Positive value
    Transfers > Discharges
    Potential flow pressure

Negative value
    Discharges > Transfers
    Potential reduction in flow pressure

Zero
    Transfers = Discharges
5. Cumulative Backlog Pressure

Cumulative backlog pressure is calculated using cumulative net flow.

Cumulative Backlog Pressure =
Cumulative Sum(Transfers - Discharges)

Python implementation:

df["cumulative_backlog_pressure"] = (
    df["hhs_net_flow"].cumsum()
)

This metric is an analytical flow-pressure indicator and should not be interpreted as an exact count of unresolved individual cases.

6. Outcome Stability Score

Outcome stability evaluates the variability of discharge effectiveness over time.

Conceptually:

Lower variability
       |
       v
Higher stability

Higher variability
       |
       v
Lower stability

A 0–100 analytical score can be created from relative variability.

The score is a project-specific analytical indicator and is not an official government KPI.

Exploratory Data Analysis

The Jupyter Notebook performs detailed exploratory data analysis.

Dataset Analysis
Dataset dimensions.
Column names.
Data types.
Date range.
Missing values.
Duplicate records.
Statistical summary.
Numerical Analysis

The project analyzes:

Mean.
Median.
Minimum.
Maximum.
Standard deviation.
Percentiles.
Data Cleaning

The notebook performs:

Date conversion.
Numeric conversion.
Column name normalization.
Missing-value analysis.
Duplicate detection.
Invalid-value detection.
Chronological sorting.
Validation of numerical fields.
Feature Engineering

The project creates the following additional features:

Transfer Efficiency Ratio
Discharge Effectiveness Index
Pipeline Throughput Rate
HHS Net Flow
Cumulative Backlog Pressure
7-Day Transfer Efficiency
7-Day Discharge Effectiveness
7-Day Net Flow
Year
Month
Week
Day Name
Weekend Flag
Temporal Analysis

The project performs analysis at different time levels.

Daily Analysis

Daily analysis includes:

Apprehensions.
CBP custody.
Transfers.
HHS care.
Discharges.
Net flow.
Transfer efficiency.
Discharge effectiveness.
Weekly Rolling Analysis

Seven-day rolling averages are used to reduce daily volatility.

df["transfer_efficiency_7d"] = (
    df["transfer_efficiency_ratio"]
    .rolling(7, min_periods=3)
    .mean()
)

df["discharge_effectiveness_7d"] = (
    df["discharge_effectiveness_index"]
    .rolling(7, min_periods=3)
    .mean()
)

df["net_flow_7d"] = (
    df["hhs_net_flow"]
    .rolling(7, min_periods=3)
    .mean()
)
Monthly Analysis

Monthly summaries are created for:

Total apprehensions.
Total transfers.
Total discharges.
Average CBP custody.
Average HHS care.
Net flow.
Pipeline throughput.
Transfer efficiency.
Discharge effectiveness.

Monthly trends help identify long-term changes in pipeline performance.

Weekday vs Weekend Analysis

The project compares:

Weekdays
vs
Weekends

The comparison includes:

Average transfers.
Average discharges.
Transfer efficiency.
Discharge effectiveness.
Net flow.

The project also analyzes performance by:

Monday
Tuesday
Wednesday
Thursday
Friday
Saturday
Sunday
Backlog Detection

Backlog pressure is analyzed by comparing transfers and discharges.

When:

Transfers > Discharges

the system experiences positive net flow.

When this continues over time, cumulative flow pressure can increase.

The project uses statistical thresholds to identify unusually high-pressure periods.

High Backlog Threshold

The default high-pressure threshold is the 80th percentile of HHS Net Flow.

backlog_threshold = (
    df["hhs_net_flow"].quantile(0.80)
)
Severe Backlog Threshold

The default severe-pressure threshold is the 90th percentile.

severe_backlog_threshold = (
    df["hhs_net_flow"].quantile(0.90)
)
Bottleneck Detection

Potential bottlenecks are identified using multiple indicators.

Low Transfer Efficiency

The bottom 20% of transfer-efficiency observations are flagged.

low_transfer_threshold = (
    df["transfer_efficiency_ratio"]
    .quantile(0.20)
)
Low Discharge Effectiveness

The bottom 20% of discharge-effectiveness observations are flagged.

low_discharge_threshold = (
    df["discharge_effectiveness_index"]
    .quantile(0.20)
)
Alert System

The project creates analytical alert flags:

alert_low_transfer
alert_low_discharge
alert_high_backlog
alert_any

These alerts help identify periods that may require further investigation.

They should not automatically be interpreted as confirmed operational failures.

Visualizations

The project includes the following visualizations:

Care Load
CBP custody over time.
HHS care over time.
Pipeline Flow
Apprehensions.
Transfers.
Discharges.
Efficiency
Transfer efficiency trend.
Discharge effectiveness trend.
Pipeline throughput trend.
Backlog
Daily HHS net flow.
Cumulative backlog pressure.
High-pressure periods.
Temporal Patterns
Weekday vs weekend comparison.
Day-of-week analysis.
Monthly performance.
Stability
Discharge effectiveness.
Rolling discharge effectiveness.
Correlation
Correlation matrix.
Heatmap.
Streamlit Dashboard

The project includes an interactive Streamlit dashboard.

Main application:

app.py

The dashboard provides interactive analysis of the care transition pipeline.

Streamlit Dashboard Features
Executive Dashboard

Displays:

Total Apprehensions
Total Transfers
Total Discharges
Transfer Efficiency
Discharge Effectiveness
Pipeline Throughput
Average Net Flow
Peak CBP Custody
Peak HHS Care
Outcome Stability
Care Pipeline Visualization

The dashboard visualizes:

Apprehension
      ↓
CBP Custody
      ↓
HHS Transfer
      ↓
HHS Care
      ↓
Discharge
      ↓
Sponsor Placement
Transfer Efficiency Panel

Provides:

Daily transfer efficiency.
Rolling transfer efficiency.
Threshold alerts.
Low-efficiency periods.
Discharge Efficiency Panel

Provides:

Daily discharge effectiveness.
Rolling discharge effectiveness.
Monthly discharge trends.
Low-effectiveness periods.
Bottleneck Detection Panel

Displays:

High backlog-pressure periods.
Severe backlog-pressure periods.
Low transfer-efficiency periods.
Low discharge-effectiveness periods.
Outcome Trend Panel

Displays:

Daily trends.
Weekly trends.
Monthly trends.
Weekday/weekend patterns.
Stability indicators.
User Controls

The Streamlit dashboard provides interactive controls.

Date Range

Users can select:

Start Date
End Date

to filter the dataset.

Metric Selection

Users can select:

Transfer Efficiency
Discharge Effectiveness
Pipeline Throughput
HHS Net Flow
Cumulative Backlog Pressure
Threshold Controls

Users can adjust analytical thresholds for identifying potential periods of concern.

Technology Stack
Programming Language

Python

Data Analysis
Pandas
NumPy
Visualization
Matplotlib
Seaborn
Plotly
Dashboard
Streamlit
File Processing
OpenPyXL
Development Environment
Jupyter Notebook
VS Code
Project Structure
Care-Transition-Analytics/
│
├── HHS_Unaccompanied_Alien_Children_Program.csv
│
├── Care_Transition_Analytics.ipynb
│
├── app.py
│
├── requirements.txt
│
├── README.md
│
└── outputs/
    │
    ├── uac_processed_analytics.csv
    ├── uac_kpis.csv
    ├── uac_monthly_summary.csv
    ├── uac_weekday_summary.csv
    ├── uac_alerts.csv
    └── uac_care_transition_analysis.xlsx
Installation
Step 1: Create Virtual Environment

For Windows:

python -m venv venv

Activate the environment:

venv\Scripts\activate
Step 2: Install Dependencies
pip install -r requirements.txt
Running Jupyter Notebook

Start Jupyter Notebook:

jupyter notebook

Open:

Care_Transition_Analytics.ipynb

Run the notebook cells sequentially from beginning to end.

Running Streamlit

Run the following command:

streamlit run app.py

The application will normally be available at:

http://localhost:8501
Output Files
Processed Analytics Dataset
uac_processed_analytics.csv

Contains the cleaned dataset and engineered analytical variables.

KPI Report
uac_kpis.csv

Contains the main performance indicators.

Monthly Summary
uac_monthly_summary.csv

Contains monthly pipeline performance.

Weekday Summary
uac_weekday_summary.csv

Contains weekday and weekend analysis.

Alerts
uac_alerts.csv

Contains records identified by the analytical alert rules.

Excel Report
uac_care_transition_analysis.xlsx

Contains multiple analytical sheets in one workbook.

Expected Insights

The project can identify:

Periods of increased CBP custody.
Periods of increased HHS care.
Changes in transfer activity.
Changes in discharge activity.
Periods where transfers exceed discharges.
Potential backlog-pressure periods.
Low transfer-efficiency periods.
Low discharge-effectiveness periods.
Monthly changes in throughput.
Weekday/weekend differences.
Unstable discharge performance.
Recommendations
1. Monitor Transfer Bottlenecks

Periods of low transfer efficiency should be investigated to determine whether operational constraints may be affecting movement from CBP to HHS.

2. Monitor Discharge Capacity

When transfers consistently exceed discharges, teams can investigate whether additional case-management or placement capacity may be required.

3. Prioritize High-Pressure Periods

Periods with unusually high positive net flow should receive additional operational attention.

4. Monitor Outcome Stability

Sudden changes in discharge effectiveness should be investigated alongside operational and external factors.

5. Analyze Temporal Patterns

Weekday and weekend differences can help identify potential workflow or staffing patterns.

Important Limitations

The dataset contains aggregate reporting information.

It does not contain individual-level information such as:

Individual Case ID
Individual Transfer Timestamp
Individual Discharge Timestamp
Sponsor Matching Timestamp
Individual Case Processing Duration
Individual Placement Waiting Time

Therefore, this project cannot directly calculate:

Individual Transfer Duration
Individual Case Duration
Individual Sponsor Matching Time
Individual Placement Waiting Time

Instead, the project analyzes aggregate flow relationships and operational pressure.

The cumulative backlog-pressure metric should therefore be interpreted as an analytical indicator rather than an exact number of unresolved individual cases.

Data Interpretation

The KPIs created in this project are analytical indicators based on aggregate reporting data.

For example:

Transfers / CBP Custody

does not represent the actual transfer time for an individual child.

Similarly:

Discharges / HHS Care

does not represent the actual placement duration of an individual case.

These metrics are intended to identify trends, flow imbalances, and periods that may require further investigation.

Future Scope

The project can be expanded if more detailed data becomes available.

Potential future improvements include:

Individual-level case tracking.
Transfer timestamps.
HHS admission timestamps.
Discharge timestamps.
Sponsor matching timestamps.
Case processing duration.
Facility-level analysis.
Shelter-level analysis.
Staffing data.
Geographic analysis.
Capacity forecasting.
Predictive backlog forecasting.
Automated anomaly detection.
Real-time monitoring.
Automated alerts.
Machine Learning Extension

With sufficiently detailed historical data, machine-learning models could be developed to predict:

Transfer Delay
Discharge Delay
Backlog Risk
Placement Delay Risk
High-Pressure Periods

Possible algorithms include:

Linear Regression.
Random Forest.
Gradient Boosting.
XGBoost.
LightGBM.
Time-Series Forecasting.
Anomaly Detection.

The current project focuses primarily on descriptive and diagnostic analytics.

Research Paper Structure

The research paper can contain the following sections:

1. Abstract

Summary of the project, methodology, findings, and recommendations.

2. Introduction

Background and importance of efficient care transitions.

3. Problem Statement

Limitations of aggregate custody monitoring.

4. Dataset

Description of the dataset and variables.

5. Methodology

Description of:

Data cleaning.
Feature engineering.
KPI calculation.
Backlog detection.
Temporal analysis.
Outcome stability analysis.
6. Exploratory Data Analysis

Statistical and visual exploration of the dataset.

7. Results

Presentation of:

Transfer efficiency.
Discharge effectiveness.
Pipeline throughput.
Net flow.
Backlog pressure.
Temporal patterns.
Outcome stability.
8. Bottleneck Analysis

Identification of periods requiring additional investigation.

9. Recommendations

Operational and analytical recommendations.

10. Limitations

Discussion of aggregate-data limitations.

11. Future Scope

Potential predictive and real-time analytics extensions.

12. Conclusion

Summary of project findings and contribution.

Project Deliverables

The project consists of:

Jupyter Notebook
Care_Transition_Analytics.ipynb

Contains the complete analytical workflow.

Streamlit Dashboard
app.py

Provides an interactive dashboard.

Requirements
requirements.txt

Contains project dependencies.

Documentation
README.md

Contains project information and usage instructions.

Research Paper

Contains EDA, methodology, findings, insights, recommendations, limitations, and future scope.

Executive Summary

Provides a concise overview for stakeholders.

Expected Benefits

The project provides:

Operational Monitoring

Helps identify periods where inflows and exits become imbalanced.

Bottleneck Identification

Highlights periods requiring deeper operational investigation.

Trend Monitoring

Allows users to understand changes in pipeline performance over time.

Decision Support

Provides data-driven indicators for operational planning.

Interactive Analysis

Allows stakeholders to filter and explore the data through a Streamlit dashboard.

Conclusion

The Care Transition Efficiency & Placement Outcome Analytics project transforms aggregate UAC reporting data into a structured process-efficiency analytics framework.

The project analyzes the movement:

CBP Custody
     ↓
HHS Transfer
     ↓
HHS Care
     ↓
Discharge
     ↓
Sponsor Placement

using key analytical indicators such as:

Transfer Efficiency Ratio
Discharge Effectiveness Index
Pipeline Throughput
HHS Net Flow
Cumulative Backlog Pressure
Outcome Stability Score

The combination of a Jupyter Notebook and Streamlit dashboard provides:

Detailed Data Analysis
        +
Interactive Visualization
        +
Operational Monitoring
        +
Bottleneck Identification

The project is intended to support data-driven understanding of care-transition patterns, identify periods of potential operational pressure, and provide evidence that can inform workflow and policy discussions.

Keywords
UAC Analytics
Care Transition Analytics
CBP to HHS
HHS Care
Sponsor Placement
Reunification
Process Efficiency
Pipeline Analytics
Backlog Detection
Operational Analytics
Outcome Analysis
Data Analytics
Python
Pandas
NumPy
Matplotlib
Seaborn
Plotly
Streamlit
Jupyter Notebook
Government Analytics
Care Management
Placement Analytics
Author

Annu Verma

Care Transition Efficiency & Placement Outcome Analytics

Technology: Python | Pandas | NumPy | Matplotlib | Seaborn | Plotly | Streamlit | Jupyter Notebook
