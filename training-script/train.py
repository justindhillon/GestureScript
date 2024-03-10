import tensorflow as tf
from object_detection.utils import config_util
from object_detection.protos import pipeline_pb2
from google.protobuf import text_format
import shutil
import subprocess

WORKSPACE_PATH = 'Tensorflow/workspace'
SCRIPTS_PATH = 'Tensorflow/scripts'
APIMODEL_PATH = 'Tensorflow/models'
ANNOTATION_PATH = WORKSPACE_PATH+'/annotations'
IMAGE_PATH = WORKSPACE_PATH+'/images'
MODEL_PATH = WORKSPACE_PATH+'/models'
PRETRAINED_MODEL_PATH = WORKSPACE_PATH+'/pre-trained-models'
CONFIG_PATH = MODEL_PATH+'/my_ssd_mobnet/pipeline.config'
CHECKPOINT_PATH = MODEL_PATH+'/my_ssd_mobnet/'

CONFIG_PATH = 'ssd_mobilenet_v2_fpnlite_320x320_coco17_tpu-8/pipeline.config'
config = config_util.get_configs_from_pipeline_file(CONFIG_PATH)

pipeline_config.model.ssd.num_classes = 7
pipeline_config.train_config.batch_size = 4
pipeline_config.train_config.fine_tune_checkpoint = 'ssd_mobilenet_v2_fpnlite_320x320_coco17_tpu-8/checkpoint/ckpt-0'
pipeline_config.train_config.fine_tune_checkpoint_type = "detection"
pipeline_config.train_input_reader.label_map_path= 'annotations/label_map.rbtxt'
pipeline_config.train_input_reader.tf_record_input_reader.input_path[:] = ['annotations/training.record']
pipeline_config.eval_input_reader[0].label_map_path = 'annotations/label_map.rbtxt'
pipeline_config.eval_input_reader[0].tf_record_input_reader.input_path[:] = ['annotations/testing.record']

config_text = text_format.MessageToString(pipeline_config)
with tf.io.gfile.GFile(CONFIG_PATH, "wb") as f:
    f.write(config_text)

shutil.rmtree(GSL-model, ignore_errors=True)
subprocess.run("python annotations/research/object_detection/model_main_tf2.py --model_dir=GSL-model --pipeline_config_path=GSL-model/pipeline.config --num_train_steps=5000", shell=True)
