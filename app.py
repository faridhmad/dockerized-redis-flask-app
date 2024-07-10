import time
import logging
import redis
from flask import Flask, jsonify

# Initialize the Flask application
app = Flask(__name__)

# Set up logging
logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

# Initialize the Redis client
cache = redis.Redis(host='redis', port=6379)

def get_hit_count():
    retries = 5
    while True:
        try:
            count = cache.incr('hits')
            logger.info(f'Hit count retrieved successfully: {count}')
            return count
        except redis.exceptions.ConnectionError as exc:
            if retries == 0:
                logger.error('Failed to connect to Redis after several attempts.')
                raise exc
            retries -= 1
            logger.warning(f'Retrying Redis connection ({5 - retries}/5)...')
            time.sleep(0.5)

@app.route('/')
def hello():
    try:
        count = get_hit_count()
        return f'''
        <html>
            <head>
                <title>Hit Counter</title>
            </head>
            <body>
                <h1>Hello World Edited!</h1>
                <p>I have been seen <strong>{count}</strong> times.</p>
            </body>
        </html>
        '''
    except Exception as e:
        logger.error(f'Error retrieving hit count: {e}')
        return jsonify({'error': 'Failed to retrieve hit count'}), 500

@app.route('/health')
def health():
    try:
        cache.ping()
        return jsonify({'status': 'healthy'}), 200
    except redis.exceptions.ConnectionError as e:
        logger.error(f'Redis health check failed: {e}')
        return jsonify({'status': 'unhealthy', 'reason': str(e)}), 500

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
