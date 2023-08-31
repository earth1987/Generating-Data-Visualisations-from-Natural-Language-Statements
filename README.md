# Generating-Data-Visualisations-from-Natural-Language-Statements

## **Abstract** 
Over the past decade there has been an increase in data driven decision making
and, in-turn, adoption of centralised data-visualisation platforms, such as Tableau and PowerBI.
However, the creation of charts and dashboards requires data manipulation and visualisation expertise.
This inhibits many users’ ability to create bespoke content and perform new analyses. Typically
products now include natural language interfaces to reduce the reliance on technical expertise. But
these systems only support analytical phrases in English and require a user to directly resolve
ambiguities. In recent years, transformer-based language models have excelled at tasks requiring
semantic parsing of text. The goal of this project was therefore to develop a transformer-based model
capable of generating data visualisations from natural language statements. The results presented in
this show successful generation of data visualisations using pre-trained autoregressive models for the first time.

## **File structure**
<pre>
|- notebooks/
   |- 1_prompt_engineering.ipynb
   |- 4_test_inference.ipynb
   |- 5_validate_outputs.ipynb
   |- 6_logic_tests.ipynb
   |- archive/
   |- figures/
|- nl2vis/
   |- custom_funcs.py
   |- config.py
|- README.md
|- data/
   |- raw/
   |- processed/
   |- cleaned/
|- scripts/
   |- RO1_gptneo125m_1.sh
   |- shell-scripts.py
   |- archive/
|- environment.yml
|- William Pitchford - MSc in Data Science - Thesis 21 12 2022.pdf
<pre>
## **Notebooks**

**1_prompt_engineering.ipynb:**

**4_test_inference.ipynb:**

**5_validate_outputs.ipynb:**

**6_logic_tests.ipynb:**