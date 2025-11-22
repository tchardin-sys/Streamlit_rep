# app.py — Personal “Terah Bot” with pre-defined prompts & responses

import streamlit as st

# -----------------------------
# 🔧 Page config
# -----------------------------
st.set_page_config(
    page_title="🤖 My Personal Chatbot",
    page_icon="🤖",
    layout="centered",
)

# -----------------------------
# ✏️ Define your prompts & responses here
# -----------------------------
# You can customize ALL of these. Think of them as "chat macros."
PREDEFINED_QA = [
    {
        "id": "study-plan",
        "label": "📚 Help me plan my study session",
        "user_text": "Can you help me plan my study session?",
        "bot_text": (
            "Absolutely! Here’s a simple 60–90 minute focused plan:\n\n"
            "1. **10 min – Setup & review:** Open your notes, syllabus, and to-do list. "
            "Write down 1–2 goals for this session.\n"
            "2. **25 min – Deep work block #1:** Work on one focused task (e.g., "
            "finish 2–3 practice problems or one quiz).\n"
            "3. **5 min – Break:** Walk, stretch, water, no phone scrolling.\n"
            "4. **25 min – Deep work block #2:** Continue or switch to a second task.\n"
            "5. **5–10 min – Wrap-up:** Summarize what you did in 3–4 bullet points "
            "and list the next steps for your next session.\n\n"
            "You can message me: *“Update my study plan”* when you want to adjust this."
        ),
    },
    {
        "id": "encouragement",
        "label": "💪 I need some encouragement",
        "user_text": "I’m feeling overwhelmed. I need some encouragement.",
        "bot_text": (
            "Totally get it. You’ve been juggling a lot, and it’s normal to feel tired.\n\n"
            "Reminder: you’ve already handled hard things—grad school, analytics, "
            "projects, job searching—and you’re still here, still pushing.\n\n"
            "Pick one tiny win you can get in the next 20 minutes (one problem, one email, "
            "one paragraph). Do that, and then you’re officially ‘back in motion’. "
            "You don’t have to do everything today—just the next right thing. 💛"
        ),
    },
    {
        "id": "career",
        "label": "💼 Help me focus my career goals",
        "user_text": "Help me focus my career goals in data/AI.",
        "bot_text": (
            "Let’s simplify your career focus into three pillars:\n\n"
            "1. **Direction:** Data / AI roles that fit you: Data Analyst, AI Product Manager, "
            "ML-adjacent Business Analyst, or Automation Specialist.\n"
            "2. **Brand:** Pick 2–3 themes you’re known for (e.g., automation, practical ML, "
            "turning messy data into decisions). Use those in your LinkedIn headline and resume.\n"
            "3. **Next 30 days:**\n"
            "   - Update resume + LinkedIn around those themes\n"
            "   - Apply to roles that match 60–70% of your skills\n"
            "   - Reach out to 2–3 people per week for short chats.\n\n"
            "You can ask: *“Remind me of my 30-day plan”* when you need to reset."
        ),
    },
    {
        "id": "debug-mindset",
        "label": "🐞 Remind me of a good debugging mindset",
        "user_text": "Remind me of a good debugging mindset when my code breaks.",
        "bot_text": (
            "Debugging mantra:\n\n"
            "1. **Reproduce the bug** on the smallest possible example.\n"
            "2. **Read the full error message**, not just the first line.\n"
            "3. **Print / inspect variables** right before the error.\n"
            "4. Change *one thing at a time* and re-run.\n"
            "5. If stuck for 20+ minutes, take a 5-minute break, then write a short, "
            "clear question about the bug (that alone often reveals the fix).\n\n"
            "You’re not ‘bad at coding’—your brain is literally learning how to talk to a "
            "very picky machine. That takes time. 🙂"
        ),
    },
]


# Turn list into a dictionary for quick lookup by id
QA_BY_ID = {item["id"]: item for item in PREDEFINED_QA}


# -----------------------------
# 💾 Initialize session state
# -----------------------------
if "chat_history" not in st.session_state:
    # Each message: {"role": "user" | "bot", "text": "..."}
    st.session_state.chat_history = []

# -----------------------------
# 🎨 Header
# -----------------------------
st.markdown(
    """
    <h1 style="text-align:center;">🤖 My Personal Chatbot</h1>
    <p style="text-align:center; font-size:0.95rem;">
        This bot uses <b>pre-defined prompts and responses</b> that you control.<br>
        Click a card below to send one of your saved prompts.
    </p>
    """,
    unsafe_allow_html=True,
)

# -----------------------------
# 🔘 Layout: prompt buttons
# -----------------------------
st.subheader("Choose a prompt")

cols = st.columns(2)
for i, item in enumerate(PREDEFINED_QA):
    col = cols[i % 2]
    with col:
        if st.button(item["label"], use_container_width=True):
            # Add user message
            st.session_state.chat_history.append(
                {"role": "user", "text": item["user_text"]}
            )
            # Add bot response
            st.session_state.chat_history.append(
                {"role": "bot", "text": item["bot_text"]}
            )

# -----------------------------
# 💬 Chat display
# -----------------------------
st.subheader("Conversation")

if not st.session_state.chat_history:
    st.info("No messages yet. Click one of the prompts above to start the conversation.")
else:
    for msg in st.session_state.chat_history:
        if msg["role"] == "user":
            with st.chat_message("user"):
                st.markdown(msg["text"])
        else:
            with st.chat_message("assistant"):
                st.markdown(msg["text"])

# -----------------------------
# 🧹 Clear conversation
# -----------------------------
if st.button("🧹 Clear conversation"):
    st.session_state.chat_history = []
    st.experimental_rerun()
