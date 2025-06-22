# from transformers import pipeline

# summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

# def summarize_text(text, max_words=150):
#     if len(text.split()) > 600:
#         text = " ".join(text.split()[:600])
#     summary = summarizer(
#         text,
#         max_length=200,
#         min_length=50,
#         do_sample=False
#     )
#     return summary[0]['summary_text']

from transformers import pipeline

# ✅ Define summarizer globally
summarizer = pipeline("summarization", model="facebook/bart-large-cnn")

def summarize_text(text, max_words=150):
    # Step 1: Limit input text to 600 words
    if len(text.split()) > 600:
        text = " ".join(text.split()[:600])

    # Step 2: Generate summary
    summary = summarizer(
        text,
        max_length=200,
        min_length=50,
        do_sample=False
    )[0]['summary_text']

    # Step 3: Limit summary to max_words
    words = summary.split()
    if len(words) > max_words:
        summary = " ".join(words[:max_words]) + "..."

    return summary
