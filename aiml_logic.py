import os
import json
import google.generativeai as genai
from dotenv import load_dotenv
import prompts

# Implementation of AIML Logic using Generative AI and Rule-Based Classification

class StudyBuddyAI:
    def __init__(self):
        load_dotenv()
        self.api_key = os.getenv("GEMINI_API_KEY")
        self.model = None
        if self.api_key:
            genai.configure(api_key=self.api_key)
            self.model = genai.GenerativeModel('gemini-pro')
        
    def is_configured(self):
        return self.model is not None

    def _get_response(self, prompt, is_json=False):
        """Helper to call Gemini API safely."""
        if not self.model:
            return None
        
        try:
            response = self.model.generate_content(prompt)
            text = response.text
            if is_json:
                # Basic cleanup if the model wrapping in markdown
                text = text.replace("```json", "").replace("```", "").strip()
            return text
        except Exception as e:
            print(f"Error calling Gemini: {e}")
            return None

    def generate_diagnostic_quiz(self, topic):
        """Generates a diagnostic quiz to assess learner level."""
        prompt = prompts.DIAGNOSTIC_QUIZ_PROMPT.format(topic=topic)
        response_text = self._get_response(prompt, is_json=True)
        
        if response_text:
            try:
                return json.loads(response_text)
            except json.JSONDecodeError:
                return [] # Fail gracefully
        
        # Fallback Mock Data if API fails or not configured
        return [
            {
                "question": "Diagnostic Q1 (Mock): What is the first step in learning " + topic + "?",
                "options": ["Read basics", "Expert Coding", "Skip to end", "Sleep"],
                "answer": "Read basics"
            },
            {
                "question": "Diagnostic Q2 (Mock): Which concept is core to " + topic + "?",
                "options": ["Concept A", "Concept B", "Concept C", "Concept D"],
                "answer": "Concept A"
            },
            {
                "question": "Diagnostic Q3 (Mock): Advanced application of " + topic + "?",
                "options": ["Simple usage", "Complex System", "Not applicable", "None"],
                "answer": "Complex System"
            }
        ]

    def classify_learner(self, score, total_questions):
        """
        AIML Logic: Rule-based Classifier.
        Classifies learner based on diagnostic quiz accuracy.
        """
        if total_questions == 0:
            return "Beginner"
            
        percentage = (score / total_questions) * 100
        
        if percentage < 50:
            return "Beginner"
        elif percentage < 80:
            return "Intermediate"
        else:
            return "Advanced"

    def get_explanation(self, topic, level):
        prompt = prompts.EXPLANATION_PROMPT.format(topic=topic, level=level)
        response = self._get_response(prompt)
        return response if response else f"Mock Explanation for {topic} ({level} Level)."

    def get_summary(self, topic):
        prompt = prompts.SUMMARY_PROMPT.format(topic=topic)
        response = self._get_response(prompt)
        return response if response else f"Mock Summary for {topic}."

    def generate_practice_quiz(self, topic, level):
        prompt = prompts.QUIZ_PROMPT.format(topic=topic, level=level)
        response_text = self._get_response(prompt, is_json=True)
        if response_text:
            try:
                return json.loads(response_text)
            except:
                pass
        return []

    def generate_flashcards(self, topic):
        prompt = prompts.FLASHCARD_PROMPT.format(topic=topic)
        response_text = self._get_response(prompt, is_json=True)
        if response_text:
            try:
                return json.loads(response_text)
            except:
                pass
        return [{"front": "Mock Term", "back": "Mock Definition"}]
