# AI Engineering Projects & Labs

Hands-on work from the IBM AI Engineering Professional Certificate (Coursera), covering the full stack from classical deep learning foundations through transformers, fine-tuning, RLHF, and applied RAG systems — capped by a deployed retrieval-augmented chatbot as the capstone.

## Capstone: Watsonx RAG Document Q&A Bot (`qabot.py`)

An end-to-end RAG application: upload a PDF, ask a question, get an answer grounded in the document.

- **Pipeline:** `PyPDFLoader` → `RecursiveCharacterTextSplitter` → Chroma vector store → IBM watsonx embeddings (`granite-embedding-278m-multilingual`) → `RetrievalQA` chain
- **LLM:** IBM watsonx.ai (`granite-4-h-small`) via `langchain_ibm`
- **Interface:** Gradio, deployed with file upload + query input
- **Notable debugging:** resolved a three-way `numpy`/`scipy`/`chromadb` dependency conflict, and worked around a sandboxed lab environment blocking outbound access needed for an earlier dataset download

## Labs by area

### Neural network foundations

- Artificial Neural Networks — Forward Propagation
- Backpropagation
- Activation Functions and Vanishing Gradients
- Implementing the Functional API in Keras
- Creating Custom Layers and Models (Keras)

### Transformer architecture

- Self-Attention and Positional Encoding
- Pretraining BERT Models (encoder) — "Baby BERT"
- Decoder Causal Language Models (GPT-like)
- Data Loading and Text Processing for BERT
- Applying Transformers for Classification
- Creating an NLP Data Loader

### Fine-tuning & parameter-efficient methods

- Fine-Tuning Transformers with PyTorch and Hugging Face
- Adapters in PyTorch
- LoRA with PyTorch — sentiment fine-tuning on IMDB from an AG News-pretrained base
- Pre-Training and Fine-Tuning with PyTorch — movie-review recommender system
- Instruction-Tuning with LLMs
- Loading Models and Inference with Hugging Face
- Optional: Pre-training LLMs with Hugging Face

### Reinforcement learning from human feedback

- PPOTrainer — RLHF using Proximal Policy Optimization

### Retrieval-augmented generation & LangChain

- Load Documents Using LangChain for Different Sources
- Apply Text Splitting Techniques to Enhance Model Responsiveness
- Create and Configure a Vector Database to Store Document Embeddings
- Develop a Retriever to Fetch Document Segments Based on Queries
- Put Whole Document into Prompt and Ask the Model — retrieval limitations
- Embed Documents Using watsonx's Embedding Model
- Build Smarter AI Apps: Empower LLMs with LangChain
- RAG with Hugging Face
- RAG with PyTorch — content-appropriateness classifier for songs
- Summarize Private Documents Using RAG, LangChain, and LLMs

### AI agents

- Building AI Agents from Scratch — Weather Agent

### Applied UI / deployment practice

- `qabot.py` — capstone RAG chatbot (Gradio)
- `llm_chat.py` — watsonx LLM chat interface (Gradio)
- `gradio_demo.py`, `Gradio_text.py`, `Input_type_development.py` — Gradio input/output component practice

## Tech stack

**Languages/frameworks:** Python, PyTorch, TensorFlow/Keras, Hugging Face Transformers
**LLM tooling:** LangChain, IBM watsonx.ai, ChromaDB, Gradio
**Techniques covered:** forward/backpropagation, transformer architectures (encoder/decoder), fine-tuning (full, adapters, LoRA), instruction-tuning, RLHF (PPO), retrieval-augmented generation

## Structure

Each topic area above corresponds to a branch; `main` holds the capstone and this README. See individual notebooks for setup instructions and IBM Skills Network lab-specific notes.
