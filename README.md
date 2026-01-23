# 🤖 Autonomous B2B Sales Agent (Web App)

An intelligent **AI Sales Development Representative (SDR)** built with **Streamlit** and **Google Gemini 2.0 Flash**. This application performs real-time web research on target companies and generates hyper-personalized cold emails using Google Search Grounding.

## 🚀 Key Features
* **Web Interface (GUI):** User-friendly dashboard built with Streamlit (no code required).
* **Real-Time Research:** Uses **Google Search Grounding** to find the latest news, funding rounds, and product launches.
* **Contextual Copywriting:** Drafts emails that specifically reference the live data found, eliminating "generic" spam.
* **Secure:** API Keys are handled securely via the sidebar or environment variables.

## 🛠️ Tech Stack
* **Frontend:** Streamlit (Python)
* **AI Model:** Google Gemini 2.0 Flash / 1.5 Flash (via `google-genai` SDK)
* **Tools:** Dynamic Google Search Retrieval

## 💻 How to Run Locally

1.  **Clone the repository:**
    ```bash
    git clone [https://github.com/stergios-ziliaskopoulos/B2B-Sales-Agent.git](https://github.com/stergios-ziliaskopoulos/B2B-Sales-Agent.git)
    cd B2B-Sales-Agent
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Run the App:**
    ```bash
    streamlit run app.py
    ```

4.  **Use the Agent:**
    * Open the link provided in the terminal (usually `http://localhost:8501`).
    * Enter your **Google API Key** in the sidebar (Get one at [Google AI Studio](https://aistudio.google.com/)).
    * Type a company name (e.g., "Tesla", "Skroutz") and click **Generate**.

## 📸 Interface Demo
Here is the agent in action via the Streamlit Web Interface:

![App Screenshot](demo.png)
**Input:** "Plaisio.gr"
**Agent Action:** Searches Google -> Finds news about "Plaisio.gr".
**Output Email:**
> "I was impressed to see Plaisio's Group turnover reached €468.7 million in 2023, marking a strong 7.8% increase and continuing your impressive growth trajectory over the past five years...."


---
*Developed by Stergios Ziliaskopoulos - AI Automation Expert*