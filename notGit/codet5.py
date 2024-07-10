from transformers import RobertaTokenizer, T5ForConditionalGeneration

tokenizer = RobertaTokenizer.from_pretrained('Salesforce/codet5-base')
model = T5ForConditionalGeneration.from_pretrained('Salesforce/codet5-base')

text = "how i made new chat bot with js and json data?"
input_ids = tokenizer(text, return_tensors="pt").input_ids


# simply generate one code span
generated_ids = model.generate(input_ids, max_length=300)
print(tokenizer.decode(generated_ids[0], skip_special_tokens=True))
# this prints "{user.username}"
