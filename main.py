import os
from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI
from langchain_core.messages import HumanMessage
from langchain_core.callbacks.streaming_stdout import StreamingStdOutCallbackHandler

llm = ChatOpenAI(
    model="mistralai/mistral-7b-instruct:free",  # OpenRouter model name
    base_url="https://openrouter.ai/api/v1",
    api_key=os.getenv("OPENAI_API_KEY"),
    temperature=0.7,
    streaming=True,  # Enable streaming
    callbacks=[StreamingStdOutCallbackHandler()],  # Add callbacks here
)

# Using streaming with the model
response = llm.invoke(
    [HumanMessage(content="Dame una frase ruda en español (Give me a badass phrase in Spanish)")]
)

# Note: When using streaming, the content is already printed by the handler
# but you can still access the complete response if needed
print("\nFull response:", response.content)