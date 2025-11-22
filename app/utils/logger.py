import logging
from pathlib import Path


def setup_logger():
   
    log_dir = Path(__file__).parent.parent.parent / "logs"
    log_dir.mkdir(exist_ok=True)
    
    logger = logging.getLogger("song_manager")
    logger.setLevel(logging.INFO)
    
    if logger.handlers:
        return logger
    
    formatter = logging.Formatter(
        '%(asctime)s - %(name)s - %(levelname)s - %(message)s',
        datefmt='%Y-%m-%d %H:%M:%S'
    )
    
    app_handler = logging.FileHandler(
        log_dir / "app.log",
        encoding='utf-8'
    )
    app_handler.setLevel(logging.INFO)
    app_handler.setFormatter(formatter)
    app_handler.addFilter(lambda record: record.levelno < logging.ERROR)
    
    error_handler = logging.FileHandler(
        log_dir / "errors.log",
        encoding='utf-8'
    )
    error_handler.setLevel(logging.ERROR)
    error_handler.setFormatter(formatter)
    
   
    logger.addHandler(app_handler)
    logger.addHandler(error_handler)
    
    return logger

logger = setup_logger()
