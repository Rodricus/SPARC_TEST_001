# SPARC_TEST_001

### 🧪 Mechanics-Only Prototype

A structured content pipeline test to validate:
- File input/output flow
- Sentence extraction from PDFs
- CSV generation inside a Docker container

> This is a baseline test — no AI or LLM integration yet.

---

## 📁 Folder Structure

SPARC_TEST_001/
├── deep-research-agent/
│ ├── assets/
│ ├── context/
│ ├── input/
│ ├── src/
│ ├── tests/
│ ├── python-test-001-mechanics-only/
│ │ ├── process/
│ │ │ └── prototype.py
│ │ └── output/
│ │ └── prototype_output_50.csv
│ ├── README.md
│ └── SPARC_TEST_001_*.md (SPARC spec files)
├── docker/
│ ├── Dockerfile
│ ├── docker-compose.yml
│ └── requirements.txt
└── README.md

---

## 🐳 Docker Setup

### Build the container

```bash
cd docker
docker-compose build

Run the pipeline
bash
Copy
Edit
docker-compose run sparc
This will extract text from:

pgsql
Copy
Edit
deep-research-agent/input/Breaking-Into-Tech-Companies.pdf
And save output to:

bash
Copy
Edit
deep-research-agent/python-test-001-mechanics-only/output/prototype_output_50.csv
🎯 Purpose
This test exists to:

Validate Dockerized script execution

Confirm pathing and input file handling

Extract and format hooks for future use

It produces 50 structured rows with:

pgsql
Copy
Edit
Hook → Constraint → Identity Alignment → Reversal → CTA → Critical Quote
