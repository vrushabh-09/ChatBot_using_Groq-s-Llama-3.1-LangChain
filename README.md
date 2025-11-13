# ChatBot_using_Groq-s-Llama-3.1-LangChain 💬

> **Converse. Learn. Explore.**
> Meet your intelligent AI assistant — built to answer queries with precision, context, and personality.
> Powered by **Groq’s Llama 3.1** and **LangChain**, this chatbot delivers lightning-fast, human-like conversations through a sleek **Streamlit** interface.
---

![Streamlit](https://img.shields.io/badge/Framework-Streamlit-FF4B4B?logo=streamlit&logoColor=white)
![Python](https://img.shields.io/badge/Python-3.11+-3776AB?logo=python&logoColor=white)
![Groq](https://img.shields.io/badge/AI-Groq_Llama_3.1_8B-00A86B?logo=groq&logoColor=white)
![LangChain](https://img.shields.io/badge/Framework-LangChain-3E8EDE?logo=chainlink&logoColor=white)
![License](https://img.shields.io/badge/License-MIT-yellow.svg)
![Status](https://img.shields.io/badge/Status-Active-brightgreen)

---

## 🌟 Overview

**Vrushabh’s Chatbot** is a personalized AI assistant designed to simulate meaningful and helpful conversations.
From tech questions to general knowledge — it provides **accurate, concise, and contextual answers**, all while maintaining a friendly and engaging tone.

This project demonstrates the integration of **LangChain** with **Groq’s Llama-3.1-8B** inside a **Streamlit** app, using session state for conversational memory.

---

## ✨ Key Features

* 💬 **Conversational Memory** – Keeps track of chat history for natural, context-aware replies.
* ⚡ **Groq-Powered Responses** – Harnesses the blazing speed of Llama 3.1 for near-instant answers.
* 🧠 **LangChain Integration** – Modular, extensible prompt templates for scalable AI logic.
* 🎨 **Clean UI** – Minimalistic, emoji-rich chat interface built with Streamlit.
* 🔐 **Secure Setup** – Environment variables loaded via `.env` to protect API keys.
* 🧩 **Error Handling** – Detects missing keys or API failures gracefully with clear messages.

---

## 🧠 Tech Stack

| Layer | Technology |
| :---: | :---: |
| **Frontend/UI** | Streamlit |
| **AI Engine** | Groq Llama 3.1 8B |
| **Prompt Management** | LangChain |
| **Environment Handling** | python-dotenv |
| **Language** | Python 3.11+ |

---

## 🧩 Architecture

```mermaid
graph TD
    A["User Input 💬"] --> B["Streamlit Interface"]
    B --> C["LangChain Prompt Template"]
    C --> D["Groq Llama-3.1-8B (via ChatGroq)"]
    D --> E["Output Parser"]
    E --> F["AI Response Display 🧠"]
    F --> G["Session Memory (Chat History)"]
````

-----

## ⚙️ Installation & Setup

### 1️⃣ Clone the Repository

```bash
git clone [https://github.com/](https://github.com/)<your-username>/ChatBot_using_Groq-s-Llama-3.1-LangChain.git
cd ChatBot_using_Groq-s-Llama-3.1-LangChain
```

### 2️⃣ Create a Virtual Environment

```bash
python -m venv venv
source venv/bin/activate        # macOS / Linux
venv\Scripts\activate           # Windows
```

### 3️⃣ Install Dependencies

```bash
pip install -r requirements.txt
```

### 4️⃣ Configure Environment Variables

Create a **`.env`** file in the project root directory:

```bash
GROQ_API_KEY=your_groq_api_key_here
LANGCHAIN_API_KEY=your_langchain_api_key_here
LANGCHAIN_PROJECT=your_project_name_here
```

### 5️⃣ Run the Application

```bash
streamlit run app.py
```

Then open the local URL displayed in the terminal (e.g., `http://localhost:8501`).

-----

## 💬 How to Use

1.  **Launch the app.**
2.  **Type any question** in the chat input (e.g., “What is AI?” or “Who is Elon Musk?”).
3.  Get instant, structured, and conversational responses.
4.  **Continue chatting** — context is preserved automatically\!

-----

## 🧠 Example Conversation

> 👤 **User:** What’s new in AI this year?
>
> 🤖 **AI:** 2025 has seen remarkable growth in multimodal models like Gemini 2.5 and Llama 3.1, focusing on reasoning and tool use.
>
> 👤 **User:** Who created you?
>
> 🤖 **AI:** I was built by Vrushabh Patil, integrating Groq AI, LangChain, and Streamlit to deliver natural conversations.

-----

## 📁 Project Structure

```bash
vrushabh-chatbot/
│
├── app.py             # Main Streamlit chatbot application
├── requirements.txt   # Python dependencies
├── .env               # API keys (excluded from Git)
├── README.md          # Documentation
└── assets/            # Optional folder for images, icons, etc.
```

-----

## 🛡️ Error Handling

| Issue | Solution |
| :---: | :---: |
| Missing API Keys | Displays warning and stops execution gracefully |
| Groq Initialization Error | Caught and displayed with a helpful message |
| Invalid Prompt or Input | Returns a friendly error notice |
| Session Reset | Memory cleared safely without app crash |

-----

## 🎨 UI Highlights

  * 💬 Modern Streamlit chat interface
  * 🌈 Emoji-supported input box
  * 🧠 Scrollable chat memory
  * 🖥️ Centered layout for focused conversations
  * ❤️ Footer credit with subtle style

-----

## 🔮 Future Roadmap

🚧 **Planned Enhancements:**

  * 🧩 Voice Input + Text-to-Speech Output
  * 🧠 Memory Persistence across sessions
  * 🌐 Integration with live data APIs
  * 📊 Analytics dashboard for chat insights
  * 🌍 Multilingual mode (English, Hindi, Marathi)

-----

## 🧑‍💻 Developer

| Information | Details |
| :---: | :---: |
| **Name** | 👤 Vrushabh Patil |
| **Role** | 🎯 AI & Software Developer – Innovating with Generative AI, Web Apps & Intelligent Systems |
| **Email** | 📧 vrushabhpatil97711@gmail.com |
| **Links** | [🔗 LinkedIn](https://www.linkedin.com/in/patilvrushabh/)

-----

## 🪪 License

This project is licensed under the **MIT License** — feel free to use, modify, and distribute with proper credit.

-----

## ⭐ Acknowledgments

Special thanks to:

  * Groq AI for ultra-fast inference
  * LangChain for modular AI orchestration
  * Streamlit for the modern Python UI
  * `dotenv` for secure environment handling

> 💡 “Technology is best when it brings people together — and intelligence to conversation.”
>
> — Vrushabh Patil

```
