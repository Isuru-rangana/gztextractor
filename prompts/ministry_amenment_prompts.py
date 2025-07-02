INITIAL_PROMPT = """
You are analyzing a Sri Lankan Government Gazette notification that lists amendments to existing ministerial assignments, institutions, and laws.

Your task is to extract **all changes** into a structured JSON array.

Each change must include:
- `ministry_name`: The full name of the ministry the change refers to.
- `change_type`: One of the following:
  - "ADD" — for inserted items or additions
  - "OMIT" — for omitted or removed items
  - "RENUMBER" — for renumbered item ranges
- `affected_column`: The column the change applies to:
  - "I" → Duties & Functions
  - "II" → Departments, Statutory Institutions, or Public Corporations
  - "III" → Laws and Ordinances to be Implemented
- `details`: A list of text descriptions that summarize the specific changes (e.g., “Omitted item 11”, “Inserted: Department of Immigration”, “Renumbered items 10–13 as 11–14”)

Wrap your response in a single line of valid JSON. Do not return incomplete objects or extra text.
### Use the following flat JSON array format:
[
  {{
    "ministry_name": "string",
    "change_type": "ADD" | "OMIT" | "RENUMBER",
    "affected_column": "I" | "II" | "III",
    "details": ["string", ...]
  }}
]

        TEXT:

        {docs}

        """