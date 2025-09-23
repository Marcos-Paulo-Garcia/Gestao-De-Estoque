FROM python:3.12-slim

WORKDIR /src

RUN apt-get update && apt-get install -y \
    default-libmysqlclient-dev \
    build-essential \
    pkg-config \
    && rm -rf /var/lib/apt/lists/*

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . /src

EXPOSE 5000

ENV FLASK_RUN_HOST=0.0.0.0
CMD ["flask", "run", "--host=0.0.0.0", "--port=5000"]
