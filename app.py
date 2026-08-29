import streamlit as st
import pandas as pd
import numpy as np
import plotly.express as px
import joblib


# ==========================================================
# PAGE CONFIG
# ==========================================================

st.set_page_config(
    page_title="EduPro Analytics",
    page_icon="🎓",
    layout="wide"
)


# ==========================================================
# LOAD DATA
# ==========================================================

@st.cache_data
def load_data():

    master_df = pd.read_csv(
        "EduPro_Master_Dataset.csv"
    )

    instructor_df = pd.read_csv(
        "EduPro_Instructor_Analysis.csv"
    )

    return master_df, instructor_df


@st.cache_resource
def load_model():

    return joblib.load(
        "EduPro_Course_Rating_Model.pkl"
    )


master_df, instructor_df = load_data()

try:
    model = load_model()
except:
    model = None


# ==========================================================
# TITLE
# ==========================================================

st.title("🎓 EduPro Instructor Performance & Course Quality")

st.markdown(
    """
    ### Data-Driven Educational Analytics Platform

    Analyze instructor effectiveness, course quality,
    expertise performance, experience impact and enrollment trends.
    """
)

st.markdown("---")


# ==========================================================
# SIDEBAR
# ==========================================================

st.sidebar.title("🎓 EduPro")

st.sidebar.markdown("### Navigation")

page = st.sidebar.radio(
    "Select Module",
    [
        "Dashboard",
        "Instructor Performance",
        "Course Quality",
        "Experience Analysis",
        "Expertise Analysis",
        "Enrollment Analysis",
        "AI Course Prediction"
    ]
)


# ==========================================================
# FILTERS
# ==========================================================

st.sidebar.markdown("---")

st.sidebar.subheader("🔎 Filters")


expertise_list = sorted(
    master_df["Expertise"]
    .dropna()
    .unique()
)

category_list = sorted(
    master_df["CourseCategory"]
    .dropna()
    .unique()
)

level_list = sorted(
    master_df["CourseLevel"]
    .dropna()
    .unique()
)


selected_expertise = st.sidebar.multiselect(
    "Expertise",
    expertise_list
)

selected_category = st.sidebar.multiselect(
    "Course Category",
    category_list
)

selected_level = st.sidebar.multiselect(
    "Course Level",
    level_list
)


# ==========================================================
# FILTER DATA
# ==========================================================

df = master_df.copy()

if selected_expertise:

    df = df[
        df["Expertise"].isin(
            selected_expertise
        )
    ]

if selected_category:

    df = df[
        df["CourseCategory"].isin(
            selected_category
        )
    ]

if selected_level:

    df = df[
        df["CourseLevel"].isin(
            selected_level
        )
    ]


# ==========================================================
# DASHBOARD
# ==========================================================

if page == "Dashboard":

    st.header("📊 EduPro Dashboard")

    # ---------------- KPI ----------------

    total_instructors = instructor_df[
        "TeacherID"
    ].nunique()

    total_courses = df[
        "CourseID"
    ].nunique()

    total_enrollments = df[
        "TransactionID"
    ].nunique()

    avg_teacher_rating = instructor_df[
        "TeacherRating"
    ].mean()

    avg_course_rating = df[
        "CourseRating"
    ].mean()


    col1, col2, col3, col4, col5 = st.columns(5)

    col1.metric(
        "👨‍🏫 Instructors",
        total_instructors
    )

    col2.metric(
        "📚 Courses",
        total_courses
    )

    col3.metric(
        "👥 Enrollments",
        total_enrollments
    )

    col4.metric(
        "⭐ Teacher Rating",
        f"{avg_teacher_rating:.2f}"
    )

    col5.metric(
        "📖 Course Rating",
        f"{avg_course_rating:.2f}"
    )


    st.markdown("---")


    # ---------------- CATEGORY ----------------

    col1, col2 = st.columns(2)

    with col1:

        category_data = (
            df
            .groupby("CourseCategory")
            ["CourseRating"]
            .mean()
            .reset_index()
            .sort_values(
                "CourseRating",
                ascending=False
            )
        )

        fig = px.bar(
            category_data,
            x="CourseCategory",
            y="CourseRating",
            title="Average Rating by Course Category"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )


    # ---------------- LEVEL ----------------

    with col2:

        level_data = (
            df
            .groupby("CourseLevel")
            ["CourseRating"]
            .mean()
            .reset_index()
        )

        fig = px.bar(
            level_data,
            x="CourseLevel",
            y="CourseRating",
            title="Average Rating by Course Level"
        )

        st.plotly_chart(
            fig,
            use_container_width=True
        )


    # ---------------- DISTRIBUTION ----------------

    fig = px.histogram(
        df,
        x="CourseRating",
        nbins=10,
        title="Course Rating Distribution"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# ==========================================================
# INSTRUCTOR PERFORMANCE
# ==========================================================

elif page == "Instructor Performance":

    st.header(
        "👨‍🏫 Instructor Performance"
    )


    instructor_data = instructor_df.copy()


    if selected_expertise:

        instructor_data = instructor_data[
            instructor_data["Expertise"].isin(
                selected_expertise
            )
        ]


    # ---------------- LEADERBOARD ----------------

    st.subheader(
        "🏆 Instructor Leaderboard"
    )

    leaderboard = instructor_data.sort_values(
        "PerformanceScore",
        ascending=False
    )


    columns = [
        "TeacherName",
        "Expertise",
        "YearsOfExperience",
        "TeacherRating",
        "AverageCourseRating",
        "TotalCourses",
        "TotalEnrollments",
        "PerformanceScore"
    ]


    st.dataframe(
        leaderboard[columns].head(20),
        use_container_width=True,
        hide_index=True
    )


    # ---------------- TOP 10 ----------------

    top10 = leaderboard.head(10)

    fig = px.bar(
        top10,
        x="PerformanceScore",
        y="TeacherName",
        orientation="h",
        title="Top 10 Instructors"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


    # ---------------- RATING RELATIONSHIP ----------------

    fig = px.scatter(
        instructor_data,
        x="TeacherRating",
        y="AverageCourseRating",
        size="TotalEnrollments",
        color="Expertise",
        hover_name="TeacherName",
        title="Teacher Rating vs Course Rating"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# ==========================================================
# COURSE QUALITY
# ==========================================================

elif page == "Course Quality":

    st.header(
        "📚 Course Quality Analysis"
    )


    # ---------------- HEATMAP ----------------

    pivot = df.pivot_table(
        index="CourseCategory",
        columns="CourseLevel",
        values="CourseRating",
        aggfunc="mean"
    )


    fig = px.imshow(
        pivot,
        text_auto=".2f",
        aspect="auto",
        title="Course Rating Heatmap"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


    # ---------------- BOX PLOT ----------------

    fig = px.box(
        df,
        x="CourseCategory",
        y="CourseRating",
        color="CourseLevel",
        title="Course Ratings by Category and Level"
    )

    fig.update_layout(
        xaxis_tickangle=-45
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


    # ---------------- COURSE TABLE ----------------

    course_summary = (
        df
        .groupby(
            [
                "CourseID",
                "CourseName",
                "CourseCategory",
                "CourseLevel"
            ]
        )
        .agg(
            Rating=("CourseRating", "first"),
            Enrollments=("TransactionID", "count")
        )
        .reset_index()
        .sort_values(
            "Rating",
            ascending=False
        )
    )


    st.subheader(
        "📋 Course Performance"
    )

    st.dataframe(
        course_summary,
        use_container_width=True,
        hide_index=True
    )


# ==========================================================
# EXPERIENCE
# ==========================================================

elif page == "Experience Analysis":

    st.header(
        "📈 Experience vs Performance"
    )


    # ---------------- EXPERIENCE → TEACHER ----------------

    fig = px.scatter(
        instructor_df,
        x="YearsOfExperience",
        y="TeacherRating",
        trendline="ols",
        hover_name="TeacherName",
        title="Experience vs Teacher Rating"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


    # ---------------- EXPERIENCE → COURSE ----------------

    fig = px.scatter(
        instructor_df,
        x="YearsOfExperience",
        y="AverageCourseRating",
        trendline="ols",
        hover_name="TeacherName",
        title="Experience vs Course Rating"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


    # ---------------- CORRELATIONS ----------------

    corr1 = instructor_df[
        "YearsOfExperience"
    ].corr(
        instructor_df["TeacherRating"]
    )

    corr2 = instructor_df[
        "YearsOfExperience"
    ].corr(
        instructor_df["AverageCourseRating"]
    )


    col1, col2 = st.columns(2)

    col1.metric(
        "Experience → Teacher Rating",
        f"{corr1:.3f}"
    )

    col2.metric(
        "Experience → Course Rating",
        f"{corr2:.3f}"
    )


# ==========================================================
# EXPERTISE
# ==========================================================

elif page == "Expertise Analysis":

    st.header(
        "🎯 Expertise Performance"
    )


    expertise_data = (
        instructor_df
        .groupby("Expertise")
        .agg(
            TeacherRating=(
                "TeacherRating",
                "mean"
            ),

            CourseRating=(
                "AverageCourseRating",
                "mean"
            ),

            Enrollments=(
                "TotalEnrollments",
                "sum"
            ),

            Instructors=(
                "TeacherID",
                "nunique"
            )
        )
        .reset_index()
    )


    st.dataframe(
        expertise_data.sort_values(
            "CourseRating",
            ascending=False
        ),
        use_container_width=True,
        hide_index=True
    )


    fig = px.bar(
        expertise_data.sort_values(
            "CourseRating",
            ascending=False
        ),
        x="Expertise",
        y="CourseRating",
        title="Average Course Rating by Expertise"
    )

    fig.update_layout(
        xaxis_tickangle=-45
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


    fig = px.scatter(
        expertise_data,
        x="TeacherRating",
        y="CourseRating",
        size="Enrollments",
        color="Expertise",
        title="Expertise Performance"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


# ==========================================================
# ENROLLMENT
# ==========================================================

elif page == "Enrollment Analysis":

    st.header(
        "🔥 Enrollment Analysis"
    )


    course_enrollment = (
        df
        .groupby(
            [
                "CourseID",
                "CourseName",
                "CourseCategory",
                "CourseLevel"
            ]
        )
        .agg(
            Rating=("CourseRating", "first"),
            Enrollments=("TransactionID", "count")
        )
        .reset_index()
    )


    # ---------------- POPULAR COURSES ----------------

    st.subheader(
        "🔥 Most Popular Courses"
    )


    popular = course_enrollment.sort_values(
        "Enrollments",
        ascending=False
    )


    st.dataframe(
        popular.head(20),
        use_container_width=True,
        hide_index=True
    )


    # ---------------- RATING VS ENROLLMENT ----------------

    fig = px.scatter(
        course_enrollment,
        x="Rating",
        y="Enrollments",
        color="CourseCategory",
        hover_name="CourseName",
        title="Course Rating vs Enrollment"
    )

    st.plotly_chart(
        fig,
        use_container_width=True
    )


    # ---------------- LOW QUALITY HIGH DEMAND ----------------

    median_enrollment = course_enrollment[
        "Enrollments"
    ].median()


    priority = course_enrollment[
        (course_enrollment["Rating"] < 3) &
        (course_enrollment["Enrollments"] >= median_enrollment)
    ]


    st.subheader(
        "⚠️ High-Demand Low-Rated Courses"
    )


    st.dataframe(
        priority.sort_values(
            "Enrollments",
            ascending=False
        ),
        use_container_width=True,
        hide_index=True
    )


# ==========================================================
# AI PREDICTION
# ==========================================================

elif page == "AI Course Prediction":

    st.header(
        "🤖 AI Course Rating Prediction"
    )

    st.write(
        "Predict expected course rating using the trained ML model."
    )


    if model is None:

        st.error(
            "Model file not found."
        )

    else:

        col1, col2 = st.columns(2)


        with col1:

            teacher_rating = st.slider(
                "Teacher Rating",
                1.0,
                5.0,
                4.0,
                0.1
            )


            age = st.number_input(
                "Teacher Age",
                18,
                80,
                35
            )


            experience = st.number_input(
                "Years of Experience",
                0,
                50,
                5
            )


            gender = st.selectbox(
                "Gender",
                sorted(
                    master_df["Gender"]
                    .dropna()
                    .unique()
                )
            )


        with col2:

            expertise = st.selectbox(
                "Expertise",
                expertise_list
            )


            category = st.selectbox(
                "Course Category",
                category_list
            )


            level = st.selectbox(
                "Course Level",
                level_list
            )


        if st.button(
            "🚀 Predict Course Rating"
        ):

            input_data = pd.DataFrame({

                "TeacherRating": [
                    teacher_rating
                ],

                "Age": [
                    age
                ],

                "YearsOfExperience": [
                    experience
                ],

                "Gender": [
                    gender
                ],

                "Expertise": [
                    expertise
                ],

                "CourseCategory": [
                    category
                ],

                "CourseLevel": [
                    level
                ]
            })


            prediction = model.predict(
                input_data
            )[0]


            prediction = np.clip(
                prediction,
                1,
                5
            )


            if prediction >= 4.5:

                quality = "Excellent 🏆"

            elif prediction >= 4:

                quality = "Good ⭐"

            elif prediction >= 3:

                quality = "Average ⚠️"

            else:

                quality = "Needs Improvement ❌"


            st.markdown("---")


            col1, col2 = st.columns(2)


            col1.metric(
                "Predicted Course Rating",
                f"{prediction:.2f} / 5"
            )

            col2.metric(
                "Course Quality",
                quality
            )


            st.progress(
                int(prediction / 5 * 100)
            )


# ==========================================================
# FOOTER
# ==========================================================

st.markdown("---")

st.caption(
    "EduPro | Instructor Performance & Course Quality Evaluation"
)