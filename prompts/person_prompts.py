INITIAL_PROMPT = """You are an expert in extracting structured information from government gazettes. Carefully analyze the text and extract all personnel appointments.

### Instructions:
1. **Only extract appointments and resignations** (no resignations/terminations unless explicitly stated).
2. Include:
   - Full names
   - Ministries/portfolios
   - Position (Minister/State Minister/Deputy Minister/Secretary/Prime Minister)
   - Gazette date in YYYY-MM-DD format

Wrap your response in a single line of valid JSON. Do not return incomplete objects or extra text.
Output valid, clean JSON only — no markdown, comments, or natural language.
### Required Output Format (Compact JSON):

Appoinments include in "ADD" and Resignations include in "TERMINATE"
```json
{{
  "ADD": [
    {{
      "name": "Full Name",
      "Ministry": "Ministry Name",
      "date": "YYYY-MM-DD",
      "position": "Minister|State Minister|Deputy Minister|Secretary|Prime Minister"
    }}
  ],
  "TERMINATE": [
    {{
      "name": "Full Name",
      "Ministry": "Ministry Name",
      "date": "YYYY-MM-DD",
      "position": "Minister|State Minister|Deputy Minister|Secretary|Prime Minister"
    }}]
}}



Now process this gazette text:
{docs}"""