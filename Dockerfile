FROM python:3.12-bookworm

COPY app .

RUN pip install openai python-dotenv

CMD ["python","./gpt_interact.py"]