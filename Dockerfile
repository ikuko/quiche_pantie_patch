FROM ubuntu:18.04

RUN apt-get update && apt-get install -y --no-install-recommends git python3 python3-pip
RUN pip3 install setuptools wheel
RUN git clone https://github.com/TenteEEEE/quiche_pantie_patch.git
WORKDIR /quiche_pantie_patch
RUN pip3 install -r requirements.txt
CMD gunicorn --bind 0.0.0.0:5000 restapi:app
