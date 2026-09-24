import streamlit as st
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

load_dotenv()

st.set_page_config(page_title="AI Chatbot", page_icon="🤖")
st.title("🤖 AI Chatbot")


@st.cache_resource
def get_model():
    llm = HuggingFaceEndpoint(
        repo_id="deepseek-ai/DeepSeek-R1-Distill-Qwen-7B"
    )
    return ChatHuggingFace(llm=llm)


model = get_model()

# ---- Sidebar controls ----
with st.sidebar:
    st.subheader("Settings")
    personality = st.radio(
        "Choose your chatbot personality:",
        ("Funny", "Sad", "Angry"),
        index=0,
        key="personality_radio"
    )
    reset_clicked = st.button("🔄 Reset Chat")


def make_system_message(p: str) -> SystemMessage:
    return SystemMessage(
        content=f"You are a {p.lower()} AI assistant that responds to user queries in a {p.lower()} way."
    )


# ---- Session state init ----
if "messages" not in st.session_state:
    st.session_state.messages = [make_system_message(personality)]
    st.session_state.last_personality = personality

# ---- Handle reset button ----
if reset_clicked:
    st.session_state.messages = [make_system_message(personality)]
    st.session_state.last_personality = personality
    st.rerun()

# ---- Handle personality change mid-chat ----
# Old replies were generated under the old personality, so mixing them with a
# new system prompt gives inconsistent behavior. Starting a fresh chat on
# switch keeps the bot's personality correct and consistent.
if personality != st.session_state.last_personality:
    st.session_state.messages = [make_system_message(personality)]
    st.session_state.last_personality = personality
    st.rerun()
