FROM debian:stretch-slim
MAINTAINER XFanis <mail@xfanis.ru>

# Generate locale C.UTF-8 for postgres and general locale data
ENV LANG C.UTF-8

# Install git, curl, pip and other python assets for odoo
RUN apt-get update && apt-get -y upgrade \
    && apt-get install -y git curl python-pip python-dev zlib1g-dev libevent-dev gcc libjpeg-dev libxml2-dev libssl-dev libsasl2-dev node-less libldap2-dev libxslt-dev \
    && apt-get clean && rm -fr /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Install wkhtmltopdf
RUN curl -o wkhtmltox.deb -sSL https://github.com/wkhtmltopdf/wkhtmltopdf/releases/download/0.12.5/wkhtmltox_0.12.5-1.stretch_amd64.deb \
    && echo '7e35a63f9db14f93ec7feeb0fce76b30c08f2057 wkhtmltox.deb' | sha1sum -c - \
    && apt-get update && apt-get install -y --no-install-recommends ./wkhtmltox.deb \
    && apt-get clean && rm -fr /var/lib/apt/lists/* /tmp/* /var/tmp/* wkhtmltox.deb

# Install postgresql-client
RUN echo 'deb http://apt.postgresql.org/pub/repos/apt/ stretch-pgdg main' > /etc/apt/sources.list.d/pgdg.list
RUN curl -o - https://www.postgresql.org/media/keys/ACCC4CF8.asc | apt-key add -
RUN apt-get update && apt-get install -y --no-install-recommends postgresql-client \
    && apt-get clean && rm -fr /var/lib/apt/lists/* /tmp/* /var/tmp/*

# Install odoo 10.0
ENV ODOO_VERSION 10.0
RUN mkdir /opt/odoo10
RUN git clone https://www.github.com/odoo/odoo --depth 1 --branch 10.0 --single-branch /opt/odoo10
RUN pip install -r /opt/odoo10/requirements.txt && rm -rf ~/.cache/pip

# Mount /var/lib/odoo to allow restoring filestore and /mnt/extra-addons for users addons
RUN mkdir -p /mnt/extra-addons
VOLUME ["/var/lib/odoo", "/mnt/extra-addons"]

# Expose Odoo services
EXPOSE 8069 8071

# Install extra requirements.txt
COPY ./requirements.txt /mnt/requirements.txt
RUN pip install -r /mnt/requirements.txt && rm -rf ~/.cache/pip