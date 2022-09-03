FROM python:3.10.5-alpine3.16
# LABEL maintainer="Operator2024 <work.pwnz+github@gmail.com>"
LABEL version="1.0.0"
ENV VER="0.1.1"
ENV TZ=Asia/Yekaterinburg
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone \ 
  && apk add --no-cache ipmitool jq && mkdir /workdir
COPY main.py  requirements.txt enrtypoint.sh /workdir/
WORKDIR "/workdir"
RUN chmod +x enrtypoint.sh
ENTRYPOINT [ "./enrtypoint.sh" ]
CMD [ "$1" ]
