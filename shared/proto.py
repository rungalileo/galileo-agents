import glob

import requests
from opentelemetry.proto.collector.trace.v1.trace_service_pb2 import (
    ExportTraceServiceRequest,
)

url = "https://api.galileo.ai/otel/v1/traces"
headers = {
    "Galileo-API-Key": "your-api-key-here",
    "Content-Type": "application/x-protobuf",
    "projectid": "your-project-id",
    "logstreamid": "your-logstream-id",
}

directory = "agents-langgraph/weather/otlp_trace"


def parse_trace(body_bytes):
    reqtrace = ExportTraceServiceRequest()
    reqtrace.ParseFromString(body_bytes)
    return reqtrace


def main():
    glob_files = glob.glob(f"{directory}/*.bin")
    glob_files.sort()
    for file in glob_files:
        print(f"Processing file: {file}")
        with open(file, "rb") as f:
            body_bytes = f.read()
            reqtrace = parse_trace(body_bytes)
        response = requests.post(url, headers=headers, data=reqtrace.SerializeToString())
        print(f"Status: {response.status_code}")
        print(f"Response: {response.text}")


if __name__ == "__main__":
    main()
