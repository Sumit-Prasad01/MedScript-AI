# 🏥 MedScript-AI - Medical RAG ChatBot

MedScript-AI is a Retrieval-Augmented Generation (RAG) based
conversational medical chatbot designed to answer user medical queries
using trusted Medical Encyclopedia PDF data.

The system leverages modern LLM infrastructure including Groq (LLaMA
3.1), LangChain, Hugging Face Embeddings, and FAISS for efficient
semantic search.

In addition to retrieval-based responses, the chatbot maintains **chat
history context**, enabling multi-turn conversations with contextual
understanding.

------------------------------------------------------------------------

## 🚀 Features

-   🔎 Retrieval-Augmented Generation (RAG) Architecture
-   🤖 Groq LLaMA 3.1 for fast LLM inference
-   📚 Medical Encyclopedia PDF as knowledge base
-   🧠 Hugging Face Embeddings for semantic vector generation
-   ⚡ FAISS Vector Store for similarity search
-   💬 Conversational memory with Chat History Context
-   🧵 Multi-turn contextual responses
-   🌐 Flask backend API
-   🎨 HTML + Tailwind CSS responsive UI
-   🐳 Dockerized application
-   🔄 CI/CD using Jenkins
-   ☁️ Deployed on AWS Runner
-   📦 Container images stored in AWS ECR

------------------------------------------------------------------------

## 🏗️ Project Architecture

User Query\
→ Flask API\
→ LangChain Conversational Retrieval Chain\
→ FAISS Vector Store (Context Retrieval)\
→ Chat History Memory Injection\
→ Groq LLaMA 3.1\
→ Final Context-Aware Response\
→ UI Display

------------------------------------------------------------------------

## 🧠 Conversational Memory

The chatbot uses LangChain's conversational memory mechanism to:

-   Store previous user queries
-   Maintain assistant responses
-   Inject chat history into LLM prompt
-   Enable follow-up questions like:
    -   "What are its symptoms?"
    -   "How is it treated?"
    -   "Is it dangerous?"

This allows contextual understanding instead of isolated Q&A responses.

------------------------------------------------------------------------

## 📂 Project Structure

    app/
     ├── components/
     │    ├── data_ingestion.py
     │    ├── data_loader.py
     │    ├── embeddings.py
     │    ├── llm.py
     │    ├── pdf_loader.py
     │    ├── retriever.py
     │    ├── vector_store.py
     │    └── memory.py (chat history logic)
     ├── config/
     ├── templates/
     └── application.py

    custom_jenkins/
    data/
    logs/
    vectorstore/
    Dockerfile
    Jenkinsfile
    requirements.txt
    setup.py

------------------------------------------------------------------------

## 🧠 Core Technologies

  Component            Technology Used
  -------------------- ---------------------------------
  LLM                  Groq (LLaMA 3.1)
  Framework            LangChain
  Embeddings           Hugging Face
  Vector DB            FAISS
  Memory               LangChain Conversational Memory
  Backend              Flask
  Frontend             HTML + Tailwind CSS
  Containerization     Docker
  CI/CD                Jenkins
  Cloud Deployment     AWS Runner
  Container Registry   AWS ECR

------------------------------------------------------------------------

## 🔧 Installation & Setup

### 1️⃣ Clone Repository

    git clone https://github.com/Sumit-Prasad01/MedScript-AI.git
    cd MedScript-AI

### 2️⃣ Create Virtual Environment

    python -m venv venv
    venv\Scripts\activate

### 3️⃣ Install Dependencies

    pip install -r requirements.txt

### 4️⃣ Add Environment Variables

Create a `.env` file:

    GROQ_API_KEY=your_groq_api_key

------------------------------------------------------------------------

## ▶️ Run Application Locally

    python app/application.py

Access at:

    http://localhost:5000

------------------------------------------------------------------------

## 🐳 Docker Setup

### Build Image

    docker build -t medscript-ai .

### Run Container

    docker run -p 5000:5000 medscript-ai

------------------------------------------------------------------------

## 🔄 CI/CD Pipeline (Jenkins)

1.  Code pushed to GitHub
2.  Jenkins pipeline triggers build
3.  Docker image built
4.  AquaTrivy security scan
5.  Image pushed to AWS ECR
6.  Deployment to AWS Runner

------------------------------------------------------------------------

## ☁️ Deployment Architecture

GitHub\
→ Jenkins CI/CD\
→ Docker Build\
→ Security Scan\
→ AWS ECR\
→ AWS Runner Deployment

------------------------------------------------------------------------

## 📌 Future Enhancements

-   Persistent database-backed chat history (Redis/PostgreSQL)
-   Multi-document medical corpus support
-   User authentication
-   Deployment on Kubernetes (EKS)
-   Role-based access control
-   Advanced prompt optimization
-   Medical disclaimer banner & emergency detection logic

------------------------------------------------------------------------

## ⚠️ Disclaimer

This chatbot provides informational responses based on medical
encyclopedia data.\
It is not a substitute for professional medical advice, diagnosis, or
treatment.

Always consult a qualified healthcare professional for medical concerns.

------------------------------------------------------------------------



