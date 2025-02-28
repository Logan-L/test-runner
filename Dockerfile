FROM registry.access.redhat.com/ubi9-minimal:9.5

# Setup environment variables
ENV SE_OFFLINE=true
ENV SE_AVOID_STATS=true
# ENV BROWSER=chrome

# Setup arguments
ARG TEST_RUNNER_DIR=/test-runner
ARG REPO_DIR=/etc/pki/rpm-gpg
ARG DRIVER_DIR=/usr/local/bin

# Add resources to image
COPY . ${TEST_RUNNER_DIR}
WORKDIR ${TEST_RUNNER_DIR}

# Setup RPM-GPG keys
RUN mv RPM-GPG-KEY-EPEL-9 ${REPO_DIR} && \
    mv RPM-GPG-KEY-CentOS-Official ${REPO_DIR} && \
    chmod 644 ${REPO_DIR}/RPM-GPG-KEY-EPEL-9 && \
    chmod 644 ${REPO_DIR}/RPM-GPG-KEY-CentOS-Official && \
    ls -al /etc/pki/rpm-gpg

# Setup repos
RUN rm -f /etc/yum.repos.d/* && \
    mv test.repo /etc/yum.repos.d && \
    chmod 644 /etc/yum.repos.d/test.repo && \
    ls -al /etc/yum.repos.d

# Install necessary packages
RUN microdnf install -y chromium firefox python3.11 python3.11-pip tar gzip && \
    microdnf clean all

# Install chromedriver and geckodriver
RUN tar -zxf chromedriver.tar.gz -C ${DRIVER_DIR} && \
    tar -zxf geckodriver-v0.36.0-linux64.tar.gz -C ${DRIVER_DIR} && \
    rm -f chromedriver.tar.gz && \
    rm -f geckodriver-v0.36.0-linux64.tar.gz && \
    chown root:root ${DRIVER_DIR}/chromedriver && \
    chown root:root ${DRIVER_DIR}/geckodriver && \
    ls -al ${DRIVER_DIR}

# Create virtual environment and install pip packages
RUN python3.11 -m venv .venv && \
    source .venv/bin/activate && \
    pip install -r requirements.txt && \
    deactivate && \
    rm -f requirements.txt

# Show the test-runner directory
RUN ls -al