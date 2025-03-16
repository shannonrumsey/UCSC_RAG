from transformers import AutoModelForQuestionAnswering, AutoTokenizer, pipeline

model_name = "deepset/roberta-base-squad2"


nlp = pipeline('question-answering', model=model_name, tokenizer=model_name)
QA_input = {
    'question': 'Why is model conversion important?',
    'context': 'The option to convert models between FARM and transformers gives freedom to the user and let people easily switch between frameworks.'
}
res = nlp(QA_input)
print(res)

model = AutoModelForQuestionAnswering.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

from transformers import pipeline
unmasker = pipeline('fill-mask', model='bert-base-uncased')

first = unmasker("he [MASK] his [MASK] [MASK] on my [MASK] and we started [MASK] [MASK] [MASK] [MASK] penetration [MASK] [MASK] [MASK] Jewish.")[0][0]["sequence"]

print(first)
print(type(first))
second = unmasker(first)[0][0]["sequence"]
third = unmasker(second)[0][0]["sequence"]
forth = unmasker(third)[0][0]["sequence"]
fifth = unmasker(forth)[0][0]["sequence"]
sixth = unmasker(fifth)[0][0]["sequence"]
seventh = unmasker(sixth)[0][0]["sequence"]
eigth = unmasker(seventh)[0][0]["sequence"]
ninth = unmasker(eigth)[0][0]["sequence"]
tenth = unmasker(ninth)[0][0]["sequence"]
eleventh = unmasker(tenth)[0]["sequence"]
print(eleventh)
