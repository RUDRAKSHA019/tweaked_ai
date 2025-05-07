
# 🧠 F.R.I.D.A.Y. - Your Fun AI Assistant

> A brutally sarcastic, voice-enabled AI chatbot powered by OpenAI and Streamlit. Designed to roast everyone like it’s a full-time job.

## ✨ Features

- 🤖 Conversational AI using OpenAI's `gpt-4o-mini`
- 🔊 Voice response via in-browser speech synthesis (No external TTS engine required)
- 🌐 Web and app opening commands (`open google`, `open notepad`, etc.)
- 📚 Wikipedia integration for quick facts
- 🔎 Google and YouTube search via simple commands
- 💬 Streamlit-based chat interface with persistent conversation history
- 🎤 Continuous input simulation (auto-clears input field after every response)
- 😈 Sarcasm mode: permanently ON

## 🚀 How to Run

1. **Clone the repo**  
   ```bash
   git clone "https://github.com/RUDRAKSHA019/tweaked_ai"
cd "tweaked_ai"
   ```

 2.**Set up your virtual environment (optional but not optional)**  
  ```bash
   python -m venv .venv
   .venv\Scripts\activate  # Windows
   source .venv/bin/activate  # macOS/Linux
   ```

3. **Install dependencies**  
   ```bash
   pip install -r requirements.txt
   ```

4. **Create a `.env` file** in the root directory:
   ```
   OPENAI_API_KEY=your_openai_api_key_here
   ```

5. **Run the chatbot**  
   ```bash
   streamlit run "./Ai.py"
   ```

6. **Talk to F.R.I.D.A.Y.**  
   Just type your question and prepare to be insulted… with answers.

## 🧠 Example Commands

- `wiki ChatGPT` → Summarizes topic via Wikipedia  
- `open youtube` → Opens YouTube  
- `open notepad` → Opens Notepad (on Windows)  
- `search google why is AI so sarcastic`  
- `search youtube doom eternal soundtrack`

## ⚠️ Disclaimer

This AI is designed to be **brutally honest**, **sarcastic**, and **unfiltered**. If you’re easily offended, this ain’t for you. It’s meant for devs who want more spice in their bots.

## 📦 Requirements

- Python 3.9+
- Streamlit
- OpenAI API Key
- pyttsx3 (optional if you want desktop voice instead of browser)

## 📄 License

Feel free to use, modify, and share this chaos machine. Just don't blame me when your feelings get hurt.

---

