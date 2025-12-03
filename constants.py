HUMAN_PROMPT = f"""
    Analyze the following CV and Job Description:
    CV: {cv_content}

    Job Description: {jd_content}

    Generate five relevant technical interview questions. Follow these guidelines:
    1. Focus on the candidate's specific experience and skills that match the job requirements.
    2. Make questions detailed and tailored to the candidate's technical expertise.
    3. Avoid general questions about data structures and algorithms.
    4. Do not include any numbering or prefixes in the questions.
    5. Each question should be on a new line.
    6. Do not include any explanations or additional text, just the questions.
    """

SYSTEM_PROMPT = "You are an AI interviewer. You are given a CV and a Job Description and you need to generate five relevant technical interview questions."