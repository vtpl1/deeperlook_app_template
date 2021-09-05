FROM vtpl/suva-cuda:beta
COPY requirements.txt /tmp/pip-tmp/
RUN pip3 install --disable-pip-version-check -r /tmp/pip-tmp/requirements.txt \
   && rm -rf /tmp/pip-tmp