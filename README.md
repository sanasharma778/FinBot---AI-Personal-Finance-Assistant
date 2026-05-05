# FinBot — Conversational AI Finance Assistant

![Python](https://img.shields.io/badge/Python-3.11-blue)
![LangChain](https://img.shields.io/badge/LangChain-latest-green)
![Streamlit](https://img.shields.io/badge/Streamlit-UI-red)
![Groq](https://img.shields.io/badge/Groq-LLaMA3.1-orange)

> An AI-powered personal finance assistant with 4 specialist modes, 
> built with LangChain, Groq and Streamlit.

##  Live Demo
Going to deploy on hugging face as soon as the proper demo gets ready

##  What Problem Does This Solve?
Personal finance is overwhelming! especially for young adults navigating budgeting, saving and investing for the first 
time. FinBot provides instant, conversational guidance tailored to the UK financial landscape.

##  Features
- 4 specialist finance modes powered by prompt engineering
- Full multi-turn conversation memory across the session
- Chat history export as .txt file
- UK-specific financial guidance mode
- Secure API key management via environment variables
- Clean separation of concerns across prompts, logic and UI

##  The 4 Modes
| Mode | What It Does |
|---|---|
| Budget Advisor | Plans monthly budgets tailored to UK cost of living |
| Investment Basics | Explains stocks, ISAs, index funds for beginners |
| Saving Goals | Breaks saving targets into weekly and monthly plans |
| UK Finance Guide | Covers ISAs, National Insurance, tax bands and more |

##  Project Structure
```
finbot/
├── app/
│   ├── chatbot.py        # LangChain model + response logic
│   └── prompts.py        # System prompts for each mode
├── frontend/
│   └── streamlit_app.py  # Streamlit UI
├── .streamlit/
│   └── config.toml       # Streamlit configuration
├── .env                  # API keys (not committed)
├── .gitignore
├── requirements.txt
└── README.md
```

##  Tech Stack
| Layer | Technology |
|---|---|
| LLM | Groq (LLaMA 3.1 8B Instant) |
| AI Framework | LangChain |
| Frontend | Streamlit |
| Language | Python 3.11 |
| Deployment | Hugging Face Spaces |

##  Setup & Run Locally
```bash
# Clone the repo
git clone https://github.com/sanasharma778/FinBot---AI-Personal-Finance-Assistant.git
cd FinBot---AI-Personal-Finance-Assistant

# Create virtual environment
python -m venv venv
venv\Scripts\activate  # Windows
source venv/bin/activate  # Mac/Linux

# Install dependencies
pip install -r requirements.txt

# Add your Groq API key
# Create a .env file and add:
# GROQ_API_KEY=your_key_here

# Run the app
streamlit run frontend/streamlit_app.py
```

##  What I Learned
Building FinBot taught me how LangChain structures conversations using 
SystemMessage, HumanMessage and AIMessage to simulate memory across 
turns. I learned why separating prompts from logic matters for 
maintainability, how Streamlit session_state persists data across 
reruns, and the importance of secure API key management using 
environment variables.

##  What's Next
- Adding a RAG pipeline so FinBot can answer from uploaded financial 
documents(Need to research and gather papers)
- Adding a spending tracker with visual charts

##  Disclaimer
FinBot provides general financial information only and does not 
constitute financial advice. Always consult a qualified financial 
advisor before making financial decisions.
