from openai import OpenAI
import os

client = OpenAI(
    api_key="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"
)

kb_path = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "knowledge_base",
    "incident_playbook.txt"
)

with open(kb_path, "r", encoding="utf-8") as file:
    knowledge = file.read()

issue = input("Describe the issue: ")

prompt = f"""
You are a Data Quality AI Agent.

Knowledge Base:
{knowledge}

Issue:
{issue}

Provide:

1. Root Cause Analysis
2. Business Impact
3. Recommended Actions
4. Priority Level
"""

response = client.responses.create(
    model="gpt-5",
    input=prompt
)

print("\n===== AI RECOMMENDATION =====\n")
print(response.output_text)