import requests

def semantic_scholar_search(query, max_results=5):
    url = f"https://api.semanticscholar.org/graph/v1/paper/search"
    params = {
        "query": query,
        "limit": max_results,
        "fields": "title,authors,url,abstract,year,citationCount"
    }
    response = requests.get(url, params=params)
    data = response.json()
    papers = []
    for paper in data.get("data", []):
        papers.append({
            "title": paper.get("title"),
            "authors": ", ".join([a["name"] for a in paper.get("authors", [])]),
            "abstract": paper.get("abstract"),
            "year": paper.get("year"),
            "citations": paper.get("citationCount"),
            "link": paper.get("url")
        })
    return papers