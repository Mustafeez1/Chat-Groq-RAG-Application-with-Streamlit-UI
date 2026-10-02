PDF RAG Chatbot with Groq, Ollama and FAISS
A Retrieval-Augmented Generation (RAG) chatbot built with
Streamlit, LangChain, Groq, Ollama, and FAISS.
This application allows users to ask questions about an internship
report PDF. The document is loaded and split into chunks, embeddings are
generated locally using Ollama, and the chunks are stored in a FAISS
vector database. When a user asks a question, relevant document content
is retrieved and provided to a Groq-powered LLM to generate a
context-based answer.
Features
- PDF document loading with PyPDFLoader
- Text chunking with RecursiveCharacterTextSplitter
- Local embeddings using Ollama nomic-embed-text
- FAISS vector database for similarity search
- Retriever-based question answering
- Groq LLM integration
- Streamlit interactive interface
- Context-only answer generation
- Display of retrieved document content
- Streamlit session state for the vector database
RAG Workflow
Internship Report PDF
        ↓
   PyPDFLoader
        ↓
 Document Content
        ↓
RecursiveCharacterTextSplitter
        ↓
   Text Chunks
        ↓
Ollama Embeddings
(nomic-embed-text)
        ↓
FAISS Vector Store
        ↓
    Retriever
        ↓
Retrieval Chain
        ↓
    Groq LLM
(openai/gpt-oss-120b)
        ↓
     Answer
Technologies Used
  Technology                       Purpose
  Python                           Application development
  Streamlit                        Web interface
  LangChain                        RAG pipeline
  Groq                             LLM inference
  Ollama                           Local embedding generation
  nomic-embed-text               Embedding model
  FAISS                            Vector similarity search
  PyPDFLoader                      PDF loading
  RecursiveCharacterTextSplitter   Text chunking
  python-dotenv                    Environment variable management
Project Structure
PDF-RAG-Chatbot/
│
├── Data/
│   └── Internship_Report.pdf
│
├── project.py
├── requirements.txt
├── .env
├── .gitignore
└── README.md
Do not commit API keys or .env to GitHub.

Installation
1. Clone the repository
git clone <your-github-repository-url>
cd <your-repository-name>
2. Create a virtual environment
python -m venv venv
Activate on macOS/Linux:
source venv/bin/activate
Windows:
venv\Scripts\activate
3. Install dependencies
pip install -r requirements.txt
If needed, install the integrations separately:
pip install langchain-groq langchain-ollama faiss-cpu
Ollama Setup
The project uses Ollama for local embeddings.
Make sure Ollama is installed and running, then pull the embedding
model:
ollama pull nomic-embed-text
The application uses:
OllamaEmbeddings(model="nomic-embed-text")
Groq API Setup
Create a .env file:
GROQ_API_KEY=your_groq_api_key
The application loads environment variables with load_dotenv().
Add the following to .gitignore:
.env
venv/
__pycache__/
.ipynb_checkpoints/
Never upload your actual API key to GitHub.
Run the Application
Start Streamlit:
streamlit run project.py
Then open the local Streamlit URL shown in the terminal.
How It Works
1. Generate embeddings
Click Generate Embeddings.
The application:
1. Loads Data/Internship_Report.pdf
2. Extracts its content
3. Splits the content into chunks
4. Generates embeddings using Ollama
5. Creates the FAISS vector store
2. Ask a question
Enter a question related to the internship report and click Answer.
For example:
What is the main objective of the internship?
3. Retrieve relevant context
The question is sent to the FAISS retriever:
retriever = st.session_state.vectors.as_retriever()
Relevant document chunks are retrieved.
4. Generate the answer
The retrieved context is passed to the document chain and Groq LLM:
document_context = create_stuff_documents_chain(
    model,
    prompt
)

retrieved_data = create_retrieval_chain(
    retriever,
    document_context
)
The response is generated with:
response = retrieved_data.invoke({
    "input": user_input
})
Prompt Design
The chatbot is instructed to answer using the retrieved context only. If
the information is not available in the context, it should respond:
I don't know
This helps keep the generated response focused on the contents of the
document.
Example Questions
What is the main objective of the internship?
What technologies were used during the internship?
What did I learn during the internship?
Explain the project mentioned in the report.
The questions should be related to information contained in the PDF.
Why RAG?
A normal LLM can generate an answer based on its learned knowledge.
A RAG application first retrieves relevant information from a specific
document and then gives that information to the LLM.
Question
   ↓
Retriever
   ↓
Relevant PDF Content
   ↓
LLM
   ↓
Context-based Answer
This makes RAG useful for document-based question answering.
Learning Outcomes
Through this project, I practiced:
- Retrieval-Augmented Generation
- PDF document loading
- Text splitting and chunking
- Embeddings
- Local embedding models
- Vector databases
- FAISS similarity search
- LangChain retrieval chains
- Groq LLM integration
- Prompt engineering
- Streamlit application development
- Session state management

Important Notes
- Ollama must be running locally.
- nomic-embed-text must be installed in Ollama.
- A valid Groq API key is required.
- The PDF path must match the application configuration.