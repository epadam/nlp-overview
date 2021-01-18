FROM python:3.7
WORKDIR /app
COPY requirements.txt ./requirements.txt
RUN pip3 install -r requirements.txt
RUN python -m spacy download en
COPY . .
CMD streamlit run app.py --server.port $PORT