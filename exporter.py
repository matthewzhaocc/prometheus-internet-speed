import os
import typing
import time

import speedtest
from prometheus_client.core import GaugeMetricFamily, REGISTRY
from prometheus_client import start_http_server

st = speedtest.Speedtest()


class InternetPerformanceCollector(object):
    def __init__(self):
        pass

    def collect(self) -> typing.Generator[GaugeMetricFamily, None, None]:
        metrics = InternetPerformanceCollector.get_metrics()
        download = GaugeMetricFamily(
            'download_speed', 'The download speed of your connection (in gigabits)', InternetPerformanceCollector.to_gigabit(metrics['download']))

        yield download

        upload = GaugeMetricFamily(
            'upload_speed', 'The upload speed of your connection (in gigabits)', InternetPerformanceCollector.to_gigabit(
                metrics['upload'])
        )

        yield upload

        ping = GaugeMetricFamily(
            'ping', 'The latency of your connection', metrics['ping']
        )

        yield ping

    @staticmethod
    def to_gigabit(bit: float) -> float:
        return bit / 1_000_000_000

    @staticmethod
    def get_metrics() -> dict:
        st.get_servers()
        st.get_best_server()
        st.download()
        st.upload()
        return st.results.dict()


def get_port() -> int:
    if (port := os.environ.get('PORT') != None):
        return int(port)

    return 3000


if __name__ == '__main__':
    start_http_server(get_port())
    REGISTRY.register(InternetPerformanceCollector())
    while True:
        time.sleep(100)
