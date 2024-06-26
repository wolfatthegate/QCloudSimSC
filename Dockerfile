FROM python:3.10-slim-buster
WORKDIR .
COPY requirements.txt .
RUN pip install --no-cache-dir -r requirements.txt
COPY . .
CMD [ "python", "SC2024.py" ]
