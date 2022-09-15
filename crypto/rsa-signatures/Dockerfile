FROM tiangolo/meinheld-gunicorn-flask:python3.8
COPY main.py secret_data.py quotes.txt requirements.txt /app/
RUN pip install -r /app/requirements.txt

