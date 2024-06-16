from pathlib import Path
import sys

# Get the absolute path of the current file
FILE = Path(__file__).resolve()
# Get the parent directory of the current file
ROOT = FILE.parent
# Add the root path to the sys.path list if it is not already there
if ROOT not in sys.path:
    sys.path.append(str(ROOT))
# Get the relative path of the root directory with respect to the current working directory
ROOT = ROOT.relative_to(Path.cwd())

# Sources
IMAGE = 'Image'
EXAMPLE = 'Example Image'

SOURCES_LIST = [IMAGE, EXAMPLE]

# Images config
IMAGES_DIR = ROOT / 'images'
DEFAULT_IMAGE = IMAGES_DIR / '122_tooth.jpg'
DEFAULT_DETECT_IMAGE = IMAGES_DIR / '122_tooth_detected.jpg'

IMAGES_DICT = {
    'Patient 1': IMAGES_DIR / '21_tooth.jpg',
    'Patient 2': IMAGES_DIR / '294_tooth.jpg',
    'Patient 3': IMAGES_DIR / '297_tooth.jpg',
    'Patient 4': IMAGES_DIR / '26_tooth.jpg',
    'Patient 5': IMAGES_DIR / '57_tooth.jpg',
    'Patient 6': IMAGES_DIR / '60_tooth.jpg',
    'Patient 7': IMAGES_DIR / '95_tooth.jpg',
}


# ML Model config
MODEL_DIR = ROOT / 'weights'
DETECTION_MODEL = MODEL_DIR / 'palmoil_97.pt'
# In case of your custome model comment out the line above and
# Place your custom model pt file name at the line below 
# DETECTION_MODEL = MODEL_DIR / 'my_detection_model.pt'

SEGMENTATION_MODEL = MODEL_DIR / 'yolov8n-seg.pt'
