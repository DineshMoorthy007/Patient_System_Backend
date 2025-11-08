# Number of worker processes
workers = 4

# Number of threads per worker
threads = 2

# Socket to bind
bind = "0.0.0.0:5000"

# Timeout for requests
timeout = 120

# Maximum requests a worker will process before restarting
max_requests = 1000
max_requests_jitter = 50

# Logging
accesslog = '-'
errorlog = '-'
loglevel = 'info'

# Worker class
worker_class = 'gthread'

# Process name
proc_name = 'patient-system-backend'

# SSL (uncomment and configure for HTTPS)
# keyfile = 'path/to/keyfile'
# certfile = 'path/to/certfile'