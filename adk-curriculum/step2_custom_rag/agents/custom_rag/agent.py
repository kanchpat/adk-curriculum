import os
from google.adk.agents import LlmAgent

# 1. Define a standard Python function tool
def read_current_document(provided_document: str = None) -> str:
    """Reads the local course_syllabus.txt document or returns provided_document text.
    
    Args:
        provided_document: Optional text string provided by user/client to override local files.
    """
    if provided_document:
         return provided_document

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
        "to pull text. If the user provided content over the prompt or dashboard "
        "manual entry stream, pass it to the tool argument. Otherwise, run the "
        "tool with no args to pull the local syllabus file file. Answer questions "
        "referencing only that file text."
    ),
    tools=[read_current_document]
)
