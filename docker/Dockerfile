FROM ubuntu:20.04

#Install system libraries
RUN apt-get update 
RUN apt install -y curl
RUN apt install -y python3-pip 
RUN apt install -y unzip
RUN DEBIAN_FRONTEND=noninteractive apt-get install -yyq --no-install-recommends openjdk-11-jdk

RUN cd /opt && curl "https://www.bioinformatics.babraham.ac.uk/projects/fastqc/fastqc_v0.11.9.zip" > fastqc_v0.11.9.zip \
    && unzip fastqc_v0.11.9.zip -d /opt/bin/ \
    && chmod -R a+x /opt/bin/FastQC

#Copy a file from outside the docker (path relative to build directory) to inside the docker image
COPY ./ICA_SDK/ /opt/ICA_SDK/
WORKDIR /opt/ICA_SDK/ 
RUN python3 setup.py install 
RUN rm -fr /opt/ICA_SDK

#install AWS Python library
RUN pip install boto3 

WORKDIR /opt/project/

COPY ../download_and_process.py .

#Set an entrypoint.  Entrypoints are commands that are executed by default when someone tries to run the docker image.  
#Arguments passed to docker image will be passed to the entrypoint by default
ENTRYPOINT ["python3", "/opt/project/download_and_process.py"]