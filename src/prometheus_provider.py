# src/prometheus_provider.py
from .metrics import (
    python_db_connection_status,
    python_memory_usage,
    python_cpu_usage,
    python_thread_count,
    python_logged_in_users
)

def set_python_db_connection_status(is_connected):
    python_db_connection_status.set(1 if is_connected else 0)

def update_python_memory_usage(memory_usage):
    python_memory_usage.set(memory_usage)

def update_python_cpu_usage(cpu_usage):
    python_cpu_usage.set(cpu_usage)

def update_python_thread_count(thread_count):
    python_thread_count.set(thread_count)

def update_python_logged_in_users(logged_in_users):
    python_logged_in_users.set(logged_in_users)

def update_python_db_connection_pool_usage(usage):
    python_db_connection_pool_usage.set(usage)
