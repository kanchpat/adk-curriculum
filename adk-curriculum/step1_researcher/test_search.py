from google.adk import tools

print("Items in tools:", dir(tools))

if 'google_search' in dir(tools):
    print("google_search type:", type(tools.google_search))
if 'google_search_tool' in dir(tools):
    print("google_search_tool type:", type(tools.google_search_tool))

try:
    from google.adk.agents import LlmAgent
    # Let's try to initialize using the available object directly
    # To be safe, let's just inspect it first
except Exception as e:
    print(f"Error: {e}")
