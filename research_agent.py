import requests
# ============================================
# SETUP - Do not modify
# ============================================
def ask_ollama(prompt, model="gemma3:4b"):
    """Send prompt to Ollama and get response"""
    response = requests.post(
    "http://localhost:11434/api/generate",
    json={
        "model": model,
        "prompt": prompt,
        "stream": False,
        "options": {
            "num_predict": 500
        }
    }
)
    data = response.json()
    return data.get("response", data.get("message", str(data)))
# ============================================
# STEP 0: COLLECT YOUR PROFILE

# ============================================
print("=" * 60)
print("PERSONALIZED CAREER RESEARCH AGENT")
print("=" * 60)
name = input("\nEnter your name: ")
print("\nCareer Interest Options:")
print(" 1. AI/ML & Data Science")
print(" 2. VLSI & Chip Design")
print(" 3. Embedded Systems & IoT")
print(" 4. Software Development")
print(" 5. Robotics & Automation")
print(" 6. Core Electronics & Hardware")
print(" 7. Not sure yet (explore all options)")
choice = input("\nEnter your choice (1-7): ")
career_options = {
"1": "AI/ML & Data Science",
"2": "VLSI & Chip Design",
"3": "Embedded Systems & IoT",
"4": "Software Development",
"5": "Robotics & Automation",
"6": "Core Electronics & Hardware",
"7": "Not sure yet"
}
career_interest = career_options.get(choice, "Not sure yet")
# Set the topic based on interest
if career_interest == "Not sure yet":
    TOPIC = "Exploring All Career Options for ECE Graduates (Graduating 2028)"
    CONTEXT = f"{name} is a 2nd year ECE student (graduating in 2028) who is unsure about their career direction and wants to explore all available options."
else:
    TOPIC = f"Career Path in {career_interest} for ECE Graduates (Graduating 2028)"
    CONTEXT = f"{name} is a 2nd year ECE student (graduating in 2028) interested in {career_interest} and wants to know how to build a career in this field."
print(f"\nHello {name}!")
print(f"Career Interest: {career_interest}")

print(f"\nResearching: {TOPIC}")
print("=" * 60)
# ------------------------------------------
# STEP 1: PLANNING (Example provided)
# ------------------------------------------
print("\n>>> STEP 1: PLANNING")
print("-" * 40)
if career_interest == "Not sure yet":
    planning_prompt = f"""
{CONTEXT}
Generate 5 search queries to help {name} explore different career paths:
- Compare different career options for ECE graduates
- Salary and growth prospects in different fields
- Skills required for various career paths
- How to discover your career interest
- Emerging fields for ECE graduates in 2028
Return ONLY the queries, one per line, no numbering.
"""
else:
    planning_prompt = f"""
{CONTEXT}
Generate 5 search queries to research {career_interest} careers:
- Job roles in {career_interest} for ECE graduates
- Skills and tools needed for {career_interest}
- Companies hiring for {career_interest} in India
- Career growth path in {career_interest}
- How to prepare for {career_interest} while in college
Return ONLY the queries, one per line, no numbering.
"""
queries = ask_ollama(planning_prompt)
print(queries)
# ------------------------------------------
# STEP 2: INITIAL DRAFT
# ------------------------------------------
print("\n>>> STEP 2: INITIAL DRAFT")
print("-" * 40)
# TODO: Write your prompt here

# Use CONTEXT, TOPIC, name, career_interest, and queries
# Make the report personalized to the student
draft_prompt = f"""
{CONTEXT}

Topic: {TOPIC}

Using these research angles: {queries}

Write a personalized career research report for {name}. Address them directly. Focus on {career_interest}. Include: key roles, skills needed, companies in India, growth path, and how to prepare in college (graduating 2028). Keep it clear and actionable (about 300-400 words).
"""

draft = ask_ollama(draft_prompt)
print(draft)
# ------------------------------------------
# STEP 3: CRITIQUE
# ------------------------------------------
print("\n>>> STEP 3: CRITIQUE")
print("-" * 40)
# TODO: Write your prompt here
# Critique should check if the report is helpful for THIS specific student
# Include the draft in your prompt
critique_prompt = f"""
You are reviewing a career report for {name}, a 2nd year ECE student (graduating 2028) interested in {career_interest}.

DRAFT REPORT:
{draft}

Critique the draft in 3-5 short points: Is it useful for {name}? Does it address {career_interest} specifically? Is the advice actionable for a 2nd year student? What is missing or could be improved? Be specific.
"""

critique = ask_ollama(critique_prompt)
print(critique)
# ------------------------------------------
# STEP 4: REVISE
# ------------------------------------------
print("\n>>> STEP 4: REVISE")
print("-" * 40)
# TODO: Write your prompt here
# Include BOTH the draft AND the critique
# Make the final report personalized and actionable
revise_prompt = f"""
{CONTEXT}

ORIGINAL DRAFT:
{draft}

CRITIQUE:
{critique}

Revise the report based on the critique. Address {name} directly. Include specific next steps for {career_interest}. Make it feel like personal advice for a 2nd year ECE student graduating in 2028. Output the final report only (no meta-commentary).
"""

final_report = ask_ollama(revise_prompt)
print(final_report)
# ------------------------------------------
# COMPLETE
# ------------------------------------------
print("\n" + "=" * 60)
print(f"RESEARCH COMPLETE FOR: {name}")
print(f"CAREER FOCUS: {career_interest}")
print("=" * 60)