import streamlit as st
import os
from google import genai
from google.genai import types
from fpdf import FPDF

# --- PAGE CONFIGURATION ---
st.set_page_config(
    page_title="Autonomous B2B Sales Agent",
    page_icon="🤖",
    layout="wide"
)

# --- HEADER & DESCRIPTION ---
st.title("🤖 Autonomous B2B Sales Agent")
st.markdown("""
This AI Agent leverages **Google Gemini 2.0 Flash** and **Google Search Grounding** to conduct real-time research on target companies and draft hyper-personalized cold emails.
""")

# --- SIDEBAR (API KEY CONFIG) ---
with st.sidebar:
    st.header("⚙️ Settings")
    
    # Input for API Key (Secure handling)
    api_key_input = st.text_input(
        "Enter your Google API Key:", 
        type="password",
        help="You can get this from Google AI Studio."
    )
    
    st.info("🔒 Your key is used securely for this session only and is not stored.")
    
    # Check if key exists in environment variables (for local dev)
    if not api_key_input and "GOOGLE_API_KEY" in os.environ:
        api_key_input = os.environ["GOOGLE_API_KEY"]
        st.success("✅ API Key detected from system environment.")

# --- AGENT LOGIC ---
def generate_email(company_name, key):
    """
    Calls the Gemini API with Search Grounding to generate the email.
    """
    client = genai.Client(api_key=key)
    
    prompt = f"""
    You are an expert B2B Sales Development Representative (SDR).
    
    TASK:
    1. Search Google for the latest news and business focus of: "{company_name}".
    2. Identify a key pain point or recent achievement.
    3. Draft a concise, professional cold email pitching "AI Automation Services".
    4. CRITICAL: The email MUST specifically reference the real-time news you found.
    
    TONE: Professional, persuasive, and non-spammy.
    """
    
    try:
        # Call Gemini 2.0 Flash with Search Tool
        response = client.models.generate_content(
            model='gemini-flash-latest',
            contents=prompt,
            config=types.GenerateContentConfig(
                tools=[types.Tool(google_search=types.GoogleSearch())],
                response_modalities=["TEXT"]
            )
        )
        return response
    except Exception as e:
        return f"Error: {e}"

def create_pdf(text):
    """
    Generates a PDF file from the provided text.
    """
    pdf = FPDF()
    pdf.add_page()
    pdf.set_font("Arial", size=12)
    
    # Handle Unicode characters by replacing them or using a compatible logic
    # FPDF 1.7.2 has limited unicode support. Basic encoding:
    clean_text = text.encode('latin-1', 'replace').decode('latin-1')
    
    pdf.multi_cell(0, 10, clean_text)
    return pdf.output(dest='S').encode('latin-1')


# --- MAIN INTERFACE ---
col1, col2 = st.columns([2, 1])

with col1:
    st.subheader("🎯 Target Company")
    company = st.text_input(
        "Company Name (e.g., Skroutz.gr, Tesla, Airbnb)", 
        placeholder="Enter company name here..."
    )
    
    # Action Button
    if st.button("🚀 Research & Generate Email", type="primary"):
        if not api_key_input:
            st.error("⚠️ Please enter your Google API Key in the sidebar first.")
        elif not company:
            st.warning("⚠️ Please enter a company name.")
        else:
            with st.spinner(f"🔍 Agent is researching {company} on Google..."):
                # Run the Agent
                result = generate_email(company, api_key_input)
                
                # Check for errors
                if isinstance(result, str) and "Error" in result:
                    st.error(result)
                else:
                    st.success("✅ Research Complete!")
                    
                    # Display the Email
                    st.subheader("📧 Generated Cold Email")
                    st.markdown("---")
                    st.markdown(result.text)
                    st.markdown("---")
                    
                    # PDF Download Button
                    pdf_bytes = create_pdf(result.text)
                    st.download_button(
                        label="📄 Download as PDF",
                        data=pdf_bytes,
                        file_name=f"{company}_cold_email.pdf",
                        mime="application/pdf"
                    )
                    
                    # Display Sources (Grounding Metadata)
                    if result.candidates[0].grounding_metadata.search_entry_point:
                        with st.expander("📚 View Research Sources (Google Search Data)"):
                            st.write(result.candidates[0].grounding_metadata.search_entry_point.rendered_content)

with col2:
    st.markdown("### 💡 How it works")
    st.info("""
    1. **Input:** You provide a target company name.
    2. **Research:** The Agent searches Google for real-time news (recent funding, launches, etc.).
    3. **Analysis:** It identifies an angle to pitch AI services.
    4. **Drafting:** It writes a personalized email referencing the found news.
    """)
    
    st.markdown("---")
    st.caption("Powered by **Google Gemini 2.0** & **Streamlit**")