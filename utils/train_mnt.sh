python train.py -data data_asql2nl/asql2nl -save_model models/asql2nl/asql2nl-model -encoder_type transformer -decoder_type transformer \
    -layers 6 -rnn_size 512 -word_vec_size 512 \
    -transformer_ff 2048 -heads 8 -log_file models/asql2nl/log.json -train_steps 100000 \
    -valid_steps 10000 -report_every 500 -tensorboard -tensorboard_log_dir ./log/asql2nl 