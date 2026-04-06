# agent_setup.py

from dotenv import load_dotenv
import os

load_dotenv()

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain.agents import initialize_agent, Tool

from tools.expense_tool import add_expense
from tools.job_tool import fetch_jobs

# ✅ LLM setup
llm = ChatGoogleGenerativeAI(
    model="gemini-1.5-flash",
    temperature=0.3,
    google_api_key=os.getenv("GOOGLE_API_KEY")
)

# ✅ Tool wrappers
def expense_tool_wrapper(input_text: str):
    return add_expense(input_text)

def job_tool_wrapper(input_text: str):
    return fetch_jobs()

# ✅ Tools
tools = [
    Tool(
        name="Expense Tracker",
        func=expense_tool_wrapper,
        description="Use this to log expenses. Input example: 'Spent 300 on food'"
    ),
    Tool(
        name="Job Finder",
        func=job_tool_wrapper,
        description="Use this to find recent job postings"
    )
]

# ✅ Agent
agent = initialize_agent(
    tools=tools,
    llm=llm,
    agent="zero-shot-react-description",
    verbose=True
)