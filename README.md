# Hoyeon Luke Jang - Rough Agent Sketch for Voiceflow Social Automation Agents

This is a **rough design prototype** created to explore how Voiceflow could leverage AI agents to automate a Growth experiment through social outreach. It contains a draft structure of **three LangGraph agents**, written in Python using LangChain and LangGraph, designed to demonstrate AI-first automation across social platforms.

⚠️ **Important Disclaimer**: This project is **not fully functional**. Many functions are placeholders and contain unoptimized prompts or fragile logic. It serves only as a conceptual framework for how multi-agent workflows might look.

---

## 🔧 Overview of Agents

### 1. **Prospect Collection Agent**

Scrapes and stores potential leads by searching keywords on:

- LinkedIn
- Twitter
- Google

**Graph Flow:**

- `create_query` → `search_linkedin`, `search_google`, `search_twitter` → `wait` → `append_to_db`



---

### 2. **Outreach Agent**

Generates and sends a personalized message using Voiceflow’s value props. It includes a basic reflection loop to validate and improve outreach messaging.

**Graph Flow:**

- `check_new_data` → `create_reach_out_message` → `reflection` → `send_message` → `update_db`



---

### 3. **Reply Agent**

Handles responses and generates appropriate follow-ups, again including a reflection step for quality.

**Graph Flow:**

- `check_response` → `create_reply` → `reflection` → `send_message`



---

## 📁 Folder Structure

```
constants/                  # Folder that contains constants used throughout the project
agents/                     # Contains all AI agents (replacing the previous 'domains' structure)
├── {agent_name}/
│   ├── dto/                # Structured output schemas and JSON formats
│   ├── edges/              # Defines conditional logic between nodes within the agent
│   ├── nodes/              # Nodes that generate outputs using LLMs
│   ├── prompts/            # Prompt templates used by each agent
│   ├── states/             # Explicitly defines input and output state schemas
│   ├── graph.py            # LangGraph definition of the agent's logic and state transitions
README.md                  # Project documentation
requirements.txt           # List of required dependencies
```

---

## 💡 What This Project Demonstrates

- LangGraph agent structure with modular folders for `dto`, `nodes`, `edges`, `prompts`, and `states`
- Functional prompt injection and graph setup for AI-driven message generation
- A visual overview of how a social automation pipeline might be built using agents

## 🧪 What You Can Do With This Repo

- Install dependencies via `requirements.txt`
- Launch the graph via LangGraph CLI to **inspect agent logic visually**

```bash
pip install -r requirements.txt
langgraph up
```

But again, **the full workflow will not execute without extensive fixes** to logic, data handling, and safety mechanisms.

---

## 🔐 Setup (Optional, if you want to experiment further)

To get everything connected:

- `OPENAI_API_KEY` for AI messaging
- `LANGCHAIN_API_KEY` for LangGraph cloud features
- `TAVILY_API_KEY` for search-related functionality (prospect discovery)
- `CLAUDE_API_KEY` if switching to Claude in `constants/ai_model.py`

These keys should be stored in your `.env` file or directly injected before runtime.

---

## ✍️ Closing Note

This is a **1-hour sketch** to demonstrate proof-of-concept agent structuring and basic prompt design. Many modules are left intentionally incomplete to show where additional business logic would need to be implemented for a robust social automation pipeline.

Feel free to use this as a **starting point** or evaluation reference. All feedback welcome!

