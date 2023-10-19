import redis

class RedisManager:
    def __init__(self, host='localhost', port=6379, db=0):
        self.redis_client = redis.StrictRedis(host=host, port=port, db=db)

    def write_data(self, key, value):
        self.redis_client.set(key, value)

    def read_data(self, key):
        return self.redis_client.get(key).decode('utf-8')

if __name__ == "__main__":
    r_manager = RedisManager()

    # Write example data
    r_manager.write_data('example_key', 'example_value')
    print("Data written to Redis.")

    # Read and print example data
    value = r_manager.read_data('example_key')
    print(f"Retrieved value for 'example_key': {value}")
