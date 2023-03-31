FROM bentoml/model-server:0.11.0-py37
MAINTAINER ersilia

RUN conda install Python=3.8 
RUN pip install rdkit-pypi 
RUN pip install Mordred
RUN pip install pandas
RUN pip install matplotlib  
RUN pip install scikit-learn==0.23.2
RUN pip install "numpy<1.24"
RUN pip install networkx==2.3

WORKDIR /repo
COPY . /repo
