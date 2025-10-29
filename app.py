import streamlit as st
from scraper import semantic_scholar_search
from nlp_utils import extract_keywords, summarize_abstract

st.set_page_config(page_title="Research Paper Finder", layout="wide")
st.title("🔍 Research Paper Finder")
st.markdown("Enter a topic or title to find related papers from Semantic Scholar.")

query = st.text_input("Enter your research topic:")
max_results = st.slider("Number of papers", 1, 15, 5)

if query:
    with st.spinner("Searching papers..."):
        results = semantic_scholar_search(query, max_results)
    for paper in results:
        st.subheader(paper['title'])
        st.write(f"👥 **Authors**: {paper['authors']}")
        st.write(f"📅 **Year**: {paper['year']} | 📈 **Citations**: {paper['citations']}")
        st.write(f"🔗 [View Paper]({paper['link']})")
        st.write(f"📝 **Abstract**: {paper['abstract']}")
        st.write(f"📌 **Keywords**: {', '.join(extract_keywords(paper['abstract']))}")
        st.write(f"🧠 **Summary**: {summarize_abstract(paper['abstract'])}")
        st.markdown("---")