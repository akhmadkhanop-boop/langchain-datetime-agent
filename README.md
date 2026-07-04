# LangChain Datetime AI Agent 🕰️🤖

An intelligent AI agent built using **LangChain** and **Groq (Llama 3.3)** that can perform mathematical calculations and logical reasoning on dates and time. 

## 🚀 Features
This agent is equipped with custom Python tools that allow it to automatically:
- **Find the Current Date:** Fetch real-time system date and time.
- **Find the Day of the Week:** Tell you the exact day (e.g., Monday, Friday) of any date in history or the future.
- **Calculate Date Differences:** Calculate the exact number of days between two given dates (handling negative inputs automatically).

## 🛠️ Technologies Used
- **Python**
- **LangChain** (`create_agent`, `@tool`)
- **Groq API** (`llama-3.3-70b-versatile`)
- **Datetime Module**

## ⚙️ How to Setup and Run
1. Clone this repository to your local machine.
2. Install the required libraries:
   ```bash
   pip install langchain-groq langchain python-dotenv
