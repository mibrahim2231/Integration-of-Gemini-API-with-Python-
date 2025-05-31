import google.generativeai as genai

# Set your API key
genai.configure(api_key="Your_API_key")

# Initialize the model
model = genai.GenerativeModel("gemini-1.5-flash")

# 1. Text Generation
def generate_text(prompt):
    response = model.generate_content(prompt)
    return response.text

# 2. Text Summarization
def text_summarization(text):
    response = model.generate_content(f"Summarize this: {text}")
    return response.text

# 3. Question Answering
def question_answering(context, question):
    response = model.generate_content(f"Question: {question}\nContext: {context}")
    return response.text

# 4. Sentiment Analysis
def sentiment_analysis(text):
    response = model.generate_content(f"Analyze the sentiment of this text: {text}")
    return response.text

# 5. Text Translation
def text_translation(text, target_language):
    response = model.generate_content(f"Translate this text to {target_language}: {text}")
    return response.text

# -----------------------------
# Calling these functions

# 1. Text Generation
prompt = "The quick brown fox"
print("Text Generation:\n", generate_text(prompt), "\n")

# 2. Summarization
text = "The quick brown fox jumps over the lazy dog"
print("Text Summarization:\n", text_summarization(text), "\n")

# 3. Question Answering
context = "The quick brown fox jumps over the lazy dog"
question = "What does the fox jump over?"
print("Question Answering:\n", question_answering(context, question), "\n")

# 4. Sentiment Analysis
text = "The quick brown fox jumps over the lazy dog"
print("Sentiment Analysis:\n", sentiment_analysis(text), "\n")

# 5. Text Translation
text = "The quick brown fox jumps over the lazy dog"
target_language = "es"  # Spanish
print("Text Translation:\n", text_translation(text, target_language), "\n")
