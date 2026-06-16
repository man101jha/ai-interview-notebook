import os
from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.vectorstores import FAISS
from langchain_community.embeddings import HuggingFaceEmbeddings
from langchain_groq import ChatGroq
from langchain.chains import RetrievalQA
from langchain.prompts import PromptTemplate

# ---------------------------------------------------------
# 1. LOAD - Load documents from source
# ---------------------------------------------------------
def load_documents(file_path: str):
    loader = PyPDFLoader(file_path)
    documents = loader.load()
    return documents

# ---------------------------------------------------------
# 2. SPLIT - Chunk documents into smaller, overlapping pieces
# ---------------------------------------------------------
def split_documents(documents, chunk_size=500, chunk_overlap=50):
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=chunk_size,
        chunk_overlap=chunk_overlap,
        separators=["\n\n", "\n", ". ", " ", ""]
    )
    chunks = splitter.split_documents(documents)
    return chunks

# ---------------------------------------------------------
# 3. EMBED - Use open-source HuggingFace embedding model
#    (runs locally, no API cost)
# ---------------------------------------------------------
def get_embedding_model():
    return HuggingFaceEmbeddings(
        model_name="sentence-transformers/all-MiniLM-L6-v2"
    )

# ---------------------------------------------------------
# 4. INDEX - Build FAISS vector store from chunks
# ---------------------------------------------------------
def build_vectorstore(chunks, embedding_model, save_path="faiss_index"):
    vectorstore = FAISS.from_documents(chunks, embedding_model)
    vectorstore.save_local(save_path)
    return vectorstore

def load_vectorstore(embedding_model, save_path="faiss_index"):
    return FAISS.load_local(
        save_path, embedding_model, allow_dangerous_deserialization=True
    )

# ---------------------------------------------------------
# 5. RETRIEVE + GENERATE - RAG chain using Groq (Llama-3.3-70b)
# ---------------------------------------------------------
def build_rag_chain(vectorstore):
    llm = ChatGroq(
        groq_api_key=os.environ["GROQ_API_KEY"],
        model_name="llama-3.3-70b-versatile",
        temperature=0.2
    )

    retriever = vectorstore.as_retriever(search_kwargs={"k": 4})

    prompt_template = """Use the following context to answer the question.
If the answer isn't in the context, say you don't know — do not make up an answer.

Context:
{context}

Question: {question}

Answer:"""

    prompt = PromptTemplate(
        template=prompt_template,
        input_variables=["context", "question"]
    )

    qa_chain = RetrievalQA.from_chain_type(
        llm=llm,
        chain_type="stuff",
        retriever=retriever,
        chain_type_kwargs={"prompt": prompt},
        return_source_documents=True
    )
    return qa_chain

# ---------------------------------------------------------
# MAIN PIPELINE
# ---------------------------------------------------------
def main():
    file_path = "sample.pdf"

    print("Loading documents...")
    docs = load_documents(file_path)

    print("Splitting into chunks...")
    chunks = split_documents(docs)

    print("Loading embedding model...")
    embedding_model = get_embedding_model()

    print("Building vector store...")
    vectorstore = build_vectorstore(chunks, embedding_model)

    print("Building RAG chain with Groq...")
    qa_chain = build_rag_chain(vectorstore)

    query = "What is this document about?"
    result = qa_chain.invoke({"query": query})

    print("\nAnswer:", result["result"])
    print("\nSources:")
    for doc in result["source_documents"]:
        print("-", doc.metadata.get("source"), "page", doc.metadata.get("page"))

if __name__ == "__main__":
    main()