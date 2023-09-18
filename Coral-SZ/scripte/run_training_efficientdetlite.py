import os

from tflite_model_maker import object_detector
from tflite_model_maker.config import ExportFormat

def trainModel(efficientDetVersion, train_data_path, validation_data_path, test_data_path, labels_file, epochs, batches, model_export_path):

    LABELS_FILE = labels_file
    EFFICIENTDET_VERSION = efficientDetVersion
    EPOCHS = epochs
    BATCH = batches
    MODEL_EXPORT_DIR = model_export_path

    os.makedirs(MODEL_EXPORT_DIR, exist_ok=True)

    VALIDATION_DATA_DIR = validation_data_path
    TRAIN_DATA_DIR = train_data_path
    TEST_DATA_DIR = test_data_path

    # Select the EfficientDet model. Other Input than 0-4 leads to 0.
    # https://www.tensorflow.org/lite/api_docs/python/tflite_model_maker/object_detector
    if EFFICIENTDET_VERSION == 0:
        EFFICIENTDET_NAME = "efficientdet-lite0"
        EFFICIENTDET_URI = "https://tfhub.dev/tensorflow/efficientdet/lite0/feature-vector/1"
    elif EFFICIENTDET_VERSION == 1:
        EFFICIENTDET_NAME = "efficientdet-lite1"
        EFFICIENTDET_URI = "https://tfhub.dev/tensorflow/efficientdet/lite1/feature-vector/1"
    elif EFFICIENTDET_VERSION == 2:
        EFFICIENTDET_NAME = "efficientdet-lite2"
        EFFICIENTDET_URI = "https://tfhub.dev/tensorflow/efficientdet/lite2/feature-vector/1"
    elif EFFICIENTDET_VERSION == 3:
        EFFICIENTDET_NAME = "efficientdet-lite3"
        EFFICIENTDET_URI = "https://tfhub.dev/tensorflow/efficientdet/lite3/feature-vector/1"
    elif EFFICIENTDET_VERSION == 4:
        EFFICIENTDET_NAME = "efficientdet-lite4"
        EFFICIENTDET_URI = 'https://tfhub.dev/tensorflow/efficientdet/lite4/feature-vector/1'
    else:
        EFFICIENTDET_NAME = "efficientdet-lite0"
        EFFICIENTDET_URI = 'https://tfhub.dev/tensorflow/efficientdet/lite0/feature-vector/1'

    TFLITE_FILENAME = f"trained_model-{EFFICIENTDET_NAME}"
    print(f"\tModel name:\t\ttrained_model-{EFFICIENTDET_NAME}")

    # Create Label map
    with open(LABELS_FILE, 'r') as f:
        label_map = [line.strip() for line in f.readlines()]

    train_data = object_detector.DataLoader.from_pascal_voc(
        os.path.join(TRAIN_DATA_DIR, 'images'),
        os.path.join(TRAIN_DATA_DIR, 'annotations'), label_map=label_map)
    validation_data = object_detector.DataLoader.from_pascal_voc(
        os.path.join(VALIDATION_DATA_DIR, 'images'),
        os.path.join(VALIDATION_DATA_DIR, 'annotations'), label_map=label_map)
    test_data = object_detector.DataLoader.from_pascal_voc(
        os.path.join(TEST_DATA_DIR, 'images'),
        os.path.join(TEST_DATA_DIR, 'annotations'), label_map=label_map)

    print("Training status:")

    print("1/7 Training in progress.. Please wait!")

    # Load EfficientDet model, configure training parameters and perform model training
    spec = object_detector.EfficientDetSpec(
        model_name=EFFICIENTDET_NAME,
        uri=EFFICIENTDET_URI,
        hparams={'max_instances_per_image': 8000})

    model = object_detector.create(train_data,
                                   model_spec=spec,
                                   batch_size=BATCH,
                                   train_whole_model=True,
                                   epochs=EPOCHS,
                                   validation_data=validation_data)

    print("2/7 Model created and trained")

    print("3/7 Tensorflow model evaluation started")
    evaluation_metrics = model.evaluate(test_data)
    print(f"Evaluation metrics TF Model:\n{evaluation_metrics}")

    print("4/7 Tensorflow model successfully evaluated")

    print("5/7 Convert to .tflite and export to file system")
    # Export tflite model and labels file into "DATASET_DIR/trained_model"
    model.export(export_dir=MODEL_EXPORT_DIR, tflite_filename=TFLITE_FILENAME + '.tflite',
                 label_filename=TFLITE_FILENAME + '_labels.txt',
                 export_format=[ExportFormat.TFLITE, ExportFormat.LABEL])
    print("6/7 Model exported")
    print(f"MODEL: {MODEL_EXPORT_DIR + '/' + TFLITE_FILENAME + '.tflite'}")
    print(f"LABELS: {MODEL_EXPORT_DIR + '/' + TFLITE_FILENAME + '_labels.txt'}")
    print("7/7 Model training and export completed")

    return model, train_data, validation_data, test_data, TFLITE_FILENAME

def testModel(efficientDetVersion, model, test_data, model_export_path):

    MODEL_EXPORT_DIR = model_export_path
    EFFICIENTDET_VERSION = efficientDetVersion

    # Select the EfficientDet model. Other Input than 0-4 leads to 0.
    # https://www.tensorflow.org/lite/api_docs/python/tflite_model_maker/object_detector
    if EFFICIENTDET_VERSION == 0:
        EFFICIENTDET_NAME = "efficientdet-lite0"
    elif EFFICIENTDET_VERSION == 1:
        EFFICIENTDET_NAME = "efficientdet-lite1"
    elif EFFICIENTDET_VERSION == 2:
        EFFICIENTDET_NAME = "efficientdet-lite2"
    elif EFFICIENTDET_VERSION == 3:
        EFFICIENTDET_NAME = "efficientdet-lite3"
    elif EFFICIENTDET_VERSION == 4:
        EFFICIENTDET_NAME = "efficientdet-lite4"
    else:
        EFFICIENTDET_NAME = "efficientdet-lite0"

    TFLITE_FILENAME = f"trained_model-{EFFICIENTDET_NAME}"

    print("Testing status:")

    print("1/1 Testing the tflite model with \"test data\"")
    evaluation_metrics = model.evaluate_tflite(os.path.join(MODEL_EXPORT_DIR, TFLITE_FILENAME + '.tflite'), test_data)
    print(f"Evaluation metrics TFLite model:\n{evaluation_metrics}")

    print("Testing completed")
    return 1





