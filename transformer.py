from transformers import pipeline
from transformers import AutoTokenizer, AutoModelForSequenceClassification
import torch
import torch.nn.functional as F
model_name = "distilbert-base-uncased-finetuned-sst-2-english"

model = AutoModelForSequenceClassification.from_pretrained(model_name)
tokenizer = AutoTokenizer.from_pretrained(model_name)

classifier = pipeline("sentiment-analysis",model = model,tokenizer = tokenizer)
res = classifier("hello! nice to meet you")

print(res)

token = tokenizer.tokenize("hey! nice to meet you")
token_ids = tokenizer.convert_tokens_to_ids(token)
input_ids = tokenizer("hey! nice to meet you")

print(f'   Tokens: {token}')
print(f'Token Ids: {token_ids}')
print(f'Input IDs: {input_ids}')

x_train = ["hey! nice to meet you","I love strawberries!"]


batch = tokenizer(x_train,padding = True,truncation = True, max_length = 512, return_tensors = "pt" )

with torch.no_grad():
    outputs = model(**batch)
    print(outputs)
    predictions = F.softmax(outputs.logits,dim = 1)
    print(predictions)
    labels = torch.argmax(predictions,dim = 1)
    print(labels)

#save model
save_directory = "saved"
tokenizer.save_pretrained(save_directory)
model.save_pretrained(save_directory)

#pull model out
tokenizer = AutoTokenizer.from_pretrained(save_directory)
model = AutoModelForSequenceClassification.from_pretrained(save_directory)


