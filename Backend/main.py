from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from dotenv import load_dotenv
from langchain_groq import ChatGroq
from langchain_core.prompts import ChatPromptTemplate
import os
import uvicorn
from fastapi.middleware.cors import CORSMiddleware

# Load environment variables from .env file
load_dotenv()
os.environ["GROQ_API_KEY"] = os.getenv("API_KEY")

# Initialize FastAPI app
app = FastAPI()
app.add_middleware(
    CORSMiddleware,
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
    allow_origins=["*"],  # Adjust this to your needs
)

# Define request schema 
class QueryInput(BaseModel):
    query: str

# Prepare prompt and LLM chain 
prompt = ChatPromptTemplate.from_messages([
    ("system", "You are a helpful chatbot that answers the user query. If you don't know the answer, say 'I don't know'."),
    ("human", "{input}"),
])


# Initialize the LLM with Groq API key
llm = ChatGroq(
    model="gemma2-9b-it",
    temperature=0,
    max_tokens=None,
    timeout=None,
    max_retries=2,
)

chain = prompt | llm


@app.get("/")
async def root():
    return {"message": "Welcome to the Chat API!"}

# Define route
@app.post("/chat")
async def get_chat_response(user_input: QueryInput):
    try:
        result = chain.invoke({"input": user_input.query})
        return {"response": result.content}
    except Exception as e:
        print(f"Error: {e}")
        raise HTTPException(status_code=500, detail=str(e))
    
    


# Entry point
if __name__ == "__main__":
    uvicorn.run("main:app", host="0.0.0.0", port=8000, reload=True)




