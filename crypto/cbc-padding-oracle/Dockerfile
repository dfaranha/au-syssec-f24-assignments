FROM tiangolo/meinheld-gunicorn-flask:python3.8
COPY main.py quotes.txt requirements.txt /app/
COPY secret_data.py /app/secret_data.py
RUN pip install -r /app/requirements.txt
