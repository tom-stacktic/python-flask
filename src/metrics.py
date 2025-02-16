# metrics.py
from prometheus_client import CollectorRegistry, Gauge, Counter, Histogram

# Create a new registry
custom_registry = CollectorRegistry()

# Flask HTTP request metrics with custom registry
flask_http_request_total = Counter(
    'flask_http_request_total',
    'Total number of HTTP requests',
    ['method', 'endpoint', 'status'],
    registry=custom_registry
)

flask_http_request_duration_seconds = Histogram(
    'flask_http_request_duration_seconds',
    'HTTP request duration in seconds',
    ['method', 'endpoint', 'status'],
    buckets=(0.1, 0.25, 0.5, 1, 2.5, 5, 10),
    registry=custom_registry
)

# System metrics with custom registry
process_resident_memory_bytes = Gauge(
    'process_resident_memory_bytes',
    'Resident memory size in bytes.',
    registry=custom_registry
)

process_cpu_seconds_total = Counter(
    'process_cpu_seconds_total',
    'Total user and system CPU time spent in seconds.',
    registry=custom_registry
)

process_open_fds = Gauge(
    'process_open_fds',
    'Number of open file descriptors.',
    registry=custom_registry
)

# Re-defined or uncommented metrics for compatibility
python_db_connection_status = Gauge(
    'python_db_connection_status',
    'Database connection status',
    registry=custom_registry
)

python_memory_usage = Gauge(
    'python_app_memory_usage_bytes',
    'Memory usage of the application in bytes',
    registry=custom_registry
)

python_cpu_usage = Gauge(
    'python_app_cpu_usage_percent',
    'CPU usage of the application in percent',
    registry=custom_registry
)

python_thread_count = Gauge(
    'python_app_thread_count',
    'Number of threads in use by the application',
    registry=custom_registry
)

python_logged_in_users = Gauge(
    'python_app_logged_in_users',
    'Number of users currently logged in',
    registry=custom_registry
)

python_db_connection_pool_usage = Gauge(
    'python_app_db_connection_pool_usage',
    'Database connection pool usage',
    registry=custom_registry
)