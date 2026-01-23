# 🤖 Autonomous B2B Sales Agent (AI Powered)

This agent acts as an autonomous **Sales Development Representative (SDR)**. It conducts real-time web research on target companies and drafts hyper-personalized cold emails using the latest **Google Gemini 2.0 Flash** model.

## 🚀 Features
* **Real-Time Grounding:** Uses Google Search to find the absolute latest news about a prospect (e.g., recent product launches, funding rounds).
* **Pain Point Identification:** Analyzes the company's business model to suggest relevant automation solutions.
* **Dynamic Copywriting:** drafts non-generic, high-converting emails referencing specific news found during research.

## 🛠️ Tech Stack
* **Python 3.14**
* **Google GenAI SDK** (Latest Version)
* **Model:** Gemini 2.0 Flash / Gemini 1.5 Flash
* **Tools:** Google Search Grounding (Dynamic Retrieval)

## 📋 Example Output
**Input:** "Skroutz.gr"
**Agent Found:** Recent launch of "Skroutz AI Assistant".
**Agent Output:**
> "I saw the recent news about the launch of the Skroutz AI Assistant... While your new AI is optimizing the front-end, we focus on backend automation..."

## 💻 How to Run
1. Clone the repository.
2. Install dependencies:
   ```bash
   pip install google-genai