FROM 1science/alpine

ENV PATH /usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin

# get our basic-needs sorted
RUN echo http://dl-cdn.alpinelinux.org/alpine/edge/testing >> /etc/apk/repositories
RUN apk update
RUN apk add --update python3 python3-dev vim bash    \
                curl build-base libffi-dev openssl-dev    \
    && curl "https://bootstrap.pypa.io/get-pip.py" | python3 \
    && pip install --upgrade pip setuptools     \
    && ln -s /usr/bin/python3 /usr/bin/python   \
    && mkdir -p /opt /app

ADD . /app
WORKDIR /app
RUN pip install -e .
RUN pip install -r requirements.txt --no-compile
CMD /app/bin/kube-limbo

# vim: set expandtab tabstop=4 shiftwidth=4 autoindent smartindent:
