import subprocess

def run_redis_container():
    command = "docker run --name my-redis -d -p 6379:6379 redis:latest"
    
    try:
        subprocess.run(command, check=True, shell=True)
        print("Redis container started successfully!")
    except subprocess.CalledProcessError as e:
        print(f"Command failed with error: {e}")

if __name__ == "__main__":
    run_redis_container()
