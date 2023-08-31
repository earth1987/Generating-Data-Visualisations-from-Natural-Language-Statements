# Generating-Data-Visualisations-from-Natural-Language-Statements

## **Abstract** 
Over the past decade there has been an increase in data driven decision making and, in-turn, adoption of centralised data-visualisation platforms, such as Tableau and PowerBI. However, the creation of charts and dashboards requires data manipulation and visualisation expertise. This inhibits many users’ ability to create bespoke content and perform new analyses. Typically products now include natural language interfaces to reduce the reliance on technical expertise. But these systems only support analytical phrases in English and require a user to directly resolve ambiguities. In recent years, transformer-based language models have excelled at tasks requiring semantic parsing of text. The goal of this project was therefore to develop a transformer-based model capable of generating data visualisations from natural language statements. The results presented show successful generation of data visualisations using pre-trained autoregressive models for the first time.

## **File structure**
<pre>
|- notebooks/
   |- 1_prompt_engineering.ipynb
   |- 2_train_inference.ipynb
   |- 3_validate_train_outputs.ipynb
   |- 4_test_inference.ipynb
   |- 5_validate_outputs.ipynb
   |- 6_logic_tests.ipynb
   |- archive/
   |- figures/
|- nl2vis/
   |- custom_funcs.py
   |- config.py
|- data/
   |- raw/
   |- processed/
   |- cleaned/
|- scripts/
   |- RO1_gptneo125m_1.sh
   |- shell-scripts.py
   |- archive/
|- environment.yml
|- README.md
|- William Pitchford - MSc in Data Science - Thesis 21 12 2022.pdf
</pre>

## **Notebooks**

**1_prompt_engineering.ipynb**

This workbook is used to create prompts comprised of five key components: a description of the task, completed in-context examples, metadata describing the content of the relevant dataset, the problem of interest and an incomplete solution which acts as a prefix to the generated tokens.

In-context examples are matched with problems based on semantic similarity. For a given problem the semantic search was implemented using the below steps.
1. The NL query and pool of potential examples were vectorized using one of two pre-trained sentence encoders: Sentence-BERT (paraphrase-MiniLM-L6-v2, embedding size: 384) or a multilingual Universal Sentence Encoder (distiluse-base-multilingual-cased-v1, embedding size: 512) (Reimers, Gurevych, 2019, Yang et al., 2019).
2. Cosine similarity between the given NL query and pool of example embeddings was computed.
3. The pool of potential examples was sorted in descending order of cosine similarity score. The highest scoring example was assumed to be the most semantically similar. The top one to three examples were used.

**2_train_inference.ipynb**

This workbook enables inference using pre-trained autoregressive models implemented in the Hugging Face library. Ten-fold cross validation hyperparameter grid searches are conducted on the training data. When testing problems in a validation set, in-context examples are drawn from the remaining nine sets. This approach enables optimisation of the prompt design (number of in-context examples) and decoding strategy (Top-P: threshold p, Top-K: threshold k & softmax temperature).

Note: Two pre-trained autoregressive models developed by EleutherAI were used in this research project: GPT-Neo and GPT-J. 

**3_validate_train_outputs.ipynb**

Two evaluation metrics are utilised: valid@k and pass@k. Valid@k represents the validation rate with k samples. For example, valid@1 would represent the fraction of problems of which the model generated a valid Vega-Lite specification in 1 sample. Similarly, pass@k represents the pass rate with k samples. Where pass@1 would represent the fraction of problems of which the model generated a Vega-Lite specification that passed all logical tests. Similar to recent studies, model performance was also assessed when k was greater than one. Specifically, with with 10 independent samples per problem.

**4_test_inference.ipynb**

**5_validate_outputs.ipynb**

**6_logic_tests.ipynb**