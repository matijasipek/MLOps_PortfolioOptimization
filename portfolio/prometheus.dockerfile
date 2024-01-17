# Use the official Prometheus image as a base
FROM prom/prometheus:v2.26.0

# Copy the configuration file into the container
COPY prometheus.yml /etc/prometheus/prometheus.yml

# Specify the entry point/command to run Prometheus
ENTRYPOINT [ "/bin/prometheus" ]
CMD [ "--config.file=/etc/prometheus/prometheus.yml", \
      "--storage.tsdb.path=/prometheus", \
      "--web.enable-lifecycle", \
      "--web.enable-admin-api" ]
