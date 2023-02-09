FROM python:3.9

ENV USER_NAME=vscode

ARG USER_ID
ARG GROUP_ID

RUN set -x \
    && apt-get update \
    && apt-get -y install \
        sudo \
        ca-certificates \
        curl \
        gnupg \
        lsb-release \
    && curl -fsSL https://download.docker.com/linux/debian/gpg | sudo gpg --dearmor -o /usr/share/keyrings/docker-archive-keyring.gpg \
    && echo \
        "deb [arch=$(dpkg --print-architecture) signed-by=/usr/share/keyrings/docker-archive-keyring.gpg] https://download.docker.com/linux/debian \
        $(lsb_release -cs) stable" | sudo tee /etc/apt/sources.list.d/docker.list > /dev/null \
    && curl -fsSL https://deb.nodesource.com/setup_18.x | /bin/bash - \
    && apt-get update \
    && apt-get -y install \
        docker-ce \
        docker-ce-cli \
        containerd.io \
        docker-compose-plugin \
        # nodejs \
        # kafkacat \
    && apt-get autoremove -y \
    && apt-get clean -y \
    && rm -rf /var/lib/apt/lists/*

RUN mkdir -p /workspace \
    && chown -R $USER_ID:$GROUP_ID /workspace \
    && addgroup --gid $GROUP_ID $USER_NAME \
    && adduser --disabled-password --gecos '' --uid $USER_ID --gid $GROUP_ID $USER_NAME \
    && usermod -aG docker $USER_NAME \
    && curl -L "https://github.com/docker/compose/releases/download/1.29.2/docker-compose-$(uname -s)-$(uname -m)" -o /usr/local/bin/docker-compose \
    && chmod +x /usr/local/bin/docker-compose

RUN set -x \
    && echo $USER_NAME ALL=\(root\) NOPASSWD:ALL > /etc/sudoers.d/$USER_NAME \
    && chmod 0440 /etc/sudoers.d/$USER_NAME

# COPY backend/src/requirements/ /tmp/

RUN python -m venv /opt/workenv \
    && /opt/workenv/bin/python -m pip install -U pip wheel setuptools honcho \
    # && /opt/workenv/bin/python -m pip install --no-cache-dir -r /tmp/test-requirements.txt \
    && chown -R $USER_ID:$GROUP_ID /opt/workenv

# RUN npm install -g @angular/cli @nestjs/cli

USER $USER_NAME

WORKDIR /workspace

ENV PATH="/opt/workenv/bin:${PATH}"

ENV PYTHONUNBUFFERED 1
# ENV PYTHONPATH /workspace/src
