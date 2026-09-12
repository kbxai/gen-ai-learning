from dotenv import load_dotenv
from langchain.chat_models import init_chat_model

load_dotenv()

llm = init_chat_model(
    "openai/gpt-oss-20b",
    model_provider="groq",
    temperature=0,
    max_tokens=200
)

response = llm.invoke("write a poem on AI")

print(response.content)
