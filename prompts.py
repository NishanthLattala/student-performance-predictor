# Prompts for the AI Study Buddy

DIAGNOSTIC_QUIZ_PROMPT = """
You are an expert tutor.
Create a short diagnostic quiz to test a student's knowledge on the topic: "{topic}".
Generate exactly 5 multiple choice questions.
Format the output strictly as a JSON list of objects, where each object has:
- "question": string
- "options": list of 4 strings
- "answer": string (the correct option text, must be one of the options)

Do not include any markdown formatting like ```json, just the raw JSON.
"""

EXPLANATION_PROMPT = """
You are an expert tutor used by students of all levels.
Explain the topic "{topic}" for a student at the "{level}" level.
Keep the explanation clear, concise, and engaging.
Use analogies if appropriate for the level.
"""

SUMMARY_PROMPT = """
Provide a cohesive and short summary of the topic "{topic}".
Focus on key takeaways.
"""

QUIZ_PROMPT = """
Generate a practice quiz for the topic "{topic}" at the "{level}" level.
Generate exactly 5 multiple choice questions.
Format the output strictly as a JSON list of objects, where each object has:
- "question": string
- "options": list of 4 strings
- "answer": string (the correct option text)
- "explanation": string (brief explanation of why the answer is correct)

Do not include any markdown formatting like ```json, just the raw JSON.
"""

FLASHCARD_PROMPT = """
Create 5 study flashcards for the topic "{topic}".
Format the output strictly as a JSON list of objects, where each object has:
- "front": string (concept or question)
- "back": string (definition or answer)

Do not include any markdown formatting like ```json, just the raw JSON.
"""
