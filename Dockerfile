FROM ubuntu
COPY warmup.sh /app/
COPY input-formatted.json /app/
RUN apt -y install jq
RUN chmod +x /app/warmup.sh
ENTRYPOINT /bin/bash warmup.sh
