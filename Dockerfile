FROM python:3.11-alpine

RUN apk upgrade --update
RUN apk add --no-cache \
    libffi-dev \
    openssl-dev \
    build-base \
    git \
    make \
    cmake \
    g++ \
    gcc \
    vim \
    curl \
    bash \
    gmp-dev

WORKDIR /app
COPY . .

RUN git clone https://github.com/herumi/mcl.git /lib/mcl && cd /lib/mcl && make -j4
ENV MCL_PATH=/lib/mcl

RUN git clone https://github.com/umberto10/mcl-python.git /lib/mcl-python
ENV PATH="${PATH}:/lib/mcl-python"

RUN sed -i "s|<mcl install path>|/lib/mcl/|g" /lib/mcl-python/mcl/hook.py

RUN pip install -r requirements.txt

CMD ["python", "main.py"]
