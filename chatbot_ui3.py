

import streamlit as st
import requests
import base64

# ------------------ Page Config ------------------
st.set_page_config(
    page_title="🌊FloatChat",
    layout="wide",
    page_icon="🐚"
)

# ------------------ Custom CSS ------------------
st.markdown("""
    <style>
    .stApp {
        background: linear-gradient(180deg, #001F3F, #003566, #001D3D, #000814);
        background-attachment: fixed;
    }
    .main {
        background: rgba(0, 40, 60, 0.75);
        color: #90EE90;  
        font-family: "Trebuchet MS", sans-serif;
        border-radius: 15px;
        padding: 20px;
    }
    h1, h2, h3, h4, h5, h6, label, p, div, span {
        color: #90EE90 !important;
    }
    section[data-testid="stSidebar"] {
        color: black !important;
        background-color: #f0f2f6 !important;
    }
    section[data-testid="stSidebar"] h1, 
    section[data-testid="stSidebar"] h2, 
    section[data-testid="stSidebar"] h3, 
    section[data-testid="stSidebar"] p, 
    section[data-testid="stSidebar"] div {
        color: black !important;
    }
    .stTextInput>div>div>input {
        border-radius: 12px;
        border: 2px solid #00B4D8;
        padding: 10px;
        background-color: rgba(255,255,255,0.95);
        text-align: center;
        color: #003566;
    }
    .stButton>button {
        background-color: #0077B6;
        color: white;
        border-radius: 10px;
        padding: 8px 20px;
        border: none;
    }
    .chat-history {
        background: rgba(0, 0, 0, 0.05);
        border-radius: 12px;
        padding: 10px;
        max-height: 300px;
        overflow-y: auto;
        font-size: 13px;
        color: black;
    }
    </style>
""", unsafe_allow_html=True)

# ------------------ Sidebar ------------------
with st.sidebar:
    st.header("⚙ Settings")
    st.text("Theme: Deep Ocean 🌊")
    st.text("Mode: Chat + Visualization")
    st.markdown("---")

    st.header("💡 Suggested Questions")
    suggestions = [
        "Plot TEMP vs PSAL as a scatter plot",
        "Plot a vertical profile of TEMP vs PRES with inverted depth axis",
        "Plot the mean and ±1 std dev of temperature (TEMP) vs depth (PRES) across all profiles in 2021 for PLATFORM NUMBER 5906440",
        "Show me TS diagram with only good data TEMP_QC=1 and PRES_QC=1",
        "Show nitrate levels daily trend for 2021"
    ]
    for q in suggestions:
        if st.button(q):
            st.session_state["chat_input"] = q

    st.markdown("---")
    st.header("📜 Chat History")
    with st.container():
        st.markdown("<div class='chat-history'>", unsafe_allow_html=True)
        if "chat_history" in st.session_state:
            for sender, msg in st.session_state.chat_history:
                st.markdown(f"{sender.capitalize()}: **{msg}**", unsafe_allow_html=True)
        st.markdown("</div>", unsafe_allow_html=True)

# ------------------ Title ------------------
st.title("🐚FloatChat")
st.markdown("Ask me questions about the *ocean, climate, or data* and I'll reply with text or a visualization!")

# ------------------ Session State ------------------
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

api_url = "http://127.0.0.1:8000/chat"

# ------------------ Display Chat ------------------
st.subheader("💬 Chat Conversation")
for sender, msg in st.session_state.chat_history:
    if sender == "user":
        st.markdown(f"🧑 *You:* {msg}", unsafe_allow_html=True)
    else:
        st.markdown(f"🤖 *OceanBot:* {msg}", unsafe_allow_html=True)

# ------------------ Chat Input ------------------
st.markdown("<br><br>", unsafe_allow_html=True)
st.markdown("<h3 style='text-align: center;'>💬 Ask OceanBot</h3>", unsafe_allow_html=True)

with st.container():
    col1, col2, col3 = st.columns([1,2,1])
    with col2:
        user_message = st.text_input("Type your question here:", key="chat_input")
        if st.button("Send 🌊"):
            if user_message.strip():
                st.session_state.chat_history.append(("user", user_message))
                with st.spinner("Thinking..."):
                    try:
                        res = requests.post(api_url, json={"question": user_message}).json()

                        if res["type"] == "text":
                            st.success("**Answer:** " + res["answer"])
                            st.session_state.chat_history.append(("bot", res["answer"]))

                        elif res["type"] == "visualization":
                            st.success("📊 Generated Visualization")
                            img_data = base64.b64decode(res["image"])
                            st.image(img_data, use_column_width=True)
                            st.session_state.chat_history.append(("bot", "Generated a visualization."))
                            with st.expander("🔍 Show Generated Code"):
                                st.code(res["code"], language="python")

                        elif res["type"] == "error":
                            st.error("⚠️ Error generating plot: " + res["error"])
                            st.code(res["code"], language="python")
                            st.session_state.chat_history.append(("bot", "Error: " + res["error"]))

                    except Exception as e:
                        st.error(f"❌ Request failed: {e}")
                        st.session_state.chat_history.append(("bot", f"Request failed: {e}"))

                st.experimental_rerun()
