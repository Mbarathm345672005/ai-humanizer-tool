import streamlit as st
import nltk
from textblob import TextBlob
from nltk.corpus import wordnet
import random
from PyPDF2 import PdfReader
from docx import Document
import io

# Page Configuration
st.set_page_config(page_title="Humanizer Pro (NLTK)", page_icon="🧬")

# --- 1. Load Resources (Cached) ---
@st.cache_resource
def setup_nltk():
    # Download necessary NLTK data
    resources = ['punkt', 'wordnet', 'omw-1.4', 'averaged_perceptron_tagger', 'punkt_tab']
    for r in resources:
        try:
            nltk.data.find(f'tokenizers/{r}')
        except LookupError:
            nltk.download(r, quiet=True)
        except ValueError:
            # Fallback for corpora like wordnet
            nltk.download(r, quiet=True)

setup_nltk()

# --- 2. Logic Functions ---

def get_synonym(word):
    """
    Finds a synonym for a word. Returns the original word if none found.
    """
    synonyms = set()
    for syn in wordnet.synsets(word):
        for lemma in syn.lemmas():
            candidate = lemma.name().replace("_", " ")
            # Avoid using the same word or just capitalization changes
            if candidate.lower() != word.lower():
                synonyms.add(candidate)
    
    if synonyms:
        return random.choice(list(synonyms))
    return word

def humanize_text_logic(text, replace_prob=0.3):
    """
    Replaces words with synonyms based on a probability.
    Increasing replace_prob makes it more 'human' (random) but less readable.
    """
    blob = TextBlob(text)
    output_sentences = []
    
    for sentence in blob.sentences:
        new_words = []
        # TextBlob breaks punctuation, so this is a simple reconstruction
        for word in sentence.words:
            # We only replace longer words (likely adjectives/verbs/nouns)
            # to keep the sentence structure intact.
            if len(word) > 4 and random.random() < replace_prob:
                new_words.append(get_synonym(word))
            else:
                new_words.append(word)
        # Join words and add a rough period if missing (simple reconstruction)
        output_sentences.append(" ".join(new_words))
        
    return ". ".join(output_sentences)

def extract_text_from_file(uploaded_file):
    text = ""
    try:
        if uploaded_file.name.endswith('.pdf'):
            reader = PdfReader(uploaded_file)
            for page in reader.pages:
                text += page.extract_text() + "\n"
        elif uploaded_file.name.endswith('.docx'):
            doc = Document(uploaded_file)
            for para in doc.paragraphs:
                text += para.text + "\n"
        elif uploaded_file.name.endswith('.txt'):
            text = uploaded_file.read().decode("utf-8")
    except Exception as e:
        st.error(f"Error reading file: {e}")
    return text

def create_docx(text):
    doc = Document()
    for paragraph in text.split('\n'):
        if paragraph.strip():
            doc.add_paragraph(paragraph)
    buffer = io.BytesIO()
    doc.save(buffer)
    buffer.seek(0)
    return buffer

# --- 3. The UI ---
st.title("🧬 AI Text Humanizer (NLTK Mode)")
st.markdown("This version uses **synonym swapping** to break AI patterns. It effectively lowers AI detection scores.")

# Settings Sidebar
st.sidebar.header("Settings")
randomness = st.sidebar.slider("Humanization Level (Randomness)", 0.1, 0.5, 0.25, 
                               help="Higher = less AI detection, but potentially grammar errors.")

# Tabs
tab1, tab2 = st.tabs(["📂 Upload File", "✍️ Paste Text"])

input_text = ""

with tab1:
    uploaded_file = st.file_uploader("Choose a file", type=['pdf', 'docx', 'txt'])
    if uploaded_file:
        with st.spinner("Reading file..."):
            input_text = extract_text_from_file(uploaded_file)
            st.info(f"Loaded {len(input_text.split())} words.")

with tab2:
    text_input = st.text_area("Paste text here", height=200)
    if not uploaded_file and text_input:
        input_text = text_input

if st.button("Humanize Text", type="primary"):
    if input_text:
        with st.spinner("Humanizing..."):
            # Run the synonym logic
            final_text = humanize_text_logic(input_text, replace_prob=randomness)
            
            st.success("Done!")
            
            st.subheader("Result:")
            st.text_area("Output", value=final_text, height=200)
            
            col1, col2 = st.columns(2)
            with col1:
                st.download_button("⬇️ Download .txt", final_text, "humanized.txt", "text/plain")
            with col2:
                docx = create_docx(final_text)
                st.download_button("⬇️ Download .docx", docx, "humanized.docx", 
                                   "application/vnd.openxmlformats-officedocument.wordprocessingml.document")
    else:
        st.warning("Please provide some text.")