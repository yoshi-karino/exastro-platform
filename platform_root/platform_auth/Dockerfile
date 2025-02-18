#   Copyright 2022 NEC Corporation
#
#   Licensed under the Apache License, Version 2.0 (the "License");
#   you may not use this file except in compliance with the License.
#   You may obtain a copy of the License at
#
#       http://www.apache.org/licenses/LICENSE-2.0
#
#   Unless required by applicable law or agreed to in writing, software
#   distributed under the License is distributed on an "AS IS" BASIS,
#   WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
#   See the License for the specific language governing permissions and
#   limitations under the License.
ARG USERNAME=app_user
ARG GROUPNAME=app_user
ARG APP_PATH=/app

FROM    registry.access.redhat.com/ubi8/ubi-init as common_build

ARG USERNAME
ARG GROUPNAME
ARG APP_PATH

ENV PYTHONPATH              $APP_PATH/
ENV LISTEN_PORT             8000
ENV LISTEN_PORT_PF_MNG      8001
ENV PYTHONIOENCODING        utf-8
ENV APACHE_PID_DIR          /var/run_$USERNAME/httpd/pid
ENV APACHE_SOCKET_DIR       /var/run_$USERNAME/httpd/socket
ENV APACHE_USERNAME         $USERNAME
ENV APACHE_GROUPNAME        $GROUPNAME

RUN dnf install -y \
    langpacks-en \
    wget \
    unzip \
    httpd \
    gcc \
    httpd-devel \
    python39 \
    python39-devel \
    python39-mod_wsgi \
&&  pip3.9 install \
    requests \
    pyyaml \
    Flask \
    pytz \
    markdown \
    requests \
    PyJWT \
    python-dotenv \
    flask-log-request-id \
    pymysql \
&&  groupadd $GROUPNAME \
&&  useradd -m -s /bin/bash -g $GROUPNAME $USERNAME \
&&  setcap 'cap_net_bind_service=+ep' /usr/sbin/httpd \
&&  chown $USERNAME:$GROUPNAME /var/log/httpd \
&&  mkdir -p $APACHE_PID_DIR \
&&  chown $USERNAME:$GROUPNAME $APACHE_PID_DIR \
&&  mkdir -p $APACHE_SOCKET_DIR \
&&  chown $USERNAME:$GROUPNAME $APACHE_SOCKET_DIR

#
# Build for development
#   Specify options when creating this image: --target develop_build
#
FROM    common_build as develop_build

ARG USERNAME
ARG GROUPNAME
ARG APP_PATH

RUN dnf config-manager --add-repo=https://download.docker.com/linux/centos/docker-ce.repo \
&&  dnf install -y \
    sudo \
    git \
    vim \
    diffutils \
    bind-utils \
    iputils \
    docker-ce-cli \
    jq \
&&  pip3.9 install \
    debugpy \
    flake8 \
    autopep8 \
&&  usermod -G wheel $USERNAME \
&&  echo '%wheel ALL=(ALL) NOPASSWD: ALL' >> /etc/sudoers

USER $USERNAME

RUN mkdir ~/.config

WORKDIR $APP_PATH

COPY ./platform_root/platform_auth/config/httpd.conf/httpd.conf /etc/httpd/conf/httpd.conf
COPY ./platform_root/platform_auth/config/httpd.conf/reverse-proxy.conf /etc/httpd/conf.d/reverse-proxy.conf
COPY ./platform_root/platform_auth/config/httpd.conf/wsgi.conf /etc/httpd/conf.d/wsgi.conf

COPY ./platform_root/version $APP_PATH/
COPY ./platform_root/platform_auth/ $APP_PATH/
COPY ./platform_root/common_library/ $APP_PATH/common_library/
COPY ./platform_root/common_resources/ $APP_PATH/common_resources/

CMD ["httpd","-D","FOREGROUND"]

#
# Build for production
#
FROM    common_build

ARG USERNAME
ARG GROUPNAME
ARG APP_PATH

WORKDIR $APP_PATH

COPY ./platform_root/platform_auth/config/httpd.conf/httpd.conf /etc/httpd/conf/httpd.conf
COPY ./platform_root/platform_auth/config/httpd.conf/reverse-proxy.conf /etc/httpd/conf.d/reverse-proxy.conf
COPY ./platform_root/platform_auth/config/httpd.conf/wsgi.conf /etc/httpd/conf.d/wsgi.conf

COPY ./platform_root/version $APP_PATH/
COPY ./platform_root/platform_auth/ $APP_PATH/
COPY ./platform_root/common_library/ $APP_PATH/common_library/
COPY ./platform_root/common_resources/ $APP_PATH/common_resources/

USER $USERNAME

CMD ["httpd","-D","FOREGROUND"]
