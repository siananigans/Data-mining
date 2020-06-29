# Docker build for noc_tools Service.

FROM alpine:3.8

LABEL \
    maintainer.name="Sian" \
    maintainer.email="Sian@telnyx.com"

ARG IMAGE_NAME="noc_tools"

# FIXME: Nomad build can't seem to pull these from the Makefile/Jenkinsfile
ARG VER_PYTHON="3.6"
ARG VER_PIP="18.1"
ARG VER_PIPENV="2018.11.26"
#^ do not call it "PIPENV_VERSION" or pipenv will crash

# Install main packages.

RUN set -o nounset -o errexit -o xtrace -o verbose \
    && apk add --no-cache \
        bash \
        curl \
        vim \
        ca-certificates \
        python3 \
    && python3 --version \
    && python3 -c "import os, sys;assert sys.version.startswith(os.environ.get('VER_PYTHON'))"

# Install s6-overlay.

COPY files/s6-overlay-amd64.tar.gz.sha512 /tmp
RUN set -o nounset -o errexit -o xtrace -o verbose \
    && cd /tmp \
    && curl -sSL -O https://github.com/just-containers/s6-overlay/releases/download/v1.19.1.1/s6-overlay-amd64.tar.gz \
    && sha512sum -c s6-overlay-amd64.tar.gz.sha512 \
    && tar zxf s6-overlay-amd64.tar.gz -C / \
    && rm s6-overlay-amd64.tar.gz

ENV S6_BEHAVIOUR_IF_STAGE2_FAILS=2 \
    SVC_DIR=/etc/services.d

# Install python dependencies.

WORKDIR /app

COPY files/pip.conf /etc/pip.conf
COPY Pipfile /app/Pipfile
COPY Pipfile.lock /app/Pipfile.lock
RUN set -o nounset -o errexit -o xtrace -o verbose \
    && apk add --no-cache --virtual .fetch-deps \
        python3-dev \
        gcc \
        g++ \
        musl-dev \
    && pip3 install \
        pip==${VER_PIP} \
        pipenv==${VER_PIPENV} \
        envtpl==0.6.0 \
    && pipenv install --dev --system --deploy \
    && apk del -q --purge .fetch-deps

# Install noc_tools service.

COPY . /app
ENV PYTHONPATH=/app

# s6 process config

RUN set -o nounset -o errexit -o xtrace -o verbose \
    \
    && addgroup -S noc_tools \
    && adduser -D -S -h /app -s /sbin/nologin -G noc_tools noc_tools \
    \
    && mkdir ${SVC_DIR}/noc_tools \
    && cp files/noc_tools-init.sh /etc/cont-init.d/ \
    && cp files/noc_tools-run.sh ${SVC_DIR}/noc_tools/run \
    && cp files/shutdown-finish.sh ${SVC_DIR}/noc_tools/finish

ENV TELEGRAF_STATSD=127.0.0.1:8125 \
    ENABLE_CONSULENV=true \
    ERROR_CODES_PATH=/etc/error-codes.json

ADD error-codes.json /etc/error-codes.json
RUN set -o nounset -o errexit -o xtrace -o verbose \
    && chown noc_tools:noc_tools /etc/error-codes.json

ENTRYPOINT ["/init"]

# Extra info that can be supplied upon build
# COMMIT - git show -s --format=%H
# DATE - git show -s --format=%cI

ARG BUILD_DATE=""
ARG BUILD_URL=""
ARG BUILD_NUMBER=""
ARG GIT_COMMIT=""
ARG GIT_COMMIT_DATE=""

# Inject as envvars so they're accessible inside
ENV IMAGE_NAME="$IMAGE_NAME" \
    VER_PYTHON="$VER_PYTHON" \
    VER_PIP="$VER_PIP" \
    VER_PIPENV="$VER_PIPENV" \
    BUILD_DATE="$BUILD_DATE" \
    BUILD_URL="$BUILD_URL" \
    BUILD_NUMBER="$BUILD_NUMBER" \
    GIT_COMMIT="$GIT_COMMIT" \
    GIT_COMMIT_DATE="$GIT_COMMIT_DATE"

# Metadata
LABEL \
    org.label-schema.build-date="$BUILD_DATE" \
    com.telnyx.build-url="$BUILD_URL" \
    com.telnyx.build-git-commit="$GIT_COMMIT" \
    com.telnyx.build-git-commit-date="$GIT_COMMIT_DATE" \
    org.label-schema.name="$IMAGE_NAME" \
    org.label-schema.vcs-url="https://github.com/team-telnyx/noc_tools" \
    org.label-schema.vendor="Telnyx" \
    com.telnyx.docker.cmd="/init" \
    com.telnyx.name.upsource="$IMAGE_NAME" \
    com.telnyx.name.bugsnag="$IMAGE_NAME"
