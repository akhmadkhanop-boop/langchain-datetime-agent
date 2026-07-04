from langchain_groq import ChatGroq
from langchain_core.tools import tool
from langchain.agents import create_agent
from datetime import datetime
from dotenv import load_dotenv  
import os

load_dotenv()

# ===== DATE/TIME TOOLS =====

@tool
def get_current_date() -> str:
     """Returns the current date and time."""
     return datetime.now().strftime("%Y-%m-%d %H:%M")
 
@tool
def get_day_of_week(date: str) -> str:
     """Returns the name of the day (e.g., Monday, Tuesday) for a given date (YYYY-MM-DD)."""
     d = datetime.strptime(date, "%Y-%m-%d")
     return d.strftime("%A")
 
@tool
def calculate_date_difference(date1: str, date2: str) -> int:
     """Calculates the total number of days between two given dates (YYYY-MM-DD)."""
     d1 =  datetime.strptime(date1, "%Y-%m-%d")
     d2 =  datetime.strptime(date2, "%Y-%m-%d")
     difference = abs((d2 - d1).days)
     return difference
 
# ===== AI AGENT SETUP =====

llm = ChatGroq(model="llama-3.3-70b-versatile", api_key=os.getenv("GROQ_API_KEY"))

tools = [get_current_date, get_day_of_week, calculate_date_difference]

agent = create_agent(llm, tools)

# ===== EXECUTION =====

question = "What day of the week was it on 1912-04-15?"

result = agent.invoke({"messages": [("user", question)]})

print("FINAL ANSWER:")
print(result["messages"][-1].content)