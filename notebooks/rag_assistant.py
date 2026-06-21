import os

kb_path = os.path.join(
    os.path.dirname(os.path.dirname(__file__)),
    "knowledge_base",
    "incident_playbook.txt"
)

with open(kb_path, "r", encoding="utf-8") as file:
    knowledge = file.read()

question = input("Describe the issue: ").lower()

print("\n===== RETRIEVAL RESULTS =====\n")

sections = knowledge.split("------------------------------------------------")

found = False

for section in sections:

    if any(word in section.lower() for word in question.split()):

        print(section)
        found = True

if not found:
    print("No matching guidance found.")