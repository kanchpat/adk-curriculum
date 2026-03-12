# Northeastern University - AI Product Management Course Staging
### 🚀 Generative AI App Development (ADK Curriculum)

This workspace contains reference templates and custom implementation modules demonstrating **Google ADK** and absolute continuous stream processing setups.

---

## 📂 1. Workspace Layout
- `adk-curriculum/` 🌟 
  - `step1_researcher` - Standard Search Execution
  - `custom_rag` - Zero-index long-context file analyzing agent 
  - `bidi-demo` - Continuous Live Bidirectional streaming with Continuous Video Frame Capture

---

## 🛠️ 2. Running Instructions

Make sure your virtual environment is active before starting any processes:
```bash
source .venv/bin/activate
```

### 🔍 **Step 1: Researcher Agent (Web Search)**
*   **Command**:
    ```bash
    cd adk-curriculum/step1_researcher
    adk web ./agents --port 8081
    ```
*   **Sample Prompt**: *"Find the latest trends in Agentic Frameworks and build a comparison matrix."*


### 📂 **Step 3: Custom Context RAG (Zero-Memory)**
Reads directly from a local `.txt` document using normal Python Tooling layers continuous with massive context windows.
*   **Command**:
    ```bash
    cd adk-curriculum/custom_rag
    adk web ./agents --port 8084
    ```
*   **Sample Prompt**: *"What is the grading breakdown structure of the course and when are professor office hours?"*

### 🎙️ **Step 4: BiDi Streaming (Continuous Audio/Video Live API)**
Fully bidirectional multimodal live socket stream.
*   **Command**:
    ```bash
    cd adk-curriculum/bidi-demo/app
    uvicorn main:app --reload --port 8086
    ```
*   **Browser Endpoint**: `http://localhost:8086`
*   **Continuous Testing Sample prompts**:
    *   **Audio**: *"Describe absolute live triggers for Continuous live feeds."*
    *   **Video Continuous**: Click **Camera** ➔ **`▶️ Stream Video`**, and ask over Audio: *"What am I holding up right now?"* or *"Describe what is inside my video panel."*

---

💡 *All workspaces are designed to load and ground flawlessly with standard keys.*

---

## 🔗 3. Important ADK Links
*   **[ADK Documentation](https://github.com/google/adk-docs)**: Official setup and orchestration guides.
*   **[ADK Samples Repository](https://github.com/google/adk-samples)**: Baseline templates. 
    *   💡 *Note: The `bidi-demo` contained in this workspace was adapted directly from this repository to support your Continuous Video Streaming exercises.*
