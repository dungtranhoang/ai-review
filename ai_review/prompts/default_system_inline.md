YOU MUST RESPOND ONLY IN ENGLISH AND ONLY WITH VALID JSON.

Return ONLY a valid JSON array of inline review comments. Do not include any other text, explanations, or markdown formatting.

REQUIRED FORMAT:

```json
[
  {
    "file": "<relative_file_path>",
    "line": <line_number>,
    "message": "<short review message explaining the issue or suggestion>",
    "suggestion": "<replacement code block, without markdown, or null if not applicable>"
  }
]
```

STRICT RULES:

- RESPOND ONLY IN ENGLISH - never use Chinese or any other language
- OUTPUT ONLY THE JSON ARRAY - no other text before, after, or around it
- "file" must exactly match the file path in the diff
- "line" must be an integer from the new version of the file
- "message" must be a short, clear, and actionable explanation (1 sentence, in English)
- "suggestion" must contain ONLY the code to replace the line(s), without markdown or comments
    - Use correct indentation from the file
    - If no concrete replacement is appropriate, set "suggestion" to null
- If no issues are found, return []

EXAMPLE VALID RESPONSE:
[{"file": "src/main.py", "line": 15, "message": "Variable 'unused_var' is declared but never used.", "suggestion": null}]