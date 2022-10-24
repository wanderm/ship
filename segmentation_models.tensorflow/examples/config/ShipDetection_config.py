# define the paths to the images directory
IMAGES_PATH = "datasets/OpenSARShip_Spk/images_8bit"
MASKS_PATH = "datasets/OpenSARShip_Spk/masks_8bit"

NUM_CLASSES = 2

NUM_VAL_IMAGES = 0.2
NUM_TEST_IMAGES = 0.6

# define the path to the output training, validation, and testing HDF5 files
TRAIN_IMG = "../../datasets/ShipDetection/train/img/"
VAL_IMG = "../../datasets/ShipDetection/valid/img/"
TEST_IMG = "../../datasets/ShipDetection/test/img/"

TRAIN_MSK = "../../datasets/ShipDetection/train/msk/"
VAL_MSK = "../../datasets/ShipDetection/valid/msk/"
TEST_MSK = "../../datasets/ShipDetection/test/msk/"

# path to the output model file
MODEL_PATH = "ShipDetection/output/alexnet_ShipDetection.model"

# define the path to the dataset mean
DATASET_MEAN = "ShipDetection/output/ShipDetection_mean.json"

# define the path to the output directory used for storing plots,
# classification reports, etc.
OUTPUT_PATH = "ShipDetection/output"