import os
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Path configurations
BASE_DIR = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
MODELS_DIR = os.path.join(BASE_DIR, "models")
DATA_DIR = os.path.join(BASE_DIR, "data")

# Camera and video settings
VIDEO_SOURCE = os.getenv("VIDEO_SOURCE", 0)  # Default to webcam (0)
# Fixed resolution for consistent aspect ratio
FRAME_WIDTH = 640
FRAME_HEIGHT = 480
DISPLAY_WIDTH = 640  # Fixed display width
DISPLAY_HEIGHT = 480  # Fixed display height
FPS = int(os.getenv("FPS", 20))

# Detection settings
DETECTION_THRESHOLD = float(os.getenv("DETECTION_THRESHOLD", 0.5))

# Classes of interest for detection
CLASSES_OF_INTEREST = [
    'person', 'bicycle', 'car', 'motorcycle', 'bus', 'truck',
    'backpack', 'suitcase', 'cell phone', 'handbag', 'knife', 'drone'
]

# Border crossing detection settings
BORDER_LINES = [
    {
        'id': 'main_border',
        'points': [(0, FRAME_HEIGHT // 2), (FRAME_WIDTH, FRAME_HEIGHT // 2)],
        'direction': 'both'  # 'north_to_south', 'south_to_north', or 'both'
    },
    # Example of a diagonal border
    {
        'id': 'northeast_border',
        'points': [(0, FRAME_HEIGHT), (FRAME_WIDTH, 0)],
        'direction': 'north_to_south'
    }
]

# Fence tampering detection settings
FENCE_REGIONS = []  # List of polygons defining fence areas
TAMPERING_SENSITIVITY = float(os.getenv("TAMPERING_SENSITIVITY", 0.3))

# Behavior analysis settings
SUSPICIOUS_BEHAVIORS = {
    "loitering": {
        "time_threshold": int(os.getenv("LOITERING_TIME", 30)),  # in seconds
        "area_threshold": float(os.getenv("LOITERING_AREA", 0.2))  # in ratio of frame
    },
    "crawling": {
        "height_ratio_threshold": float(os.getenv("CRAWLING_RATIO", 0.5))  # height/width ratio
    }
}

# Alert settings
ALERT_COOLDOWN = int(os.getenv("ALERT_COOLDOWN", 60))  # seconds between identical alerts
SMS_ALERTS_ENABLED = os.getenv("SMS_ALERTS_ENABLED", "false").lower() == "true"
DASHBOARD_ALERTS_ENABLED = os.getenv("DASHBOARD_ALERTS_ENABLED", "true").lower() == "true"

# Twilio settings for SMS alerts
TWILIO_ACCOUNT_SID = os.getenv("TWILIO_ACCOUNT_SID", "")
TWILIO_AUTH_TOKEN = os.getenv("TWILIO_AUTH_TOKEN", "")
TWILIO_PHONE_NUMBER = os.getenv("TWILIO_PHONE_NUMBER", "")
ALERT_RECIPIENT_NUMBERS = os.getenv("ALERT_RECIPIENT_NUMBERS", "").split(",")

# MQTT settings for alert distribution
MQTT_BROKER = os.getenv("MQTT_BROKER", "localhost")
MQTT_PORT = int(os.getenv("MQTT_PORT", 1883))
MQTT_TOPIC = os.getenv("MQTT_TOPIC", "border/alerts")

# Geographical settings
GPS_ENABLED = os.getenv("GPS_ENABLED", "false").lower() == "true"
DEFAULT_LAT = float(os.getenv("DEFAULT_LAT", 23.81606))
DEFAULT_LON = float(os.getenv("DEFAULT_LON", 86.44212))

# Map settings
MAP_UPDATE_INTERVAL = int(os.getenv("MAP_UPDATE_INTERVAL", 5))  # in seconds
MAP_TILE_PROVIDER = os.getenv("MAP_TILE_PROVIDER", "OpenStreetMap")
MAP_ZOOM_LEVEL = int(os.getenv("MAP_ZOOM_LEVEL", 15))
MAP_OUTPUT_FILE = os.path.join(BASE_DIR, "output", "detection_map.html")
GPSD_HOST = os.getenv("GPSD_HOST", "localhost")
GPSD_PORT = int(os.getenv("GPSD_PORT", 2947))
HEATMAP_ENABLED = os.getenv("HEATMAP_ENABLED", "true").lower() == "true"

# Map border settings
MAP_BORDERS = []  # List will be populated with border definitions added from UI
MAP_BORDERS_ENABLED = os.getenv("MAP_BORDERS_ENABLED", "true").lower() == "true"
DEFAULT_BORDER_COLOR = os.getenv("DEFAULT_BORDER_COLOR", "red")
DEFAULT_BORDER_WEIGHT = int(os.getenv("DEFAULT_BORDER_WEIGHT", 3))

# Performance settings for edge deployment
USE_GPU = os.getenv("USE_GPU", "true").lower() == "true"
MODEL_PRECISION = os.getenv("MODEL_PRECISION", "fp16")  # fp32, fp16, or int8
MAX_BATCH_SIZE = int(os.getenv("MAX_BATCH_SIZE", 1))

# Logging settings
LOG_LEVEL = os.getenv("LOG_LEVEL", "INFO")
LOG_FILE = os.path.join(BASE_DIR, "logs", "surveillance.log")