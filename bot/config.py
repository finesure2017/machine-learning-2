DATA_PATH = 'D:\workspace\zimu'
DATA_FILE = 'subtitle.corpus'
CPT_PATH = 'checkpoints'

THRESHOLD = 2

PAD_ID = 0
UNK_ID = 1
START_ID = 2
EOS_ID = 3

BUCKETS = [(19, 19), (28, 28)]

NUM_LAYERS = 5

EMB_SIZE = 512  # embedding size 又是 神经元个数
BATCH_SIZE = 512

LR = 0.0005

MAX_GRAD_NORM = 5.0

NUM_SAMPLES = 500


SENTENCE_MAX_LEN = 30

TRAIN_PERCENTAGE = 90
TEST_PERCENTAGE = 10

DATA_SIZE = 10000

MIN_FREQUENT = 5
MAX_FREQUENT = 90

DEC_VOCAB = 2802 #w = tf.get_variable('proj_w', [config.EMB_SIZE, config.DEC_VOCAB])  ， 这个投影矩阵很大
ENC_VOCAB = 2802
