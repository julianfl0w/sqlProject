import subprocess

def run_docker_command():
    command = "docker run -it --rm -p 27017:27017 mongo"
    
    try:
        subprocess.run(command, check=True, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Command failed with error: {e}")

if __name__ == "__main__":
    run_docker_command()
