import yaml

def parse(file: str):
    with open(file) as f:
        return yaml.safe_load(f)
