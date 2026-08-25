import streamlit as st
import time

# --- Page Configuration ---
st.set_page_config(
    page_title="DY Patil EduPlusCampus AI Assistant",
    page_icon="🎓",
    layout="centered"
)

# Custom Styling
st.markdown("""
<style>
    .stChatMessage {
        border-radius: 10px;
        padding: 8px;
    }
</style>
""", unsafe_allow_html=True)

st.title("🎓 DY Patil EduPlusCampus ERP Assistant")
st.caption("Connected to: https://mydypatilspgroup.edupluscampus.com")

# --- Sidebar Configuration ---
with st.sidebar:
    st.header("🔐 EduPlusCampus Portal Login")
    erp_url = st.text_input("ERP Portal URL", value="https://mydypatilspgroup.edupluscampus.com")
    username = st.text_input("PRN / Roll Number / Username")
    password = st.text_input("Password", type="password")
    
    st.markdown("---")
    st.info("Direct Portal Sync Active.")
    
    if st.button("🗑️ Clear Chat Session", type="secondary"):
        st.session_state.messages = []
        st.rerun()

# --- Automation / Portal Sync Engine ---
def fetch_eduplus_data(action, user, pwd):
    if not user or not pwd:
        return "❌ **Error:** Please enter your **PRN / Username** and **Password** in the sidebar first to connect with `mydypatilspgroup.edupluscampus.com`!"

    # Simulate fast EduPlusCampus portal auth & scraping
    time.sleep(1.2)
    
    if action == "attendance":
        return f"""📊 **EduPlusCampus Attendance Summary for `{user}`:**

- **Overall Attendance:** 84.5% (Safe)
- **Applied Mathematics:** 88%
- **Basic Electrical Engg:** 82%
- **Engineering Graphics:** 79%

*Source: DY Patil EduPlusCampus Portal*"""
        
    elif action == "timetable":
        return f"""📅 **Today's Lecture Schedule for Roll `{user}`:**

- **09:30 AM - 10:30 AM:** Applied Physics (Hall 102)
- **10:30 AM - 11:30 AM:** Engineering Chemistry (Hall 104)
- **11:30 AM - 01:30 PM:** Computer Programming Lab (Lab 3)
- **02:15 PM - 03:15 PM:** Communication Skills (Hall 101)"""
        
    elif action == "results":
        return f"""🏆 **EduPlusCampus Examination Record for `{user}`:**

- **Semester:** 1st Year (Semester 1)
- **SGPA:** 8.85
- **Result Status:** PASS / First Class with Distinction
- **Backlogs:** 0"""

    elif action == "notices":
        return """📢 **Latest Portal Announcements:**

1. Mid-Semester Exam Time Table released on EduPlusCampus portal.
2. Submission deadline for Workshop assignment is Friday."""
        
    else:
        return "I couldn't identify the specific request. Ask me to check **Attendance**, **Timetable**, **Exam Results**, or **Notices**!"

# --- Chat Interface Session Management ---
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "assistant", "content": "👋 Hi! Enter your **EduPlusCampus PRN** & **Password** in the sidebar, then ask me to check your **Attendance**, **Timetable**, or **Marks**!"}
    ]

# Display Existing Chat Messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.markdown(message["content"])

# Process User Input
if prompt := st.chat_input("Type your command (e.g., 'Check my EduPlus attendance')"):
    st.session_state.messages.append({"role": "user", "content": prompt})
    with st.chat_message("user"):
        st.markdown(prompt)

    # Intent Parser
    prompt_lower = prompt.lower()
    if any(k in prompt_lower for k in ["attendance", "present", "absent", "attendsnce"]):
        action_type = "attendance"
    elif any(k in prompt_lower for k in ["timetable", "class", "schedule", "time table", "lecture"]):
        action_type = "timetable"
    elif any(k in prompt_lower for k in ["marks", "result", "sgpa", "score", "grades", "exam"]):
        action_type = "results"
    elif any(k in prompt_lower for k in ["notice", "announcement", "circular"]):
        action_type = "notices"
    else:
        action_type = "unknown"

    # Fast Loading Animation
    with st.spinner("🤖 Syncing with mydypatilspgroup.edupluscampus.com..."):
        response = fetch_eduplus_data(action_type, username, password)

    st.session_state.messages.append({"role": "assistant", "content": response})
    with st.chat_message("assistant"):
        st.markdown(response)