import pandas as pd
import streamlit as st

df = pd.read_csv("symptom_treatment_data.csv")

def search_condition(user_input):
    user_input = user_input.lower()
    for _, row in df.iterrows():
        if user_input in row['condition'].lower() or user_input in row['symptoms'].lower():
            return f"""
**🩺 Condition:** {row['condition']}

**🔍 Description:** {row['description']}

**📌 Symptoms:** {row['symptoms']}

**💊 Treatment:** {row['treatment']}

**⏳ Recovery Time:** {row['recovery_time']}

**👨‍⚕️ Specialist:** {row['specialist']}
            """
    return "❌ Sorry, I couldn't find a match. Please try another symptom or condition."

st.set_page_config(page_title="Health Chatbot", page_icon="💊")
st.title("🤖 Symptom to Treatment Chatbot")
st.write("Type a **symptom** or **condition** to get treatment info:")

user_input = st.text_input("Enter symptom or condition")

if user_input:
    result = search_condition(user_input)
    st.markdown(result)
