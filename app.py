"""
PromptCraft — Main Application
Interactive LLM Prompting Demonstration App
"""

import os
import streamlit as st
from dotenv import load_dotenv

load_dotenv()

# ── Page Config ─────────────────────────────────────────────────
st.set_page_config(
    page_title="PromptCraft",
    page_icon="🧠",
    layout="wide",
    initial_sidebar_state="expanded",
)

# ── Custom CSS ──────────────────────────────────────────────────
from utils.ui_components import inject_custom_css
inject_custom_css()

# ── Sidebar ─────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("""
    <div style="text-align:center; padding:20px 0;">
        <div style="font-size:3rem;">🧠</div>
        <h1 style="margin:0; font-size:1.6rem; background:linear-gradient(135deg, #7C4DFF, #00E676);
                   -webkit-background-clip:text; -webkit-text-fill-color:transparent;">
            PromptCraft
        </h1>
        <p style="color:#888; font-size:0.8rem; margin-top:4px;">Master LLM Prompting</p>
    </div>
    """, unsafe_allow_html=True)

    st.divider()

    # API Key configuration
    api_key = os.getenv("OPENROUTER_API_KEY", "")
    if not api_key or api_key == "your_openrouter_api_key_here":
        st.markdown("##### 🔑 API Configuration")
        entered_key = st.text_input(
            "OpenRouter API Key",
            type="password",
            placeholder="Enter your OpenRouter API key",
            help="Get a key from https://openrouter.ai/keys",
        )
        if entered_key:
            os.environ["OPENROUTER_API_KEY"] = entered_key
            st.success("✅ API key set!")
            st.rerun()
    else:
        st.success("✅ API key configured")

    st.divider()

    # Session stats
    if "run_history" not in st.session_state:
        st.session_state.run_history = []

    total_runs = len(st.session_state.run_history)
    st.markdown(f"**📊 Session Stats**")
    st.caption(f"Total runs: {total_runs}")

    st.divider()
    st.markdown(
        '<p style="color:#555; font-size:0.7rem; text-align:center;">'
        'Built with Streamlit + OpenRouter</p>',
        unsafe_allow_html=True,
    )


# ── Main Content ────────────────────────────────────────────────
st.markdown("""
<div style="text-align:center; padding:40px 0 20px 0;">
    <div style="font-size:4rem; margin-bottom:16px;">🧠</div>
    <h1 style="font-size:3rem; margin:0; background:linear-gradient(135deg, #7C4DFF, #448AFF, #00E676);
               -webkit-background-clip:text; -webkit-text-fill-color:transparent; font-weight:800;">
        PromptCraft
    </h1>
    <p style="font-size:1.3rem; color:#aaa; margin-top:12px; font-weight:300;">
        Master LLM Prompting — See How Better Prompts Eliminate Hallucinations
    </p>
</div>
""", unsafe_allow_html=True)

st.divider()

# ── Feature Cards ───────────────────────────────────────────────
st.markdown("### 🚀 What You Can Do")
st.write("")

col1, col2, col3 = st.columns(3)

with col1:
    st.markdown("""
    <div class="technique-card" style="border:1px solid #7C4DFF30;">
        <div style="font-size:2.5rem; margin-bottom:12px;">📖</div>
        <div style="font-size:1.1rem; font-weight:600; color:white; margin-bottom:8px;">
            Guided Tutorial
        </div>
        <div style="font-size:0.85rem; color:#aaa; line-height:1.5;">
            Walk through 8 prompting levels — from Zero-Shot to Tree-of-Thought.
            See how each technique improves LLM responses.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col2:
    st.markdown("""
    <div class="technique-card" style="border:1px solid #448AFF30;">
        <div style="font-size:2.5rem; margin-bottom:12px;">🏟️</div>
        <div style="font-size:1.1rem; font-weight:600; color:white; margin-bottom:8px;">
            Prompt Arena
        </div>
        <div style="font-size:0.85rem; color:#aaa; line-height:1.5;">
            Compare any two prompting techniques side-by-side.
            Same question, different approaches, measurable results.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col3:
    st.markdown("""
    <div class="technique-card" style="border:1px solid #00E67630;">
        <div style="font-size:2.5rem; margin-bottom:12px;">🔍</div>
        <div style="font-size:1.1rem; font-weight:600; color:white; margin-bottom:8px;">
            Hallucination Detector
        </div>
        <div style="font-size:0.85rem; color:#aaa; line-height:1.5;">
            Analyze any LLM response claim-by-claim.
            Find hallucinations and learn which techniques prevent them.
        </div>
    </div>
    """, unsafe_allow_html=True)

st.write("")

col4, col5, col6 = st.columns(3)

with col4:
    st.markdown("""
    <div class="technique-card" style="border:1px solid #FF910030;">
        <div style="font-size:2.5rem; margin-bottom:12px;">🛠️</div>
        <div style="font-size:1.1rem; font-weight:600; color:white; margin-bottom:8px;">
            Prompt Workbench
        </div>
        <div style="font-size:0.85rem; color:#aaa; line-height:1.5;">
            Build your own prompts with template variables.
            Test, iterate, and compare against built-in techniques.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col5:
    st.markdown("""
    <div class="technique-card" style="border:1px solid #FFD60030;">
        <div style="font-size:2.5rem; margin-bottom:12px;">📊</div>
        <div style="font-size:1.1rem; font-weight:600; color:white; margin-bottom:8px;">
            Analytics Dashboard
        </div>
        <div style="font-size:0.85rem; color:#aaa; line-height:1.5;">
            Track performance across techniques. Radar charts,
            leaderboards, and exportable run history.
        </div>
    </div>
    """, unsafe_allow_html=True)

with col6:
    st.markdown("""
    <div class="technique-card" style="border:1px solid #FF174430;">
        <div style="font-size:2.5rem; margin-bottom:12px;">📚</div>
        <div style="font-size:1.1rem; font-weight:600; color:white; margin-bottom:8px;">
            Scenario Library
        </div>
        <div style="font-size:0.85rem; color:#aaa; line-height:1.5;">
            16 curated challenge scenarios across 6 categories.
            From trick questions to medical queries.
        </div>
    </div>
    """, unsafe_allow_html=True)


# ── Quick Start ─────────────────────────────────────────────────
st.write("")
st.divider()
st.markdown("### ⚡ Quick Start")

from core.llm_client import is_api_key_configured

if is_api_key_configured():
    st.success("✅ You're all set! Use the sidebar to navigate to any page.")
else:
    st.info(
        "👈 **Enter your OpenRouter API key** in the sidebar to get started. "
        "Get a key at [OpenRouter](https://openrouter.ai/keys)."
    )

# ── Technique Overview ──────────────────────────────────────────
st.write("")
st.divider()
st.markdown("### 🧩 The 8 Prompting Levels")

from core.prompt_templates import ALL_TEMPLATES
import config

for i, key in enumerate(config.TECHNIQUE_ORDER):
    template = ALL_TEMPLATES[key]
    with st.expander(f"**Level {i+1}: {template.icon} {template.name}** — {template.description}"):
        st.markdown(f"**How it works:** {template.how_it_works}")
        st.markdown(f"**Why it helps:** {template.why_it_helps}")
        st.markdown(f"**Expected improvement:** {template.example_boost}")
