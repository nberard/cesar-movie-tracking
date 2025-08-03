FROM python:latest
COPY warmup.py /app/
COPY input-formatted.json /app/
COPY requirements.txt /app/
RUN mkdir /app/cache
RUN pip install -r /app/requirements.txt
RUN chmod +x /app/warmup.py