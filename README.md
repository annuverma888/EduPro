# 🎓 EduPro – Instructor Performance & Course Quality Evaluation

## 📌 Project Overview

EduPro is a data-driven analytics and machine learning project designed to evaluate **instructor performance and course quality** in an online education platform.

The project analyzes instructor experience, teacher ratings, course ratings, expertise areas, course categories, course levels, and enrollment activity to identify high-performing instructors and courses that require improvement.

The goal is to replace subjective instructor evaluation with a structured, data-driven framework.

---

## 🎯 Problem Statement

EduPro currently lacks clarity on:

* Which instructors consistently deliver high-quality courses?
* Does teaching experience translate into better instructor ratings?
* Is instructor quality associated with course quality?
* Which expertise areas consistently deliver better-rated courses?
* Which course categories and levels perform better?
* Are highly rated instructors associated with higher enrollment?
* Which high-demand courses require quality improvement?

---

## 🚀 Project Objectives

1. Analyze instructor performance.
2. Evaluate course quality.
3. Study the relationship between teaching experience and ratings.
4. Compare course quality across categories and levels.
5. Identify high-performing instructors.
6. Analyze expertise-wise performance.
7. Study enrollment patterns.
8. Identify high-demand, low-rated courses.
9. Build a machine learning model for course-rating prediction.
10. Develop an interactive Streamlit dashboard.

---

## 📊 Dataset

The project uses three major datasets/sheets:

### Teachers

| Field             | Description                  |
| ----------------- | ---------------------------- |
| TeacherID         | Unique instructor identifier |
| TeacherName       | Instructor name              |
| Age               | Instructor age               |
| Gender            | Instructor gender            |
| Expertise         | Instructor specialization    |
| YearsOfExperience | Teaching experience          |
| TeacherRating     | Instructor rating            |

### Courses

| Field          | Description              |
| -------------- | ------------------------ |
| CourseID       | Unique course identifier |
| CourseName     | Course name              |
| CourseCategory | Course category          |
| CourseLevel    | Course difficulty level  |
| CourseRating   | Course rating            |

### Transactions

| Field         | Description                   |
| ------------- | ----------------------------- |
| TransactionID | Unique transaction identifier |
| CourseID      | Course identifier             |
| TeacherID     | Instructor identifier         |

---

## 🔗 Data Integration

The datasets are integrated using:

```text
Teachers
   │
   │ TeacherID
   ▼
Transactions
   │
   │ CourseID
   ▼
Courses
```

The final analytical dataset combines instructor, course and enrollment information.

---

## 🔬 Methodology

### 1. Data Collection

Data was obtained from the EduPro dataset containing instructor, course and transaction information.

### 2. Data Cleaning

The following preprocessing activities were performed:

* Missing-value checking
* Duplicate checking
* Data-type validation
* Identifier validation
* Rating validation
* Instructor-course mapping validation

### 3. Data Integration

Teachers, Courses and Transactions were joined using:

* `TeacherID`
* `CourseID`

### 4. Exploratory Data Analysis

EDA was performed to understand:

* Instructor rating distribution
* Course rating distribution
* Teaching experience
* Expertise performance
* Course category performance
* Course level performance
* Enrollment patterns

### 5. Statistical Analysis

Correlation analysis was performed between:

* Years of Experience ↔ Teacher Rating
* Years of Experience ↔ Course Rating
* Teacher Rating ↔ Course Rating
* Teacher Rating ↔ Enrollment
* Performance Score ↔ Enrollment

### 6. Instructor Performance Scoring

A performance score was calculated to compare instructors using factors such as:

* Teacher Rating
* Course Rating
* Course activity
* Enrollment performance

This score was used to create an instructor leaderboard.

### 7. Machine Learning

Machine learning was applied to predict expected course ratings.

The workflow includes:

```text
Raw Data
    ↓
Preprocessing
    ↓
Feature Engineering
    ↓
Train/Test Split
    ↓
Model Training
    ↓
Model Evaluation
    ↓
Best Model Selection
    ↓
Course Rating Prediction
```

---

## 📈 Key Findings

The current analysis produced the following results:

### Highest-Rated Expertise

**Marketing**

Average Course Rating:

```text
3.65
```

### Highest-Rated Course Category

**Marketing**

Average Rating:

```text
3.69
```

### Highest-Rated Course Level

**Intermediate**

Average Rating:

```text
3.34
```

### Experience vs Teacher Rating

Correlation:

```text
0.598
```

This indicates a moderately positive relationship between teaching experience and teacher rating in the analyzed dataset.

### Experience vs Course Rating

Correlation:

```text
-0.057
```

This indicates a very weak linear relationship between teaching experience and course rating.

### Teacher Rating vs Course Rating

Correlation:

```text
0.000
```

The analyzed dataset does not show a measurable linear relationship between these two variables.

### Top-Performing Instructor

**Yolanda Levine**

Performance Score:

```text
81.26
```

---

## 📌 KPIs

The project evaluates the following KPIs:

| KPI                        | Purpose                                                |
| -------------------------- | ------------------------------------------------------ |
| Average Teacher Rating     | Teaching quality benchmark                             |
| Average Course Rating      | Course effectiveness                                   |
| Rating Consistency Index   | Instructor reliability                                 |
| Experience Impact Score    | Impact of teaching experience                          |
| Enrollment Influence Ratio | Relationship between instructor performance and demand |

---

## 🖥️ Streamlit Dashboard

The project includes an interactive Streamlit dashboard.

### Dashboard Modules

#### 📊 Dashboard

Displays:

* Total instructors
* Total courses
* Total enrollments
* Average teacher rating
* Average course rating
* Category performance
* Level performance
* Rating distribution

#### 👨‍🏫 Instructor Performance

Includes:

* Instructor leaderboard
* Top 10 instructors
* Performance scores
* Teacher rating comparison
* Course rating comparison

#### 📚 Course Quality

Includes:

* Course-rating heatmap
* Category analysis
* Course-level analysis
* Course performance table

#### 📈 Experience Analysis

Includes:

* Experience vs teacher rating
* Experience vs course rating
* Correlation analysis

#### 🎯 Expertise Analysis

Includes:

* Expertise-wise course rating
* Expertise-wise instructor rating
* Enrollment comparison

#### 🔥 Enrollment Analysis

Includes:

* Most popular courses
* Rating vs enrollment
* High-demand low-rated courses

#### 🤖 AI Course Prediction

The dashboard allows users to enter instructor and course information and obtain a predicted course rating from the trained machine learning model.

---

## 🔎 Dashboard Filters

Users can filter the analysis using:

* Instructor expertise
* Course category
* Course level

These filters allow stakeholders to investigate specific segments of the EduPro platform.

---

## 🛠️ Technologies Used

### Programming

* Python

### Data Analysis

* Pandas
* NumPy

### Data Visualization

* Plotly
* Matplotlib
* Seaborn

### Machine Learning

* Scikit-learn
* Joblib

### Dashboard

* Streamlit

### Development Environment

* Jupyter Notebook
* VS Code

### Data Storage

* CSV
* Excel

---

## 📁 Project Structure

```text
EduPro_Project/
│
├── EduPro_Analysis.ipynb
├── app.py
├── requirements.txt
├── README.md
│
├── EduPro_Master_Dataset.csv
├── EduPro_Instructor_Analysis.csv
├── EduPro_Course_Rating_Model.pkl
├── EduPro_Feature_Importance.csv
├── EduPro_Model_Comparison.csv
└── EduPro_Final_KPIs.csv
```

---

## ⚙️ Installation

Clone/download the project and open the project directory.

Install the required dependencies:

```bash
pip install -r requirements.txt
```

---

## ▶️ Run the Application

Run the Streamlit application using:

```bash
streamlit run app.py
```

The application will open in your browser.

---

## 📓 Jupyter Notebook

The complete data analysis is available in:

```text
EduPro_Analysis.ipynb
```

The notebook contains:

* Data loading
* Data preprocessing
* Data integration
* EDA
* Statistical analysis
* Instructor performance analysis
* Course quality analysis
* Enrollment analysis
* Machine learning
* Model evaluation
* Final insights

---

## 💡 Business Recommendations

Based on the analysis, EduPro can:

### 1. Recognize High-Performing Instructors

Create recognition or incentive programs for instructors with consistently high performance.

### 2. Improve Low-Rated Courses

Identify courses with low ratings and provide targeted instructional or content-quality interventions.

### 3. Monitor High-Demand Low-Rated Courses

Courses with high enrollment but poor ratings should receive priority quality reviews.

### 4. Develop Instructor Training

Use expertise-wise and performance-wise analysis to identify areas where instructors may benefit from additional training.

### 5. Monitor Course Quality Continuously

Track course ratings and instructor performance regularly rather than relying on one-time evaluations.

### 6. Use Data for Instructor Evaluation

Combine instructor ratings, course quality and enrollment indicators to support objective performance evaluation.

---

## 🔮 Future Scope

Future versions of the project can include:

* Real-time student feedback analysis
* Sentiment analysis of course reviews
* Recommendation systems
* Instructor churn prediction
* Student retention analysis
* Automated instructor improvement recommendations
* Advanced explainable AI
* Real-time analytics
* Cloud deployment
* Role-based dashboards for administrators and instructors

---

## 📌 Limitations

The findings are based on the available EduPro dataset.

Correlation analysis identifies linear association and does not by itself establish causation.

Machine learning performance depends on the quality, size and characteristics of the available dataset.

Enrollment should not automatically be interpreted as a direct measure of instructional quality.

---

## 🏆 Expected Impact

The EduPro analytics framework can help the platform:

* Improve course quality
* Identify high-performing instructors
* Detect quality gaps
* Support instructor development
* Understand enrollment patterns
* Improve data-driven decision making
* Increase platform credibility
* Establish continuous quality monitoring

---

## 👩‍💻 Project

**EduPro – Instructor Performance and Course Quality Evaluation**

A data analytics, machine learning and interactive dashboard project focused on improving instructor effectiveness and course quality through data-driven decision making.
