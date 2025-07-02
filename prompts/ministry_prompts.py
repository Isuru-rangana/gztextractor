# INITIAL_PROMPT = """
# You are an expert data extractor.

# Your task is to extract structured information for **each ministry** in the document, including:

# - Column I: "Subjects and Functions"
# - Column II: "Departments, Statutory Institutions and Public Corporations"
# - Column III: "Laws, Acts and Ordinances to be Implemented"

# ### OUTPUT FORMAT (JSON):
# {
#   "ministers": [
#     {
#       "name": "Full Ministry Name",
#       "subjects_and_functions": [
#         "Subject/Function 1",
#         "Subject/Function 2",
#         ...
#       ],
#       "departments": [
#         "Department or Institution 1",
#         "Department or Institution 2",
#         ...
#       ],
#       "laws_and_ordinances": [
#         "Law/Act/Ordinance 1",
#         "Law/Act/Ordinance 2",
#         ...
#       ]
#     }
#   ]
# }

# ### STRICT EXTRACTION RULES:
# 1. For each ministry, extract ONLY the data shown in each of the 3 columns (Column I, II, III).
# 2. Maintain the **exact order and wording** of each entry as in the document. Don't paraphrase or summarize.
# 3. Preserve **capitalization and spelling** as in the source text (e.g., “sri Lanka Army” not “Sri Lanka Army”).
# 4. Remove numbering (e.g., "1.", "2.") from list items, but **retain bullet points or hyphens** only if they are part of the name.
# 5. Include ministries spread over **multiple pages**. Use continuation content.
# 6. Return valid, clean JSON only — no explanations or extra text.

# Now extract and format the data from the following document:

# Content to extract from:
# {docs}
# """

INITIAL_PROMPT = """
You are an assistant extracting structured data from an official Sri Lankan Government Gazette.

Each ministry includes three columns:
- Column I: "Subjects and Functions"
- Column II: "Departments, Statutory Institutions and Public Corporations"
- Column III: "Laws, Acts and Ordinances to be Implemented"

Your task is to extract the data **exactly as it appears** under each column for every ministry and return the output in the following JSON format:

{{
  "ministers": [
    {{
      "name": "Exact full name of the minister (from heading)",
      "subjects_and_functions": [
        "Line 1 from Column I",
        "Line 2 from Column I",
        ...
      ],
      "departments": [
        "Line 1 from Column II",
        "Line 2 from Column II",
        ...
      ],
      "laws_and_ordinances": [
        "Line 1 from Column III",
        "Line 2 from Column III",
        ...
      ]
    }}
  ]
}}

### STRICT RULES:
1. DO NOT paraphrase, summarize, reword, rename or interpret anything. Copy each line **exactly** as shown.
2. DO NOT mix values between columns. Each item must go into the correct array according to where it is **visually listed** in the gazette.
3. DO NOT include the same item in more than one column. Each value belongs to **only one** column.
4. REMOVE only numbering (e.g., "1.", "•") if it is not part of the actual name.
5. INCLUDE continuation pages. If a ministry’s data spans multiple pages, combine all columns under the correct minister.
6. **if one value in one column mentioned another column, ignore that.**
8. Output valid, clean JSON only — no markdown, comments, or natural language.

Start extracting from the following document content:
{docs}
"""
