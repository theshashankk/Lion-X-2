FROM sandy1709/catuserbot:latest

#clonning repo 
RUN git clone https://github.com/Mdnoor786/Lion.git /root/Lion
#working directory 
WORKDIR /root/Lion

# Install requirements
RUN pip3 install -U -r requirements.txt

ENV PATH="/home/Lion/bin:$PATH"

CMD ["python3","-m","Lion"]
