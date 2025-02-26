#streamlit
import streamlit as st

# Set page configuration (MUST be the first command)
st.set_page_config(page_title="Growth Mindset Project", page_icon="★")

# Custom CSS for styling
st.markdown("""
    <style>
        /* Background Color */
        .main {
            background-color: #f5f7fa;
        }
        
        /* Header Styles */
        h1, h2 {
            color: #2E86C1;
            font-weight: bold;
            text-align: center;
        }

        /* Text Input and Text Area Styling */
        textarea, input {
            border: 2px solid #2E86C1 !important;
            border-radius: 8px !important;
            padding: 10px !important;
        }

        /* Success and Info Messages */
        .stSuccess {
            background-color: #D4EDDA !important;
            color: #155724 !important;
            border-radius: 8px;
            padding: 10px;
        }

        .stInfo {
            background-color: #D1ECF1 !important;
            color: #0C5460 !important;
            border-radius: 8px;
            padding: 10px;
        }

        .stError {
            background-color: #F8D7DA !important;
            color: #721C24 !important;
            border-radius: 8px;
            padding: 10px;
        }

        /* Footer Styling */
        .footer {
            text-align: center;
            margin-top: 30px;
            font-size: 14px;
            color: #6c757d;
        } 
    </style>
""", unsafe_allow_html=True)

st.title("🌱 Growth Mindset Challenge: Web App with Streamlit")

st.header("🚀 Welcome to Your Growth Mindset Journey!")
st.write("Embrace challenges, learn continuously, and unlock your full potential! 🔑")

# Quote Section
st.header("💡 Inspirational Quote of the Day")
st.write("Believe you can and you're halfway there. - Theodore Roosevelt")

# Challenge Section
st.header("🎯 What's your Challenge Today?")
user_input = st.text_input("Describe a challenge you're facing:")

if user_input:
    st.success(f"💪 You're facing: {user_input}. Push through—great things are ahead! 🌟")
else:
    st.error("Please enter a challenge you're facing.")

# Reflection Section
st.header("🧠 Reflect on Your Challenge")
st.write("What skills or knowledge do you need to overcome this challenge?")
reflection = st.text_area("Write your reflections here:")

if reflection:
    st.success(f"✨ Great Insight! Your reflections: {reflection}. Keep growing!")
else:
    st.info("Reflecting on past experience helps you grow! Share your difficulties.")

# Achievements Section
st.header("🏆 Celebrate Your Achievements!")
achievement = st.text_area("Share something you've recently accomplished:")

if achievement:
    st.success(f"🎊 Congratulations! Your achievement: {achievement}. Keep shining!")
else:
    st.info("Celebrate your small wins to build momentum and confidence! 🥳")

# Footer
st.write("- - -") 
st.markdown('<p class="footer">🌱🚀 Keep believing in yourself. Growth is a journey, not a destination! 🌟<br><br>ⓒ Growth Mindset Project by Nida Iqbal</p>', unsafe_allow_html=True)
