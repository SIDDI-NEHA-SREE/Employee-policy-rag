import streamlit as st
from rag_pipeline import generate_answer

st.title(
    "Employee Policy Assistant"
)

question = st.text_input(
    "Ask a policy question"
)

if st.button("Search"):

    context,answer = generate_answer(
        question
    )

    st.subheader(
        "Retrieved Context"
    )

    st.write(context)

    st.subheader(
        "Answer"
    )

    st.write(answer)
