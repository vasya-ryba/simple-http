FROM python:3

WORKDIR /usr/src/app

COPY requirements.txt ./
RUN pip install --no-cache-dir -r requirements.txt

COPY static/ static/

COPY main.py .

EXPOSE 5000
ENTRYPOINT [ "python" ]
CMD [ "main.py" ]