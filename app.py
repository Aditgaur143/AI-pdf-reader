from dotenv import load_dotenv
import streamlit as st
from PyPDF2 import PdfReader
from langchain.text_splitter import CharacterTextSplitter
from langchain.embeddings.openai import OpenAIEmbeddings
from langchain.vectorstores import FAISS
from langchain.chains.question_answering import load_qa_chain
from langchain.llms import OpenAI
from langchain.callbacks import get_openai_callback


def extract_text_from_pdf(pdf):
    """Extract text from uploaded PDF file."""
    pdf_reader = PdfReader(pdf)
    return "\n".join(page.extract_text() or "" for page in pdf_reader.pages)


def process_text(text):
    """Split text into manageable chunks and create vector embeddings."""
    if not text.strip():
        return None

    text_splitter = CharacterTextSplitter(separator="\n", chunk_size=1000, chunk_overlap=200, length_function=len)
    chunks = text_splitter.split_text(text)
    embeddings = OpenAIEmbeddings()
    return FAISS.from_texts(chunks, embeddings)


def answer_question(knowledge_base, user_question):
    """Search for relevant documents and generate an answer."""
    if not knowledge_base:
        return "Error: No valid content extracted from the PDF."

    docs = knowledge_base.similarity_search(user_question)
    llm = OpenAI()
    chain = load_qa_chain(llm, chain_type="stuff")

    with get_openai_callback() as cb:
        response = chain.run(input_documents=docs, question=user_question)
        print(cb)

    return response


def main():
    load_dotenv()
    st.set_page_config(page_title="Ask your PDF", page_icon="🧊")
    st.header("Ask your PDF 💬")

    pdf = st.file_uploader("Upload your PDF", type="pdf")

    if pdf:
        text = extract_text_from_pdf(pdf)
        knowledge_base = process_text(text)

        if knowledge_base:
            user_question = st.text_input("Ask a question about your PDF:")
            if user_question:
                response = answer_question(knowledge_base, user_question)
                st.write(response)
        else:
            st.error("No text could be extracted from the PDF. Try a different file.")


if __name__ == '__main__':
    main()
