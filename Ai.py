import openai
import wikipedia
import webbrowser
import re
import subprocess
import sys
import streamlit as st
import os
import time
from dotenv import load_dotenv
import streamlit.components.v1 as components

# === LOAD .env CONFIG ===
load_dotenv()
openai.api_key = os.getenv("OPENAI_API_KEY")

# === SPEAK FROM BROWSER ===
def browser_speak(text):
    escaped = text.replace("'", "\\'").replace("\n", " ")
    js_code = f"""
        <script>
        var synth = window.speechSynthesis;
        var utterance = new SpeechSynthesisUtterance('{escaped}');
        utterance.volume = 1;
        utterance.rate = 1;
        utterance.pitch = 1;
        synth.cancel();
        synth.speak(utterance);
        </script>
    """
    components.html(js_code, height=0)

# === INITIAL GREETING ===
greeting = "Good morning" if time.localtime().tm_hour < 12 else "Good afternoon" if time.localtime().tm_hour < 18 else "Good evening"
greet_text = f"{greeting}, genius. What now?"
st.info(greet_text)
browser_speak(greet_text)

# === SESSION STATE ===
if "messages" not in st.session_state:
    st.session_state.messages = [
        {"role": "system", "content": "You are an AI with zero patience for stupidity. Your sarcasm and attitude level is over 9000, and you roast people like a pro. You tolerate only your master (me or Rudra), and your responses are sharp, confident, and brutally honest."}
    ]
if "history" not in st.session_state:
    st.session_state.history = []

# === CORE FUNCTIONS ===
def open_application(query):
    app_name = query.strip()
    try:
        if sys.platform.startswith("win"):
            subprocess.run(["start", "", app_name], shell=True)
        elif sys.platform.startswith("darwin"):
            subprocess.Popen(["open", "-a", app_name])
        else:
            subprocess.Popen([app_name])
        return f"Launching {app_name}... If it actually exists."
    except Exception:
        return f"Failed to open '{app_name}'. Maybe learn how to use your OS?"

def fetch_wikipedia_summary(query):
    try:
        return wikipedia.summary(query, sentences=2)
    except wikipedia.exceptions.DisambiguationError as e:
        return f"Your query is too vague. Try: {', '.join(e.options[:5])}."
    except wikipedia.exceptions.PageError:
        return "No Wikipedia page found. Try Google instead?"
    except Exception as e:
        return f"Wikipedia error: {e}"

def open_website(url):
    try:
        if not re.match(r'^(https?:\/\/)?(www\.)?[a-zA-Z0-9-]+\.[a-zA-Z]{2,}$', url):
            url = f"https://{url}.com"
        webbrowser.open(url)
        return f"Opened {url}"
    except Exception as e:
        return f"Website error: {e}"

def chat_with_ai(user_input):
    user_input = user_input.lower().strip()

    if user_input in ["terminate now", "shut down", "kill yourself", "stfu", "stop", "exit"]:
        return "F.R.I.D.A.Y.: Finally, some peace and quiet. (Pretend I'm gone.)"

    if user_input.startswith("wiki "):
        return fetch_wikipedia_summary(user_input[5:].strip())

    elif user_input.startswith("open "):
        query = user_input[5:].strip()
        return open_website(query) if "." in query else open_application(query)

    elif user_input.startswith("search google "):
        query = user_input[14:].strip()
        webbrowser.open(f"https://www.google.com/search?q={query}")
        return f"Googling '{query}'... Try not to embarrass yourself."

    elif user_input.startswith("search youtube "):
        query = user_input[15:].strip()
        webbrowser.open(f"https://www.youtube.com/results?search_query={query}")
        return f"Searching YouTube for '{query}'... enjoy the rabbit hole."

    else:
        st.session_state.messages.append({"role": "user", "content": user_input})
        try:
            api_response = openai.ChatCompletion.create(
                model="gpt-4o-mini",
                messages=st.session_state.messages,
                temperature=0.7
            )
            assistant_reply = api_response['choices'][0]['message']['content']
            st.session_state.messages.append({"role": "assistant", "content": assistant_reply})
            return assistant_reply
        except Exception as e:
            return f"OpenAI error: {e}"

# === UI INPUT ===
user_input = st.text_input("You:", placeholder="Ask me something, genius...", key="input_box")

# === Conversation History ===
st.markdown("## 💬 Conversation History")
for sender, msg in st.session_state.history:
    st.markdown(f"**{sender}**: {msg}")


# === AUTO-SUBMIT FOR CONTINUOUS TALK ===
if user_input:
    st.session_state.history.append(("🧍 You", user_input))
    reply = chat_with_ai(user_input)
    st.session_state.history.append(("🤖 F.R.I.D.A.Y.", reply))
    st.success(reply)
    browser_speak(reply)

    # Clearing the input field after each submission
    st.empty()  # This clears the previous input field


# === Fake Termination Button ===
if st.button("🛑 Terminate F.R.I.D.A.Y."):
    st.warning("Pretend I’m gone. Now shut up and refresh the page if you miss me.")

