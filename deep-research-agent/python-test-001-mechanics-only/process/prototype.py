import os
import pandas as pd
import PyPDF2

# Paths
input_dir = "/app/input"
output_dir = "/app/python-test-001-mechanics-only/output"

book_file = os.path.join(input_dir, "Breaking-Into-Tech-Companies.pdf")

# Extract text from PDF
def extract_text_from_pdf(file_path):
    text = ""
    with open(file_path, "rb") as f:
        reader = PyPDF2.PdfReader(f)
        for page in reader.pages:
            text += page.extract_text() or ""
    return text

# Process text into hooks
def process_text(text):
    sentences = text.split(".")
    hooks = [s.strip() for s in sentences if len(s.strip()) >= 40]
    return hooks[:50]

# Prepare structured output
def prepare_output(hooks):
    data = []
    for hook in hooks:
        data.append({
            "Hook": hook,
            "Constraint": "TBD",
            "Identity Alignment": "TBD",
            "Reversal": "TBD",
            "CTA": "Join newsletter + Buy book",
            "Critical Quote": "TBD"
        })
    return pd.DataFrame(data)

# Execute pipeline
if __name__ == "__main__":
    print("Extracting text from book...")
    book_text = extract_text_from_pdf(book_file)
    print("Processing hooks...")
    hooks = process_text(book_text)
    print(f"Found {len(hooks)} hooks.")
    df = prepare_output(hooks)
    
    # Ensure output directory exists
    os.makedirs(output_dir, exist_ok=True)
    
    # Save CSV
    output_file = os.path.join(output_dir, "prototype_output_50.csv")
    df.to_csv(output_file, index=False)
    print(f"Output saved to {output_file}")

