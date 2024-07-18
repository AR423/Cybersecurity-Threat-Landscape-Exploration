import subprocess
import logging

logging.basicConfig(filename='automated_scraper.log', level=logging.INFO)

def run_script(script_name):
    try:
        result = subprocess.run(['python', script_name], check=True, text=True, capture_output=True)
        logging.info(f"Output of {script_name}:\n{result.stdout}")
    except subprocess.CalledProcessError as e:
        logging.error(f"Error running {script_name}:\n{e.stderr}")

if __name__ == "__main__":
    scripts = ['web_scraper.py']
    for script in scripts:
        run_script(script)