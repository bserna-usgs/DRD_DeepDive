#!/usr/bin/env python
from deepdive import *    # required for @tsv_extractor and @returns

sentences1 = [1,2,3,4,5]

@tsv_extractor
@returns(lambda #Declares the types of output columns as declared in DDlog
	docid = "text",
	topic = "text",
	:[])

def dam_pres(
	docid = "text",
	sentid = "int"
  ):

  """
  records dam name found in article
  """

  num_topics = 0


  if sentid in sentences1:
	num_topics += 1
	yield [docid, "sent"]

  if num_topics == 0:
	yeild [docid, None]

