import subprocess
import os
import logging

logging.basicConfig(filename='automated_scraper.log', level=logging.INFO)

def run_script(script_name):
    script_path = os.path.join('scripts', script_name)
    try:
        result = subprocess.run(['python', script_path], check=True, text=True, capture_output=True)
        logging.info(f"Output of {script_name}:\n{result.stdout}")
    except subprocess.CalledProcessError as e:
        logging.error(f"Error running {script_name}:\n{e.stderr}")

if __name__ == "__main__":
    scripts = ['scrape_groups.py', 'scrape_softwares.py', 'scrape_techniques.py']
    for script in scripts:
        run_script(script)