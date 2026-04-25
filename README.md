# Agentic-AI
# Deep Research Agent

# A Python-based agentic AI system that conducts comprehensive research using LLMs, web search, and iterative reflection patterns.

# Overview

# This project demonstrates the difference between non-agentic (single-pass) and agentic (multi-step, iterative) AI workflows for research tasks. The agent can:

• Generate targeted search queries from a research goal
• Search the web for real-time information
• Fetch and extract content from URLs
• Summarize findings from multiple sources
• Self-critique and revise its own work
• Produce comprehensive, source-backed reports

# Key Features

| Feature | Description |
|---------|-------------|
| Task Decomposition | Breaks complex research into LLM, code, and tool steps |
| Tool Integration | Web search (DuckDuckGo) and URL content extraction |
| Reflection Pattern | Generate → Critique → Revise loop for quality improvement |
| Source Citation | Reports include verifiable sources and links |

Installation

``bash
Clone the repository
git clone https://github.com/yourusername/deep-research-agent.git
cd deep-research-agent

Install dependencies
pip install requests beautifulsoup4 duckduckgo-search
`

Quick Start

`python
from researchagent import researchwithtools, reflectionloop

Define your research goal
researchgoal = "How to build a retail company that competes with DMART in India"

Run the research pipeline
summaries = researchwithtools(researchgoal, numqueries=3)

Generate and refine report
initialreport = generatereport(summaries)
finalreport = reflectionloop(initialreport, researchgoal, maxiterations=2)
`

# Architecture

`
┌─────────────────────────────────────────────────────────────┐
│                         INPUT                                │
│            Research goal / question                          │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│              STEP 1: Generate Search Queries [LLM]           │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│              STEP 2: Web Search [TOOL]                       │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│              STEP 3: Fetch URL Content [TOOL]                │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│              STEP 4: Summarize Sources [LLM]                 │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│              STEP 5: Write Report Draft [LLM]                │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│              STEP 6: Critique [LLM]                          │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│              STEP 7: Revise [LLM]                            │
└─────────────────────────────────────────────────────────────┘
                              │
                              ▼
┌─────────────────────────────────────────────────────────────┐
│                         OUTPUT                               │
│            Final research report with sources                │
└─────────────────────────────────────────────────────────────┘
`

# Non-Agentic vs Agentic Comparison

| Aspect | Non-Agentic | Agentic |
|--------|-------------|---------|
| LLM Calls | 1 | 8-10 |
| Has Real Sources | No | Yes |
| Word Count | ~250 | ~1,800 |
| Actionable Insights | Low | High |
| Verifiable Claims | No | Yes |

Core Components
Query Generator

`python
def generatesearchqueries(researchgoal, numqueries=5):
    """Use LLM to generate effective search queries."""
    # Returns specific, diverse queries targeting different aspects
`

Web Search Tool

`python
def websearch(query, maxresults=5):
    """Search the web using DuckDuckGo."""
    # Returns titles, URLs, and snippets
`

URL Fetcher

`python
def fetchurl(url, maxchars=5000):
    """Fetch and extract text content from a URL."""
    # Cleans HTML and extracts readable text
`

Reflection Loop

`python
def reflectionloop(initialreport, researchgoal, maxiterations=2):
    """Run multiple critique-revise iterations."""
    # Improves report quality through self-critique
`

The Decomposition Heuristic

For each step in your agent, ask:

> "Can this step be done by an LLM, code, or a tool?"

• YES → Execute with that component
• NO → Decompose further

# Example

Bad decomposition:
Research the topic
Write a report

Good decomposition:
Generate search queries [LLM]
Search the web [TOOL]
Fetch URL content [TOOL]
Summarize sources [LLM]
Write report draft [LLM]
Critique the report [LLM]
Revise based on critique [LLM]

When to Use Reflection

Reflection helps most when:
• Output is complex (reports, essays, code)
• Quality matters more than speed
• First draft likely has gaps
• You have specific criteria to check

Reflection helps less when:
• Task is simple (single fact lookup)
• Speed is critical (real-time chat)
• Task has a clear right answer

Requirements
• Python 3.8+
• requests
• beautifulsoup4
• duckduckgo-search
• Access to an LLM API (Google Colab AI, OpenAI, etc.)

# Project Structure

`
deep-research-agent/
├── README.md
├── requirements.txt
├── researchagent.py      # Core agent implementation
├── tools/
│   ├── websearch.py      # DuckDuckGo search wrapper
│   └── urlfetcher.py     # Content extraction
├── patterns/
│   ├── decomposition.py   # Task breakdown utilities
│   └── reflection.py      # Critique-revise loop
└── examples/
    └── dmartresearch.py  # Complete example
`

Contributing
Fork the repository
Create a feature branch (git checkout -b feature/new-tool)
Commit changes (git commit -am 'Add new tool')
Push to branch (git push origin feature/new-tool`)
Open a Pull Request

Acknowledgments
• Course: Introduction to Agentic AI Systems
• Instructor: Lokesh Dange
