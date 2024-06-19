import os

def get_config():
    env = os.getenv('ENV', 'dev')
    if env == 'dev':
        from config.dev_config import DevConfig as Config
    elif env == 'uat':
        from config.uat_config import UatConfig as Config
    else:
        raise ValueError(f"Unknown environment: {env}")
    return Config
