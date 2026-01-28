# AI-Powered Adaptive Study Buddy

## Project Overview
This project is an AI-Powered Adaptive Study Buddy application built using **Python** and **Streamlit**. It leverages **Generative AI** (Google Gemini) and **AIML logic** to create personalized learning experiences.

The system assesses a learner's proficiency via a diagnostic quiz and adapts the study material (explanations, summaries, quizzes, flashcards) accordingly.

## Core Features
1.  **Adaptive Learning Path**:
    - **Diagnostic Quiz**: Assesses initial knowledge.
    - **AIML Classification**: Rules-based logic classifies users as Beginner, Intermediate, or Advanced.
2.  **Generative AI Integration**:
    - Dynamically generates explanations tailored to the user's level.
    - Creates custom quizzes and flashcards on *any* topic.
3.  **Interactive UI**:
    - Built with Streamlit for a clean, responsive web interface.

## Tech Stack
-   **Frontend**: Streamlit
-   **Backend Logic**: Python
-   **AI Model**: Google Gemini Pro (via `google-generativeai` SDK)
-   **Environment Management**: `python-dotenv`

## Installation & Setup

1.  **Clone/Download** the repository.
2.  **Install dependencies**:
    ```bash
    pip install -r requirements.txt
    ```
3.  **Run the Application**:
    ```bash
    streamlit run app.py
    ```

## Usage Guide
1.  **Enter API Key**: Upon launching, enter your Google Gemini API Key in the sidebar. (If you don't have one, the app runs in **Mock Mode** for demonstration).
2.  **Start Learning**: Enter a topic (e.g., "Machine Learning").
3.  **Take Diagnostic**: Complete the short quiz to get your level.
4.  **Dashboard**: Use the buttons to generate customized content.

## Innovation & AIML Logic
-   **Learner Classification**: The system uses a specific threshold logic (AIML concept) to categorize users based on quiz performance.
    -   < 50%: Beginner
    -   50-80%: Intermediate
    -   > 80%: Advanced
-   **Prompt Engineering**: Uses sophisticated prompt templates (`prompts.py`) to instruct the LLM to change its tone and complexity based on the classified level.
