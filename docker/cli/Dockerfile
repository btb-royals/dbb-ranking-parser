FROM alpine:3.3

RUN apk add --no-cache \
        libxml2 \
        libxslt \
        python3 \
        && \
    apk add --no-cache --virtual=.build-deps-lxml \
        build-base \
        libxml2-dev \
        libxslt-dev \
        python3-dev \
        && \
    python3 -m ensurepip && \
    pip3 install --upgrade pip && \
    pip3 install dbb-ranking-parser && \
    apk del .build-deps-lxml && \
    rm -rf /var/cache/apk/*

ENTRYPOINT ["dbb-ranking"]

CMD ["--help"]
