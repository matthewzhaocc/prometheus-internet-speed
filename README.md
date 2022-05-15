# Welcome to Prometheus Speedtest Exporter

This Prometheus exporter is used to get the internet download, upload, and ping speeds to be graphed using 3rd party tools like Grafana.

This exporter utilizes speedtest-cli to be able to ping the servers within the [speedtest.net](https://speedtest.net) network made by Ookla.

## Setup

To get this locally running, run:

```bash
docker-compose up -d
```

This will bring up everything with reasonable default configs. 

You can now log into `http://localhost:3000` to access the grafana panel. You need to manually add the prometheus data source, which is available at `http://prometheus:9090`

## Data Cap

This can be relatively intense for your network if it is on a capped band. Simply edit the `prometheus.yml` and `exporter.py` files to edit the frequency in which data is being fetched.

Within `prometheus.yml`, edit:

```
scrape_interval: 150s
```

To be what you feel is reasonable to be downloading files from the remote systems.

Within `exporter.py`, at the end, edit:

```
time.sleep(100)
```

to be a number that is about consistent with scrape interval.