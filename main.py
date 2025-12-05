import PyPDF2
from langOllama import generate_questions
from text_to_speech import text_to_speech_bark


def read_pdf(file_path):
    with open(file_path, 'rb') as file:
        reader = PyPDF2.PdfReader(file)
        text = ""
        for page in reader.pages:
            text += page.extract_text() + "\n"
    return text



def read_cv_jd(cv_path, jd_path):
    cv_content = read_pdf(cv_path)
    jd_content = read_pdf(jd_path)
    return cv_content, jd_content


cv_path = 'Saurav_Kapadiya_CV.pdf'
jd_path = 'Research_Engg_Raapid_JD.pdf'


cv_content, jd_content = read_cv_jd(cv_path, jd_path)
print(cv_content)
print()
print(jd_content)

questions = generate_questions(cv_content, jd_content)
print(questions)


for i, question in enumerate(questions.split('\n\n')):
    text_to_speech_bark(i+1, question)