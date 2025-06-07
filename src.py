"""loads hendrycks_math dataset and saves train and test splits to json files"""
from datasets import load_dataset

types = ['algebra', 'counting_and_probability', 'geometry', 'intermediate_algebra', 'number_theory', 'prealgebra', 'precalculus']

for t in types: 
    dataset = load_dataset("EleutherAI/hendrycks_math", t) 
    dataset['train'].to_json('data/hendrycks_math_' + t + '_train.json')
    dataset['test'].to_json('data/hendrycks_math_' + t + '_test.json')
    
dataset = load_dataset("commonsense_qa")
dataset['train'].to_json('data/common_sense_train.json')
dataset['test'].to_json('data/common_sense_test.json')
dataset['validation'].to_json('data/common_sense_validation.json')

for t in ["main", "socratic"]: 
    dataset = load_dataset("gsm8k", t)
    dataset['train'].to_json('gsmk8_'+ t + '_train.jsonl')
    dataset['test'].to_json('gsmk8_'+ t + '_train.jsonl')