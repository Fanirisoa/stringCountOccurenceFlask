FROM python:3.7

ENV MY_STRINGS="blue green red black"

COPY main.py /
COPY sparseArray.py /

RUN chmod +x main.py \
        && chmod +x sparseArray.py

ENTRYPOINT ["python","./main.py","-q"]