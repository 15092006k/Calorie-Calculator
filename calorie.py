import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Karishma Calorie Calculator",
    page_icon="🍎",
    layout="centered"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

.title {
    text-align: center;
    font-size: 40px;
    font-weight: bold;
    color: #2e7d32;
}

.subtitle {
    text-align: center;
    font-size: 18px;
    color: #666;
    margin-bottom: 30px;
}

.result-box {
    background-color: white;
    padding: 25px;
    border-radius: 15px;
    box-shadow: 0px 4px 15px rgba(0,0,0,0.12);
    text-align: center;
}

.calorie {
    font-size: 36px;
    font-weight: bold;
    color: #2e7d32;
}

.info {
    font-size: 18px;
    color: #444;
}

</style>
""", unsafe_allow_html=True)


# ---------------- HEADER ----------------
st.markdown(
    '<div class="title">🍎 Karishma Calorie Calculator</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'Calculate your estimated daily calorie requirement'
    '</div>',
    unsafe_allow_html=True
)


# ---------------- PERSONAL DETAILS ----------------
st.subheader("👤 Personal Details")

col1, col2 = st.columns(2)

with col1:
    age = st.number_input(
        "Age (years)",
        min_value=15,
        max_value=100,
        value=20
    )

with col2:
    gender = st.selectbox(
        "Gender",
        ["Male", "Female"]
    )


# ---------------- BODY DETAILS ----------------
st.subheader("⚖️ Body Details")

col1, col2 = st.columns(2)

with col1:
    weight = st.number_input(
        "Weight (kg)",
        min_value=30.0,
        max_value=250.0,
        value=60.0,
        step=0.5
    )

with col2:
    height = st.number_input(
        "Height (cm)",
        min_value=100.0,
        max_value=250.0,
        value=165.0,
        step=0.5
    )


# ---------------- ACTIVITY LEVEL ----------------
st.subheader("🏃 Activity Level")

activity = st.selectbox(
    "Select your usual activity level",
    [
        "Sedentary - Little or no exercise",
        "Lightly Active - Exercise 1-3 days/week",
        "Moderately Active - Exercise 3-5 days/week",
        "Very Active - Exercise 6-7 days/week",
        "Extra Active - Very hard exercise/physical job"
    ]
)


# ---------------- ACTIVITY MULTIPLIERS ----------------
activity_factors = {
    "Sedentary - Little or no exercise": 1.2,
    "Lightly Active - Exercise 1-3 days/week": 1.375,
    "Moderately Active - Exercise 3-5 days/week": 1.55,
    "Very Active - Exercise 6-7 days/week": 1.725,
    "Extra Active - Very hard exercise/physical job": 1.9
}


# ---------------- CALCULATE BUTTON ----------------
if st.button(
    "🔥 Calculate Calories",
    use_container_width=True
):

    # BMR calculation
    if gender == "Male":
        bmr = (
            10 * weight
            + 6.25 * height
            - 5 * age
            + 5
        )
    else:
        bmr = (
            10 * weight
            + 6.25 * height
            - 5 * age
            - 161
        )

    # Activity multiplier
    activity_factor = activity_factors[activity]

    # TDEE calculation
    daily_calories = bmr * activity_factor


    # ---------------- RESULT ----------------
    st.markdown("---")

    st.subheader("📊 Your Result")

    st.markdown(
        f"""
        <div class="result-box">

        <div class="info">
        Your estimated daily calorie requirement is
        </div>

        <div class="calorie">
        {daily_calories:.0f} kcal/day
        </div>

        </div>
        """,
        unsafe_allow_html=True
    )


    # ---------------- BMR ----------------
    st.markdown("---")

    col1, col2 = st.columns(2)

    with col1:
        st.metric(
            "🔥 BMR",
            f"{bmr:.0f} kcal/day"
        )

    with col2:
        st.metric(
            "⚡ Daily Calories",
            f"{daily_calories:.0f} kcal/day"
        )


    # ---------------- INTERPRETATION ----------------
    st.subheader("💡 Simple Interpretation")

    st.info(
        f"""
        Based on the information you entered, your body is estimated
        to use approximately **{daily_calories:.0f} calories per day**
        at your selected activity level.

        **BMR ({bmr:.0f} kcal/day)** is the estimated energy your body
        needs for basic functions such as breathing and circulation
        while at rest.

        **Daily calorie requirement ({daily_calories:.0f} kcal/day)**
        includes your estimated activity level.
        """
    )


    # ---------------- GENERAL GUIDANCE ----------------
    st.subheader("🍽️ General Guidance")

    st.write(
        "Your calorie requirement is an estimate. Actual energy needs "
        "can vary depending on body composition, activity, health, "
        "and other factors."
    )

    st.warning(
        "⚠️ This calculator is for educational purposes only and "
        "should not be used as a substitute for professional medical "
        "or nutrition advice."
    )


# ---------------- FOOTER ----------------
st.markdown("---")

st.caption(
    "🍎 Karishma Calorie Calculator | Built with Python + Streamlit"
)
