# Machine Learning for Conversational AI

Chatbot is probably the most challenging application in NLP. It requires almost all tasks above to give smooth communicating experience.
It can be simple Q&A chatbot, task specific cahtbot to open domain chatbot or all-in-one chatbot. 

## Classfication FAQ Chatbot (Data in the training dataset)

1. Simple classification
2. QQ pair and return Answer

## Open/Close Domain Chatbot (Information Retrieval)

For this kind of chatbot, you don't really need chatbot framework since there's no intention. Haystack with input

A. QA Chatbot (Doesn't need chatbot framework)
1. Reading Comprehension Chatbot (single Document)
2. Retrieve -> Reader (multiple Documents, can also be multi-hop) 
3. Knowlege Graph (NER -> KG -> Generator)
4. End-to-End (pretrained transformer like Meena, BlenderBot)

B. Multi-Turn Chatbot

* [Comparison of Transfer-Learning Approaches for Response Selection in Multi-Turn Conversations](http://workshop.colips.org/dstc7/papers/17.pdf)

* [Towards a Conversational Agent that Can Chat About…Anything](https://ai.googleblog.com/2020/01/towards-conversational-agent-that-can.html)


## Task Oriented/Mutli-task Chatbot 

If you need a task oriented chatbot or a multiple functions chatbot including FQA, chitchat, then you need a chatbot framework to recognize the intention first

It's also possible for rasa to train the model end-to-end without NLU.

### NLU

It requires NLU, which include intent extraction, Name Entity Recognition, Relation Extraction, Enitity Linking

* Joint Classification of NER and Intention

  * [DIET from RASA](https://github.com/RasaHQ/rasa/blob/main/rasa/nlu/classifiers/diet_classifier.py) 


### Dialog State Tracking

This component store chat history, NER and the slot

### Dialog Policy

* [TEDpolicy](https://github.com/RasaHQ/rasa/blob/main/rasa/core/policies/ted_policy.py)

### NLG
