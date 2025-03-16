from pathlib import Path
import requests


def download(url: str, local_filename: str = None, target_dir: str = None) -> str:
    """download data from url and save to the data folder"""
    local_filename = local_filename or Path(url).name
    target_dir = target_dir or Path(__file__).parent
    full_path = Path(target_dir) / local_filename
    full_path.parent.mkdir(exist_ok=True)

    response = requests.get(url, stream=True)
    response.raise_for_status()

    with open(full_path, "wb") as file:
        for chunk in response.iter_content(chunk_size=8192):
            file.write(chunk)

    return full_path


download(
    "https://github.com/PredictiveScienceLab/data-analytics-se/raw/master/lecturebook/data/stress_strain.txt"
)
