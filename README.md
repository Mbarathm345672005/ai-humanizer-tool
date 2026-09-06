<p align="center">
  <h1 align="center">🧬 AI Text Humanizer (NLTK Mode)</h1>
  <p align="center">
    A Streamlit-powered tool that transforms AI-generated text into natural, human-sounding content using intelligent synonym swapping.
  </p>
</p>

<p align="center">
  <a href="https://mark-ai-humanizer-tool.streamlit.app/"><img src="https://img.shields.io/badge/🚀_Live_Demo-Click_Here-FF4B4B?style=for-the-badge" alt="Live Demo"></a>
</p>

<p align="center">
  <a href="https://www.python.org/downloads/"><img src="https://img.shields.io/badge/Python-3.9-blue?logo=python&logoColor=white" alt="Python 3.9"></a>
  <a href="https://streamlit.io/"><img src="https://img.shields.io/badge/Streamlit-App-FF4B4B?logo=streamlit&logoColor=white" alt="Streamlit"></a>
  <a href="https://www.nltk.org/"><img src="https://img.shields.io/badge/NLTK-NLP-green?logo=bookstack&logoColor=white" alt="NLTK"></a>
  <a href="https://github.com/Mbarathm345672005/ai-humanizer-tool/blob/main/LICENSE"><img src="https://img.shields.io/badge/License-MIT-yellow.svg" alt="License: MIT"></a>
</p>

---

## 📸 Screenshot

<!-- 
  👇 REPLACE THE PATH BELOW WITH YOUR ACTUAL SCREENSHOT 👇
  Upload your screenshot to the repo (e.g., screenshots/ui.png) and update the path.
-->

<img width="1916" height="859" alt="image" src="https://github.com/user-attachments/assets/4045727a-7a02-43e4-84ac-25aeb921077d" />


---

## 📖 About The Project

**AI Text Humanizer** is a lightweight web application that helps rewrite AI-generated text to make it sound more natural and human-like. It uses **NLTK's WordNet** corpus to intelligently swap words with their synonyms, effectively breaking repetitive AI patterns and lowering AI-detection scores.

Whether you're a student, content writer, or researcher — this tool helps you refine AI-assisted drafts into polished, human-sounding content.

### ✨ Key Features

| Feature | Description |
|---|---|
| 🔄 **Synonym Swapping** | Replaces words with contextually appropriate synonyms using WordNet |
| 📂 **Multi-Format Upload** | Supports `.pdf`, `.docx`, and `.txt` file uploads |
| ✍️ **Direct Text Input** | Paste text directly into the app for quick humanization |
| 🎚️ **Adjustable Randomness** | Fine-tune the humanization level (0.1 – 0.5) via a sidebar slider |
| ⬇️ **Export Results** | Download humanized text as `.txt` or `.docx` |
| 🧠 **Smart Word Selection** | Only replaces words longer than 4 characters to preserve sentence structure |
| ⚡ **Cached NLTK Setup** | NLTK resources are downloaded once and cached for fast subsequent runs |

---

## 🛠️ Tech Stack

- **Frontend / UI** — [Streamlit](https://streamlit.io/)
- **NLP Engine** — [NLTK](https://www.nltk.org/) + [TextBlob](https://textblob.readthedocs.io/)
- **PDF Parsing** — [PyPDF2](https://pypdf2.readthedocs.io/)
- **DOCX Handling** — [python-docx](https://python-docx.readthedocs.io/)
- **Runtime** — Python 3.9

---

## 🚀 Getting Started

### Prerequisites

- **Python 3.9+** installed on your machine
- **pip** package manager

### Installation

1. **Clone the repository**

   ```bash
   git clone https://github.com/Mbarathm345672005/ai-humanizer-tool.git
   cd ai-humanizer-tool
   ```

2. **Create a virtual environment** (recommended)

   ```bash
   python -m venv venv

   # Windows
   venv\Scripts\activate

   # macOS / Linux
   source venv/bin/activate
   ```

3. **Install dependencies**

   ```bash
   pip install -r requirements.txt
   ```

4. **Run the application**

   ```bash
   streamlit run app.py
   ```

5. Open your browser and navigate to `http://localhost:8501`

---

## 📋 Usage

1. **Launch the app** using `streamlit run app.py`
2. **Choose your input method:**
   - 📂 **Upload File** — Upload a `.pdf`, `.docx`, or `.txt` file
   - ✍️ **Paste Text** — Type or paste text directly
3. **Adjust the Humanization Level** using the sidebar slider
   - `0.1` = minimal changes (safer, more readable)
   - `0.5` = aggressive changes (lower AI detection, potential grammar trade-offs)
4. **Click "Humanize Text"** to process
5. **Download the result** as `.txt` or `.docx`

---

## 📁 Project Structure

```
ai-humanizer-tool/
├── app.py              # Main Streamlit application
├── requirements.txt    # Python dependencies
├── runtime.txt         # Python runtime version (for deployment)
├── README.md           # Project documentation
└── screenshots/        # UI screenshots
    └── ui.png
```

---

## ⚙️ How It Works

```
┌─────────────┐     ┌──────────────┐     ┌─────────────────┐     ┌──────────────┐
│  Input Text  │ ──▶ │  TextBlob    │ ──▶ │  Synonym Swap   │ ──▶ │  Humanized   │
│  (file/paste)│     │  Tokenizer   │     │  (WordNet + RNG) │     │  Output      │
└─────────────┘     └──────────────┘     └─────────────────┘     └──────────────┘
```

1. **Input** → Text is received via file upload or direct paste
2. **Tokenization** → TextBlob splits text into sentences and words
3. **Synonym Replacement** → For each word longer than 4 characters, a random check (based on the humanization level) decides whether to replace it with a WordNet synonym
4. **Output** → The reconstructed text is displayed and available for download

---

## 🤝 Contributing

Contributions are welcome! If you have ideas for improvements:

1. Fork the repository
2. Create a feature branch (`git checkout -b feature/amazing-feature`)
3. Commit your changes (`git commit -m 'Add amazing feature'`)
4. Push to the branch (`git push origin feature/amazing-feature`)
5. Open a Pull Request

---

## 📝 License

Distributed under the MIT License. See `LICENSE` for more information.

---

## 📬 Contact

**Barath M** — [@Mbarathm345672005](https://github.com/Mbarathm345672005)

Project Link: [https://github.com/Mbarathm345672005/ai-humanizer-tool](https://github.com/Mbarathm345672005/ai-humanizer-tool)

---

<p align="center">
  Made with ❤️ using Python & Streamlit
</p>
