FROM cdrx/pyinstaller-windows:python3

WORKDIR /src

COPY . /src

RUN pip install -r requirements.txt
