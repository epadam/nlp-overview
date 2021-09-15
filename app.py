import streamlit as st
import spacy

st.title('Natural Language Processing Overview')



topic = st.sidebar.selectbox('Tasks',('Select a task', 'Part of Speech Tagging',  'Dependency Parsing', 'Named Entity Recognition', 'Textual Entailment', 'Text Classification', 'Text Similarity','Sentiment Analysis', 'Ranking', 'Question Answering', 'Machine Translation', 'Automatic Summarization', 'Dialogue System', 'Recommendation System']





if task == 'Select a task':
    st.write('Recent years machine learning based solutions has replaced rule-based solutions for NLP tasks. But always remember, machine learning is data driven. Without data, even you use Bert, the performance won''t be too good.')

    st.subheader('Dataset')

    st.write('Two most common datasets are [GLUE](https://gluebenchmark.com/) and [SQUAD](https://rajpurkar.github.io/SQuAD-explorer/). You can find more datasets [here](https://github.com/niderhoff/nlp-datasets) or on [Kaggle](https://www.kaggle.com/datasets?search=natural+language). A lot of deep learning frameworks such as [Tensorflow](https://www.tensorflow.org/datasets/catalog/overview), [PyTorch](https://github.com/pytorch/text) also include many datasets.')

    st.markdown('#### Data Augmentation')
    st.text('')

    st.write('What if you only have very little data? Generate more!!')

    st.write('There are couple of tools you can do data augementation fro NLP:')

    st.markdown('[**Snorkel**](https://www.snorkel.org/): Snorkel uses weakly supervision to generate training data.')


    st.subheader('Models, Libraries and Tools for NLP Tasks')

    st.write('Task in this overviwe will use common NLP libraies, such as Spacy, Huggingface or other pretrained models and compare them with statistic methods. Many pretrained models can be found in the major deep learning framework or there are many model Hub on the internet.')
    st.markdown('Spacy starts to use [deep learning models](https://spacy.io/models#architecture) since v2.0. But you can also load your own trained model. It has a clear comparisons of its usecases and performance with other tools. You can go check [here](https://spacy.io/usage/facts-figures).')
    st.markdown('AllenNLP also has very nice [demo](http://demo.allennlp.org) on multiple NLP tasks.')


    st.subheader('Performance Comparison')

    st.markdown('There are many benchmark websites for NLP tasks. [Here](https://gluebenchmark.com/leaderboard) you can see GLUE is dominated by Bert models. [NLP-progress](http://nlpprogress.com/) also shows benchmarks of a lot of NLP tasks with different dataset. Again, Bert models are in the top.')


if task == 'Part of Speech Tagging':
    st.header('Part of Speech Tagging')
    st.subheader('Dataset:')
    st.subheader('Models:')
    
    doc = st.text_input('Input text')

    st.write('Results:')

    st.subheader('code:')

    pos = ''' 
    
    import spacy
    nlp = spacy.load('en')
    tags = {w.pos:, w.pos_ for w in doc}

    '''



    st.code(pos, language='python')

    st.subheader('Applications:')

    st.write('POS tagging can be used for grammer correction.')
    

if task == 'Dependency Parsing':
    st.header('Dependency Parsing')
    st.subheader('Dataset:')
    st.subheader('Models:')
    
    doc = st.text_input('Input text')
    st.write('Results:')

    st.subheader('code:')
    # nlp= spacy.load("en")
    # doc = nlp(doc) 
    # for token in doc :
    #     st.write(token.text, token.tag_, token.dep_, token.head.text, token.head.tag_)

    st.subheader('Applications:')

    st.write('Like POS tagging, Dependency parsing can be used for grammer correction.')

if task == 'Named Entity Recognition':
    st.header('Named Entity Recognition')
    st.subheader('Dataset:')
    st.subheader('Models:')
    
    
    doc = st.text_input('Input text')
    st.write('Results:')

    st.subheader('code:')
    st.subheader('Entity Linkin')

    st.subheader('Applications:')

    st.write('1. NER can be also used for grammer correction.')

    st.write('2. NER is very import for Natural language understanding. It extracts key information from the sentence. This is especially important for Chatbot.')

    st.subheader('Interesting Research:')



if task == 'Textual Entailment':
    
    st.header('Textual Entailment (Natural Language Inference)')
    st.subheader('Dataset:')
    st.subheader('Models:')
    st.selectbox('Select an example', '')
    st.write('Results:')

    st.subheader('code:')

    st.subheader('Applications:')

    st.subheader('Interesting Research:')


if task == 'Text Classification':
    st.header('Text Classification')
    st.subheader('Dataset:')
    st.subheader('Models:')
    st.text_area('Type your text here.')
    st.write('Results:')

    st.subheader('code:')
    st.header('TF-IDF vs FastText vs Bert')

    st.write('Which model to use depends on size of your dataset, cost, and speed requirement.')

    st.subheader('Applications:')

    st.write('Text classification is one the most useful applications of NLP. It can be used to detect fake news, organizing documents in all sectors, code analysis, etc. IF you have a lot labeled data, Bert can do quite well on this task.')

    st.subheader('Interesting Research:')


if task == 'Text Similarity':
    st.header('Text Similarity')
    st.subheader('Dataset:')
    st.subheader('Models:')
    
    st.selectbox('Select an example','')
    st.write('Results:')

    st.subheader('code:')
    st.header('Cosine Similarity vs TF-IDF vs FastText vs Bert')

    st.subheader('Applications:')

    st.write('Traditional methods use key words and statistics methoos. But deep learning models can capture the context of the words in different contents. This is especially for words with different meanings or articles describing same things with different words.')

    st.subheader('Interesting Research:')

if task == 'Sentiment Analysis':
    st.header('Sentiment Analysis')
    st.subheader('Dataset:')
    st.subheader('Models:')
    st.text_area('Type your text here')
    st.write('Results:')

    st.subheader('code:')
    st.subheader('Applications:')

    st.write('Obviously this can be used for customer services or chatbot. When it is combined with computer vision and voice recognition, it can capture the true emotion of a person.')

    st.subheader('Interesting Research:')


if task == 'Ranking':
    st.header('Ranking')
    st.subheader('Dataset:')
    st.subheader('Models:')
    st.selectbox('Choose an example', '')

    st.write('Results:')

    st.subheader('code:')

    st.subheader('Applications:')

    st.write('This is can be seen as a higher level task for similarity task. It is often used for searching and reconmendation. Q&A Chatbot also use it a lot.')


    st.subheader('Interesting Research:')

if task == 'Question Answering':
    st.header('Question Answering')
    st.subheader('Dataset:')
    st.subheader('Models:')
    st.text_area('Phrase')
    st.text_input('Question')
    st.write('Results:')

    st.subheader('code:')

    st.subheader('Applications:')

    st.write('This is very useful for all the Q&A system like customer services or in chatbot.')


    st.subheader('Interesting Research:')


if task == 'Machine Translation':
        st.header('Machine Translation')
        st.subheader('Dataset:')
        st.subheader('Models:')
        st.write('Results:')

        st.subheader('code:')
        st.subheader('Applications:')

        st.write('The application is just same as the title.')

        st.subheader('Interesting Research:')

if task == 'Automatic Summarization':
    st.header('Automatic Summarization')
    


    st.subheader('Extractive Summarization')
    st.write('Extractive summerization refers to pick important sentences in the article as the abstract or summerization.')
    st.markdown('#### Dataset:')
    st.markdown('#### Models:')
    st.markdown('#### code:')

    st.subheader('Generative Summarization')
    
    
    st.markdown('#### Dataset:')
    st.markdown('#### Models:')

    st.subheader('Applications:')

    st.write('This is personally application I want. How nice would it be if you write an article or paper and the abstract is automatically generated.')

    st.subheader('Interesting Research:')


    

if task == 'Dialogue System':
    st.header('Dialogue System')
    st.write('Dialogue system is also called conversational AI. It may combine many different models and couple of different NLP tasks.')
    st.image('rasa.png',caption='from https://legacy-docs.rasa.com/')
    st.subheader('1. Natural Language Understanding')

    st.write('NLU extract the key information from the user. The task most includes NER/Enity linking, intent classification and slot-filling. Slot-filling can be treated as a expanding task of NER. Here we discuss approaches from different research.')

    st.markdown('#### NLU with Knowledge Graph')

    st.write('Some research directly use Knowledge graph to train the model or build a co-training model and some uses it seperately as a two step solution. Here we discuss the literature with different methods')

    st.image('kgt.png', use_column_width=True)


    st.subheader('2. Dialogue State Tracking')

    st.write('DST is mostly used for multi-turn conversation. It stores the origin messages and other elements extracted from NLU. Here we first show how the open source framework Rasa realize the task and discuss other methods in literature.')


    st.subheader('3. Dialogue Policy')

    st.write('Dialogue policy predict the most suitable action based on the information from DST. Here again, we show the basic model used by Rasa and other solutions.')
    st.image('dp.jpg', use_column_width=True ,caption='https://blog.rasa.com/attention-dialogue-and-learning-reusable-patterns/')

    st.markdown('#### Dialogue Policy with Knowledge Graph')

    st.write('A lot of contents can not be stored in dialog policy module. Therefore,you can use the information stored in knowledge graph for different actions. Here we show some examples.')

    st.subheader('4. Natural Languae Generation')


    st.write('After the model predict the action, it will be sent to NLG module to generate proper text reply.')

    st.markdown('#### Generative models')

    st.write('Transformer is the most common model for text generation.')

    st.markdown('#### Retrieving based solutions')

    st.write('Some applications can have predefined text that matches the action.')

    st.header('Types of chatbot')
    st.subheader('Simple Q&A chatbot')
    st.write('A simple Q&A chatbot may not follow the architecture mentioned above but recall and rerank models. It finds a list of possible answers to the quesions, and use machine learning model to predict the most possible answers to the question.')
    st.subheader('Task Oriented chatbot')
    st.subheader('Multi-Task chatbot')

    st.header('Framework')
    st.subheader('Rasa')
    st.write('New veriosn of Rasa starts to support Bert for NLU, they also develop their own NLU model called DIET')
    st.markdown('Useful tool for RASA development')
    st.markdown('[RASA-ui](https://github.com/paschmann/rasa-ui)')
    st.markdown('[Botfront](https://github.com/botfront/botfront)')
    st.markdown('[RasaLit](https://github.com/RasaHQ/rasalit)')



    st.subheader('Deepavlov and Deepavlov agent')
    st.write('DeepPavlove agent is a library for developing multi skill chatbot. DeepPavlov already includes many pretrained models. It can also connect to RASA')
    # st.markdown('#### Nvidia Nemo')
    # st.text('Like DeepPavlov, Nemo also includes many pretrained models')


if task == 'Recommendation System':
    st.header('Recommendation System')


    


    
    
    





