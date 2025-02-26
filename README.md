# AI-pdf-reader
Ask your PDF 💬 : 
A Streamlit application that extracts text from a PDF file and answers questions based on the extracted text.



Description : 
This Python script utilizes several libraries and modules to create a Streamlit application for processing PDF files. It extracts text from the uploaded PDF, splits it into chunks, and builds a knowledge base for question answering. Users can ask questions about the PDF content, and the application provides answers based on the extracted text.



Features : 
Upload PDF files to extract text from them.
Perform text extraction and chunking for efficient question answering.
Utilize OpenAI embeddings for text processing.
Use a question-answering chain for answering user questions.
Display answers in the Streamlit app interface.


Installation : 
Clone the repository: 
git clone https://github.com/CodeThat/Langchain-Chat-PDF.git



Change to the project directory :
cd your-repository



Create a virtual environment (optional but recommended) : 
python -m venv venv
source venv/bin/activate
Install the required dependencies:
pip install -r requirements.txt



Usage : 
Make sure you have activated the virtual environment (if created).

Run the script: python script.py

Open your web browser and navigate to the provided local URL (e.g., http://localhost:8501).

Upload a PDF file using the file uploader in the Streamlit app.

Enter your question about the PDF content in the provided text input.

View the answer displayed in the app interface.


License : 
This project is licensed under the MIT License.



TODO : 
Add functionality to parse more doc types using langchain.



Acknowledgments : 
Streamlit - The web application framework used for building the user interface.
PyPDF2 - A library for reading PDF files.
OpenAI - The language model and embeddings used in the script.
LangChain - The library for text splitting, embeddings, vector stores, and question answering.
FAISS a library that allows us to quickly search for multimedia documents that are similar to each other
