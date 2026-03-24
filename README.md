# PromptCraft

PromptCraft is an interactive Streamlit application designed to demonstrate and compare various LLM prompting techniques. Learn how better prompts eliminate hallucinations through guided tutorials, side-by-side prompt arenas, hallucination detectors, and more!

## Features
- **Guided Tutorial:** Explore 8 different prompting levels (Zero-Shot to Tree-of-Thought).
- **Prompt Arena:** Compare any two prompting techniques side-by-side.
- **Hallucination Detector:** Analyze any LLM response claim-by-claim.
- **Prompt Workbench:** Build your own prompts with template variables.
- **Analytics Dashboard:** Track performance and history.
- **Scenario Library:** 16 curated challenge scenarios to test prompts against.

## Setup & Installation

It is highly recommended to use a virtual environment (`venv`) to install the dependencies and keep your system clean.

### 1. Create a virtual environment

For Windows:
```bash
python -m venv .venv
.venv\Scripts\activate
```

For macOS/Linux:
```bash
python3 -m venv .venv
source .venv/bin/activate
```

### 2. Install dependencies

Once the virtual environment is activated, install the required packages using `requirements.txt`:

```bash
pip install -r requirements.txt
```

### 3. Environment Variables

Create a `.env` file based on `.env.example` and add your OpenRouter API key:
```env
OPENROUTER_API_KEY=your_api_key_here
```

### 4. Run the Application

```bash
streamlit run app.py
```