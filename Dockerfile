FROM bentoml/model-server:0.11.0-py38
MAINTAINER ersilia

RUN conda install -c conda-forge scikit-learn==0.23.2
RUN pip install rdkit==2023.9.6
RUN pip install mordredcommunity==2.0.6
RUN pip install matplotlib==3.7.5
RUN pip install pandas==2.0.3
RUN pip install networkx==2.3
RUN pip install numpy==1.23


WORKDIR /repo
COPY . /repo
