#!/usr/bin/env python
from deepdive import *

@tsv_extractor
@returns(lambda
        mention_id       = "text",
        mention_text     = "text",
        docid            = "text",
        sentid           = "int",
        begin_index      = "int",
        end_index        = "int",
    :[])
def extract(
        docid          = "text",
        sentid         = "int",
        wordidx        = "int[]",
        poses          = "text[]",
    ):
    """
    Finds phrases that are continuous words tagged with Noun
    """
    index_num = len(poses_tags)
    # find all first indexes of series of tokens tagged as PERSON
    first_indexes = (i for i in xrange(index_num) if poses[i] == "NNP" or poses[i] == "NN"
    for begin_index in first_indexes:
        # find the end of the NNP/NN tag (consecutive words posses tagged as NNP or NN)
        end_index = begin_index + 1
        while end_index < index_num and (poses[end_index] == "NNP" or poses[i] == "NN"):
            end_index += 1
        end_index -= 1
        # generate a mention identifier
        mention_id = "%s_%d_%d_%d" % (doc_id, sentence_index, begin_index, end_index)
        mention_text = " ".join(map(lambda i: wordidx[i], xrange(begin_index, end_index + 1)))
        # Output a tuple for each noun phrase
        yield [
            mention_id,
            mention_text,
            docid,
            sentid,
            begin_index,
            end_index,
        ]
