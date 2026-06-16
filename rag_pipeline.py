import os

def load_documents(folder):
    docs = []

    for file in os.listdir(folder):

        if file.endswith(".txt"):

            with open(
                os.path.join(folder, file),
                "r",
                encoding="utf-8"
            ) as f:

                text = f.read()

            docs.append({
                "file": file,
                "text": text
            })

    return docs


def generate_answer(question):

    docs = load_documents("data")

    context = ""

    for doc in docs:
        context += doc["text"] + "\n"

    question = question.lower()

    for doc in docs:
        if any(word in doc["text"].lower() for word in question.split()):
            return context, doc["text"]

    return context, "No relevant policy found."
