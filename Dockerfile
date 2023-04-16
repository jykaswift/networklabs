FROM python:3
COPY . /app
WORKDIR /app
RUN pip install -r requirements.txt
ENV PYTHONPATH "${PYTHONPATH}:/app/"
ENTRYPOINT ["python3","src/start.py"]
