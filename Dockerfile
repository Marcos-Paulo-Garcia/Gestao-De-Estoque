FROM python:3.12

WORKDIR /src

COPY requirements.txt requirements.txt
RUN pip install --no-cache-dir -r requirements.txt

COPY . /src

EXPOSE 5000

ENV FLASK_RUN_HOST=0.0.0.0
CMD ["gunicorn", "--bind", "0.0.0.0:5000", "run:app"]
