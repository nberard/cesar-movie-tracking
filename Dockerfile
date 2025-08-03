FROM python:latest
COPY warmup.py /app/
COPY input-formatted.json /app/
RUN pip install -r requirements.txt
RUN chmod +x /app/warmup.py