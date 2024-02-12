# doc-bot
A medical chatbot that can talk about medicines, diseases, symptoms and treatments.

# Medical Chatbot

- Can chat about diseases and their symtopms, drugs and treatments etc. 
- Utilizes RAG (Retrieval-Augmented Generation) with a medicine encyclopedia provided as a pdf. (The document can be changed to make the bot more intelligent)
- Uses HuggingFace embeddings for vector conversion.
- Uses FAISS(Facebook AI Similarity Search) to create and store an index on the local machine.
- Uses the llama 2 LLM model for generating natural response.

## Screenshots

![App Screenshots](https://github.com/vishnusingh-12/doc-bot/blob/main/readme/bot.PNG)




## Deployment
<pre>git clone  https://github.com/vishnusingh-12/doc-bot
cd doc-bot
pip install -r requirements.txt
python embedding_creation.py
chainlit run model.py </pre>

The model uses GPU with CUDA 11.8 to run for which LlamaCpp has to be configured differently. Follow the below link for reference:
https://python.langchain.com/docs/integrations/llms/llamacpp

The model uses a quantized llama 2 model and can also run on cpu with no change in the code. If LlamaCpp Cuda version is available it uses GPU else it uses CPU. 


## Technologies
<img src="https://raw.githubusercontent.com/vishnusingh-12/main/readme/docbot.PNG">

## Support

For support, contact me:

[<img src="https://img.icons8.com/color/48/000000/gmail.png" alt="Gmail" width="30" height="30">](mailto:vishnusingh1995@gmail.com)
&nbsp;&nbsp;&nbsp;
[<img src="https://img.icons8.com/color/48/000000/instagram-new.png" alt="Instagram" width="30" height="30">](https://www.instagram.com/vishnusingh12/)
&nbsp;&nbsp;&nbsp;
[<img src="https://img.icons8.com/ios-filled/50/000000/github.png" alt="GitHub" width="30" height="30">](https://github.com/vishnusingh-12)
&nbsp;&nbsp;&nbsp;
[<img src="https://img.icons8.com/color/48/000000/linkedin.png" alt="LinkedIn" width="30" height="30">](https://www.linkedin.com/in/singh-vishnu)

