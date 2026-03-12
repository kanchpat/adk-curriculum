import os
from google.adk.agents import LlmAgent

# 1. Define a standard Python function tool
def read_current_document() -> str:
    """Reads the contents of the local course_syllabus.txt document."""
    # Build absolute path to data folder relative to this file
    filepath = os.path.abspath(os.path.join(os.path.dirname(__file__), "../../data/course_syllabus.txt"))
    
    try:
        with open(filepath, 'r', encoding='utf-8') as f:
            return f.read()
    except FileNotFoundError:
        return "Error: course_syllabus.txt was not found in the data/ directory."

root_agent = LlmAgent(
    name="custom_rag",
    model="gemini-2.5-flash",
    instruction=(
        "You are a document analyzer. Use the `read_current_document` tool "
        "to pull text from the local syllabus file. Answer ALL questions "
        "by referencing ONLY that file. ALWAYS state that you read it."
    ),
    tools=[read_current_document]
)
