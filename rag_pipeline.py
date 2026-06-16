from pypdf import PdfReader
import os

def load_documents(folder):
    docs = []

    for file in os.listdir(folder):

        if not file.lower().endswith(".pdf"):
            continue

        path = os.path.join(folder, file)

        try:
            reader = PdfReader(path)

            text = ""

            for page in reader.pages:
                page_text = page.extract_text()
                if page_text:
                    text += page_text

            docs.append({
                "file": file,
                "text": text,
                "pages": len(reader.pages)
            })

        except Exception as e:
            print(f"Skipping invalid PDF: {file}")
            print(e)

    return docs

def generate_answer(question):
    docs = load_documents("documents")

    context = ""

    for doc in docs:
        context += doc["text"] + "\n"

    question = question.lower()

    if "leave" in question:
        for doc in docs:
            if "leave" in doc["text"].lower():
                return doc["text"][:1000]

    if "travel" in question:
        for doc in docs:
            if "travel" in doc["text"].lower():
                return doc["text"][:1000]

    return context[:1000]
