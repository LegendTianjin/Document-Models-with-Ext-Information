####################################
# Author: Shashi Narayan
# Date: September 2016
# Project: Document Summarization
# H2020 Summa Project
####################################

"""
My flags
"""

from __future__ import absolute_import
from __future__ import division
from __future__ import print_function

import numpy as np
import tensorflow as tf

########### ============ Set Global FLAGS ============= #############


### GPU setting
tf.app.flags.DEFINE_string("gpu_id", "1", "0 based gpu id")

### Global setting
tf.app.flags.DEFINE_boolean("force_reading", False,
                            "Force re-definition of datasets attrs")


tf.app.flags.DEFINE_string("acc_type",
                           "top",
                           "Which accuracy type use:"
                           "'top' if top-ranked sent is in gold-answer-sents-set, then correct;"
                           "'any' if any 1-lbled sent is in gold-answer-sents-set, then correct")


tf.app.flags.DEFINE_boolean("filtered_setting", False,
                            "Decoding only over top K sentences")

tf.app.flags.DEFINE_integer("topK", 20, "Top K sentences wrt ISF score. Only used with filtered setting")

tf.app.flags.DEFINE_string("exp_mode", "train", "Training 'train' or Test 'test' Mode.")

tf.app.flags.DEFINE_boolean("use_fp16", False, "Use fp16 instead of fp32.")

tf.app.flags.DEFINE_string("data_mode",  "newsqa", "newsqa or squad")

tf.app.flags.DEFINE_integer("model_to_load", -1, "Select model to load for test case")

tf.app.flags.DEFINE_integer("load_prediction", -1, "Select which .npy prediction file to load")

tf.app.flags.DEFINE_boolean("use_subsampled_dataset", False, "Use subsampled training dataset.")

tf.app.flags.DEFINE_boolean("save_preds", False, "Save predictions and cos_sim.")

tf.app.flags.DEFINE_boolean("save_models", True, "Save model checkpoint.")

### Pretrained wordembeddings features

tf.app.flags.DEFINE_integer("wordembed_size", 200, "Size of wordembedding (<= 200).")

tf.app.flags.DEFINE_boolean("trainable_wordembed", False, "Is wordembedding trainable?")
# UNK and PAD are always trainable and non-trainable respectively.

### Sentence level features

tf.app.flags.DEFINE_integer("max_sent_length", 100, "Maximum sentence length (word per sent.)")

tf.app.flags.DEFINE_integer("sentembed_size", 350, "Size of sentence embedding.")

### Document level features

tf.app.flags.DEFINE_integer("max_doc_length", 110, "Maximum Document length (sent. per document).") # 174 train, 114 dev, 101 test

tf.app.flags.DEFINE_integer("max_title_length", 1, "Maximum number of top title to consider.") # 1

tf.app.flags.DEFINE_integer("max_image_length", 0, "Maximum number of top image captions to consider.") # 10

tf.app.flags.DEFINE_integer("max_firstsentences_length", 0, "Maximum first sentences to consider.") # 1

tf.app.flags.DEFINE_integer("max_randomsentences_length", 0, "Maximum number of random sentences to consider.") # 1

tf.app.flags.DEFINE_integer("target_label_size", 2, "Size of target label (1/0).")

### Convolution Layer features

tf.app.flags.DEFINE_integer("max_filter_length", 7, "Maximum filter length.")

tf.app.flags.DEFINE_integer("min_filter_length", 1, "Minimum filter length.")
# Filter of sizes min_filter_length to max_filter_length will be used, each producing
# one vector. 1-7 same as Kim and JP. max_filter_length <=
# max_sent_length

tf.app.flags.DEFINE_string("handle_filter_output", "concat", "sum or concat")
# If concat, make sure that sentembed_size is multiple of max_filter_length.


### MLP LAYER

tf.app.flags.DEFINE_integer("mlp_size", 100, "Size of FF layer")


### LSTM Features

tf.app.flags.DEFINE_integer("size", 600, "Size of each model layer.")

tf.app.flags.DEFINE_integer("num_layers", 1, "Number of layers in the model.")

tf.app.flags.DEFINE_string("lstm_cell", "lstm", "Type of LSTM Cell: lstm or gru.")

### Encoder Layer features

# Document Encoder: Unidirectional LSTM-RNNs
tf.app.flags.DEFINE_boolean("doc_encoder_reverse", True, "Encoding sentences inorder or revorder.")


### Training features

tf.app.flags.DEFINE_string("train_dir",
            "./train_dir_newsqa",
            "Training directory.")

tf.app.flags.DEFINE_float("learning_rate", 0.001, "Learning rate.")

tf.app.flags.DEFINE_float("dropout", 0.65, "Dropout intensity.")

tf.app.flags.DEFINE_boolean("use_dropout", False, "True only during training")

tf.app.flags.DEFINE_boolean("use_dropout_outatt", False, "Use dropout on SentExt output")

tf.app.flags.DEFINE_float("max_gradient_norm", -1, "Maximum gradient norm.")

tf.app.flags.DEFINE_boolean("weighted_loss", True, "Weighted loss to ignore padded parts.")

tf.app.flags.DEFINE_integer("batch_size", 20, "Batch size to use during training.")

tf.app.flags.DEFINE_integer("train_epoch_crossentropy", 20, "Number of training epochs.") # Reshuffle training data after every epoch

tf.app.flags.DEFINE_integer("training_checkpoint", 1, "How many training steps to do per checkpoint.")

###### Input file addresses: No change needed

# Pretrained wordembeddings data

tf.app.flags.DEFINE_string("pretrained_wordembedding_orgdata",
                           "../datasets/word_emb/1-billion-word-language-modeling-benchmark-r13output.word2vec.vec",
                           "Pretrained wordembedding file trained on the original data.")

# Data directory address

tf.app.flags.DEFINE_string("preprocessed_data_directory",
                           "../datasets/preprocessed_data",
                           "Pretrained news articles for various types of word embeddings.")


tf.app.flags.DEFINE_string("doc_sentence_directory",
                           "../datasets",
                           "Directory where document sentences are kept.")

############ Create FLAGS
FLAGS = tf.app.flags.FLAGS