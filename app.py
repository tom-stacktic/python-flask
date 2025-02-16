from flask import Flask, jsonify, request, g
import os
import time
import json





from src.cache_decorator import cache_response  # Import the caching decorator
from src.redis_provider import get_redis_client  # Import the Redis provider




# Initialize connection_info
connection_info = {}


# Import metrics directly for use in Flask routes or before/after request functions if needed
from src.metrics import flask_http_request_total, flask_http_request_duration_seconds, custom_registry
# Import DispatcherMiddleware from Werkzeug for serving Prometheus metrics on a separate endpoint
from werkzeug.middleware.dispatcher import DispatcherMiddleware
# Import make_wsgi_app from prometheus_client to create a WSGI application for Prometheus metrics
from prometheus_client import make_wsgi_app

# Import functions from prometheus_provider for updating Prometheus metrics
from src.prometheus_provider import (
    set_python_db_connection_status,
    update_python_memory_usage,
    update_python_cpu_usage,
    update_python_thread_count,
    update_python_logged_in_users,
    update_python_db_connection_pool_usage
)

app = Flask(__name__)

# Serve metrics through '/actuator/prometheus'
app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
    '/actuator/prometheus': make_wsgi_app(registry=custom_registry)
})




##################### Promothues #########################

from src.prometheus_provider import (
    set_python_db_connection_status,
    update_python_memory_usage,
    update_python_cpu_usage,
    update_python_thread_count,
    update_python_logged_in_users
)

app = Flask(__name__)

# Serve metrics through '/actuator/prometheus'
app.wsgi_app = DispatcherMiddleware(app.wsgi_app, {
    '/actuator/prometheus': make_wsgi_app(registry=custom_registry)
})














@app.before_request
def before_request():
    g.start_time = time.time()



@app.after_request
def after_request(response):
    # Calculate request duration and update metrics
    if hasattr(g, 'start_time'):
        request_duration = time.time() - g.start_time
        # Import Flask HTTP request metrics directly from metrics module
        from src.metrics import flask_http_request_total, flask_http_request_duration_seconds
        flask_http_request_total.labels(method=request.method, endpoint=request.path, status=response.status_code).inc()
        flask_http_request_duration_seconds.labels(method=request.method, endpoint=request.path, status=response.status_code).observe(request_duration)
    return response



# Define your routes
@app.route('/greeting')
def greeting():
    # Log all headers
    print(request.headers)
    return jsonify({"message": "Hello, welcome to the service!"}), 200

# ... (other route definitions) ...

# Run the application
if __name__ == "__main__":
    app.run(debug=True, host='0.0.0.0', port=int(os.getenv('SERVICE_PORT', 8080)))



