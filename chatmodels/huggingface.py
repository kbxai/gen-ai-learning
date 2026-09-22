import streamlit as st
from langchain_huggingface import ChatHuggingFace, HuggingFaceEndpoint
from dotenv import load_dotenv
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage

load_dotenv()

st.set_page_config(page_title="Funny AI Chatbot", page_icon="🤖")
st.title("🤖 Funny AI Chatbot")

@st.cache_resource
def get_model():
    llm = HuggingFaceEndpoint(
        repo_id="deepseek-ai/DeepSeek-R1-Distill-Qwen-7B"
    )
    return ChatHuggingFace(llm=llm)

model = get_model()


if "messages" not in st.session_state:
    st.session_state.messages = [
        SystemMessage(content="You are a funny AI assistant that responds to user queries in a humorous way.")
    ]

# Render existing conversation (skip the SystemMessage)
for msg in st.session_state.messages:
    if isinstance(msg, HumanMessage):
        with st.chat_message("user"):
            st.markdown(msg.content)
    elif isinstance(msg, AIMessage):
        with st.chat_message("assistant"):
            st.markdown(msg.content)

prompt = st.chat_input("You:")

if prompt:
    st.session_state.messages.append(HumanMessage(content=prompt))
    with st.chat_message("user"):
        st.markdown(prompt)

    response = model.invoke(st.session_state.messages)
    st.session_state.messages.append(AIMessage(content=response.content))

    with st.chat_message("assistant"):
        st.markdown(response.content)
