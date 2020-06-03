# **GABIBOT**
 Gabriela Pardo de Andrade Aljure <br>
 *Data Part Time Barcelona Dec 2019*
 
## Content

1. [Project Description](#id1)
2. [Hypothesis](#id2)
3. [Dataset](#id3)
4. [Model](#id4)
5. [Model Training](#id5)
6. [Conclusions](#id6)
7. [Future Work](#id7)
8. [Workflow](#id8)
9. [Links](#id9)



### Project Description<a name="id1"></a>

The objective is a **Self-learning Generative Chatbot** which replies with sarcasm.

### Dataset<a name="id3"></a>

For the project I'm using the Self-Annotated Reddit Corpus (SARC), which I converted to a dataset. Luckly for me it was just what I was looking for; it works perfectily for my proyect given that it's made up of 1.3 million sarcastic comments and what a generative model needs is enough information to learn. You can learn more about this amazing project in their repo: https://github.com/NLPrinceton/SARC

Dataset I created contains: 
- 3 columns [Question, Answer_1, Answer_2, ]; where 'Question' is a reddit comment and 'Answer_1' and 'Answer_2' are sarcastic replies.
- 

## Model<a name="id4"></a>

 The model itself is made with Keras. 
 It has 4 layers: Input, Embedding, Dense & LSTM; you can found more about what they do in the 'model_creation' document


## Model Training<a name="id5"></a>

Training takes for ever, GPUs save lives.

The objective of the final model is for it to be trained with 


## Conclusion<a name="id6"></a>

Generative models need a lot of resources and time. If you don't have enough resources make sure to use VM and a lot of time.
I have to make sure I inform myself of what I will be doing and what I will need befor strarting working, because depending on how much data I was using the VM was asking me up to a minimum of 1TB. 
It's never as easy as it seems.
Whenever you look for examples make sure the code it not from 5 years ago... if it is, but it what you need... let it go.
If your get yourself in a .pkl like making a generative model make sure there's absolutley NO WAY OUT. If there is you will most likely take it.


## Future Work<a name="id7"></a>

Try with the Sequential() model
Try other RNN layers such as GRU or Bidirectional layer.
Try different en/decoding methods.
Try different parameters when compiling the model.
Try a training with more than 500 epochs (depending on the results) or from different machines at the same time to be more time efficient

## Workflow<a name="id8"></a>

 1. Investigation: most of my time was invested in investigation. What was a generative model? How did it work? How could I create a chat bot with it? An issue that came up during my investigation was: Where will I get enough data to tran a generative model? Generative models need very big amounts of information.
 
 2. Trial & Error: Paralel to the investigation I worked with a lot of models, many worked, many didn't. I not only worked with Generative models but also with Retraival based models so I could get familiarized with all the aspects of the chatbot world.
 
 3. The proyect: Once I learned enough about generative models and had seen enough of them, I was able to work with them and understand what I was doing and started working on the proyect. Most of the issues came from the big amout of data that I've worked with and the number of epochs (iterations through the dataset) I decided where the minimum necessary: 500. 
 
 Interface Creation: Telegram, with Fatherbot, 

## Links<a name="id9"></a>
