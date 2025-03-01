FROM registry.access.redhat.com/ubi9-minimal:9.5
# FROM registry.access.redhat.com/ubi8-minimal:8.10

# Setup arguments
ARG TEST_RUNNER_DIR=/test-runner
ARG KEY_DIR=/etc/pki/rpm-gpg
ARG REPO_DIR=/etc/yum.repos.d
ARG DRIVER_DIR=/usr/local/bin

# Setup environment variables
ENV SE_OFFLINE=true
ENV SE_AVOID_STATS=true
ENV BROWSER=chrome

# Add resources to image
COPY . ${TEST_RUNNER_DIR}
WORKDIR ${TEST_RUNNER_DIR}

# Setup RPM-GPG keys
RUN mv RPM-GPG-KEY-EPEL-9 ${KEY_DIR} && \
    mv RPM-GPG-KEY-CentOS-Official ${KEY_DIR} && \
    chmod 644 ${KEY_DIR}/RPM-GPG-KEY-EPEL-9 && \
    chmod 644 ${KEY_DIR}/RPM-GPG-KEY-CentOS-Official && \
    ls -al /etc/pki/rpm-gpg

# Setup repos
RUN rm -f ${REPO_DIR}/* && \
    mv nexus.repo ${REPO_DIR} && \
    chmod 644 ${REPO_DIR}/nexus.repo && \
    ls -al ${REPO_DIR}

# Install necessary packages
RUN microdnf install -y chromium-133.0.6943.126-1.el9.x86_64 firefox-128.7.0-1.el9.x86_64 python3.11 python3.11-pip tar gzip && \
    microdnf clean all

# Install chromedriver and geckodriver
RUN tar -zxf geckodriver-v0.36.0-linux64.tar.gz -C ${DRIVER_DIR} && \
    tar -zxf chromedriver-v133.0.6943.126-linux64.tar.gz -C ${DRIVER_DIR} && \
    rm -f geckodriver-v0.36.0-linux64.tar.gz && \
    rm -f chromedriver-v133.0.6943.126-linux64.tar.gz && \
    chown root:root ${DRIVER_DIR}/geckodriver && \
    chown root:root ${DRIVER_DIR}/chromedriver && \
    ls -al ${DRIVER_DIR}

# Create virtual environment and install pip packages
RUN python3.11 -m venv .venv && \
    source .venv/bin/activate && \
    pip install -r requirements.txt && \
    deactivate && \
    rm -f requirements.txt

# Show the test-runner directory
RUN ls -al
