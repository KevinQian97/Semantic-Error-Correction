TEXT=datasets/spider_wikisql
fairseq-preprocess --source-lang nl --target-lang crnl \
    --trainpref $TEXT/train.bpe.nl-crnl \
    --validpref $TEXT/valid.bpe.nl-crnl \
    --destdir data-bin/sw.nl.crnl_sql.bpe16k \
    --workers 10

fairseq-preprocess --source-lang nl --target-lang sql \
    --trainpref $TEXT/train.bpe.nl-sql \
    --validpref $TEXT/valid.bpe.nl-sql \
    --tgtdict data-bin/sw.nl.crnl_sql.bpe16k/dict.nl.txt \
    --destdir data-bin/sw.nl.crnl_sql.bpe16k  \
    --workers 10