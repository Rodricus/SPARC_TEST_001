# SPARC_TEST_001

Standalone SPARC test project for validating document-based AI content generation.

## 🐳 Docker Setup

To build and run the container:

```bash
cd docker
docker-compose build
docker-compose run sparc
```

This launches a Python 3.12 container with all dependencies pre-installed.

The root directory is mounted to `/app`.

## 📂 Docker Folder Structure

```
docker/
├── Dockerfile
├── docker-compose.yml
└── requirements.txt
```

## 🧠 Notes

- Runs `prototype.py` from `deep-research-agent/python-test-001-mechanics-only/process/`.
- Output is saved to `deep-research-agent/python-test-001-mechanics-only/output/`.
