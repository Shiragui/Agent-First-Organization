import os 
from arklex.env.tools.tools import register_tool 
from tavily import TavilyClient

@register_tool(
    "Provides an explanation of a given ETF using Tavily API.",
    [{
        "name": "etf",
        "type": "string",
        "description": "name or ticker of the ETF",
        "prompt": "What ETF would you like to know about?",
        "required": True
    }],
    [{
        "name": "result",
        "type": "string",
        "value": "",
        "description": "an overview of the ETF and its performance",
    }]
)

def etf_tool(etf):
    client = TavilyClient(api_key=os.getenv("TAVILY_API_KEY"))
    query = f"{etf} ETF overview"
    try:
        response = client.search(query, search_depth="basic", include_answer=True)
        return response["answer"]
    except Exception as e:
        return f"Error: {str(e)}"

