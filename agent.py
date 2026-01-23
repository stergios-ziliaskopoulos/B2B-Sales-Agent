import os
from google import genai
from google.genai import types


# SECURITY: We use os.environ to load the key safely, or a placeholder for the demo.
# Users should set 'GOOGLE_API_KEY' in their environment variables.
API_KEY = os.environ.get("GOOGLE_API_KEY", "YOUR_API_KEY_HERE")

# Initialize the Google GenAI Client
client = genai.Client(api_key=API_KEY)

def research_and_write_email(company_name):
    """
    Uses Google Search Grounding to research a target company 
    and generates a hyper-personalized B2B sales email.
    """
    print(f"🤖 Agent starting research for: {company_name}...")
    
    # Define the System Instruction & Task
    # We instruct the model to act as an SDR (Sales Development Rep)
    prompt = f"""
    You are an expert B2B Sales Representative.
    
    TASK:
    1. Search Google for the latest news regarding: "{company_name}".
    2. Write a short, professional cold email pitching "AI Automation Services".
    3. Crucial: The email MUST specifically reference the recent news/events you found to prove research was done.
    
    TONE: Professional, concise, and value-driven.
    """
    
    try:
        # Generate content using the Gemini model
        # We use 'gemini-flash-latest' for optimal speed and cost-efficiency
        response = client.models.generate_content(
            model='gemini-flash-latest',
            contents=prompt,
            config=types.GenerateContentConfig(
                # Enable Google Search Grounding (Dynamic Retrieval)
                tools=[types.Tool(google_search=types.GoogleSearch())],
                response_modalities=["TEXT"]
            )
        )
        
        # Verify if Grounding (Search) was actually used
        if response.candidates[0].grounding_metadata.search_entry_point:
             print("✅ Google Search Success: Real-time data retrieved.")
             
        return response.text

    except Exception as e:
        return f"❌ Error during execution: {e}"

# --- MAIN EXECUTION ---
if __name__ == "__main__":
    # Define the target company for the demo
    target_company = "Skroutz.gr"
    
    # Run the agent
    email_draft = research_and_write_email(target_company)
    
    # Display the result
    print("\n" + "="*50)
    print(f"📧 GENERATED EMAIL DRAFT FOR: {target_company}")
    print("="*50 + "\n")
    print(email_draft)