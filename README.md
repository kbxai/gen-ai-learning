# Gen AI Learning Repository

Hands-on code snippets and mini-projects built while learning Generative AI concepts using LangChain, Hugging Face, Streamlit, and modern LLM APIs.

## Projects & Learning Modules

- **Environment & Basics**: Setting up LangChain, environment configuration, and version checks.
- **Chat Models (`chatmodels/chat.py`)**: Initializing Groq LLM, invoking prompts, tuning temperature and token limits.
- **Structured Output Extraction (`chatmodels/core.py`)**: Using Pydantic output parsers and ChatPromptTemplate with Gemini to extract structured movie information into a Streamlit UI.
- **Hugging Face Endpoint Chatbot (`chatmodels/huggingface.py`)**: Integrating open-source DeepSeek models via Hugging Face endpoints with a Streamlit chat UI.
- **Full-featured AI Chatbot (`chatmodels/UIChatBot.py`)**: Interactive Streamlit chatbot featuring personality selection (Funny, Sad, Angry), conversation reset, session state history, and loading indicators.
- **Local Models (`chatmodels/localmodel.py`)**: Workspace for running models locally.

## Setup Instructions

1. Install requirements:
```bash
pip install -r requirements.txt
```

2. Configure environment variables:
Create a `.env` file from `.env.example`:
```bash
cp .env.example .env
```
Add your respective API keys (OpenAI, Google, Groq, Mistral, HuggingFace).

3. Run applications:
```bash
streamlit run chatmodels/UIChatBot.py
```
