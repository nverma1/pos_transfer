# pos_transfer
Neha and Jeffrey's Final Project

All functional code is contained within the IPython notebooks:

development.ipynb contains our baseline model, without any Dutch transfer learning or pretrained embeddings.

fasttext_embeddings.ipynb contains our baseline model, using unaligned fastText word embeddings.

fasttext_embeddings.ipynb contains our baseline model, using RCSLS-aligned fastText word embeddings.

transfer_testing.ipynb contains our model with Dutch transfer learning, without any pretrained embeddings.

transfer_testing_with_pretraining.ipynb contains our model with Dutch transfer learning, using unaligned fastText word embeddings.

transfer_testing_with_aligned_pretraining.ipynb contains our model with Dutch transfer learning, using RCSLS-aligned fastText word embeddings.

In order to run the models with aligned fastText word embeddings, please download the Dutch and Afrikaans files from https://fasttext.cc/docs/en/aligned-vectors.html and place them into a directory called .vector_cache in this directory. The files were too large, so we were not able to upload them onto GitHub. 

