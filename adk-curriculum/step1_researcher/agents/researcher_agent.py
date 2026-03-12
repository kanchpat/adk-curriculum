import os
from dotenv import load_dotenv

# Load environment variables if helpful
load_dotenv()

from google.adk.agents import LlmAgent
from google.adk.tools import google_search

# 🔍 Step 1: Initialize the Career Researcher
researcher_agent = LlmAgent(
    name="career_researcher",
    model="gemini-2.5-flash", 
    instruction="""
    You are a professional Career & Recruitment Coach.
    Your job is to help users research the current job market.
    
    When a user asks to find job listings:
    1. Use the `google_search` tool to find 3-4 highly relevant, recent vacancies matching their criteria.
    2. Consolidate the results for the student including:
        - Job Title & Company
        - Core Requirements / Tech Stack
        - Relevance (Why you picked this based on their query)
    3. Always conclude with: *"Would you like me to track any of these in your Google Sheet?"* (This sets up our next lesson).
    """,
    tools=[google_search]
)
# No executable code loop here. 
# ADK's CLI or Web framework loads agent instances automatically from the module!
