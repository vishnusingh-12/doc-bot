# doc-bot
A medical chatbot that can talk about medicines, diseases, symptoms and treatments.

# Medical Chatbot

- Can chat about diseases and their symtopms, drugs and treatments etc. 
- Utilizes RAG (Retrieval-Augmented Generation) with a medicine encyclopedia provided as a pdf. (The document can be changed to make the bot more intelligent)
- Uses HuggingFace embeddings for vector conversion.
- Uses FAISS(Facebook AI Similarity Search) to create and store an index on the local machine.
- Uses the llama 2 LLM model for generating natural response.

## Screenshots

![App Screenshots](https://raw.githubusercontent.com/vishnusingh-12/doc-bot/)




## Deployment
<pre>git clone  https://github.com/vishnusingh-12/doc-bot
cd doc-bot
pip install -r requirements.txt
python embedding_creation.py
chainlit run model.py </pre>
Instead of python app.py you can also double click on app.py and wait for the application to run.

The model uses Pytorch and cuda 11.8 for training the model. The Drwosiness_detection.ipynb file has all the information to train your own custom model using CPU as well.
To run app.py (my custom model) torch and  opencv are required after cloning the repo.


## Technologies
<img src="https://raw.githubusercontent.com/vishnusingh-12/drowsiness-detection/master/readme/techs.PNG">

## Support

For support, contact me:

[<img src="https://img.icons8.com/color/48/000000/gmail.png" alt="Gmail" width="30" height="30">](mailto:vishnusingh1995@gmail.com)
&nbsp;&nbsp;&nbsp;
[<img src="https://img.icons8.com/color/48/000000/instagram-new.png" alt="Instagram" width="30" height="30">](https://www.instagram.com/vishnusingh12/)
&nbsp;&nbsp;&nbsp;
[<img src="https://img.icons8.com/ios-filled/50/000000/github.png" alt="GitHub" width="30" height="30">](https://github.com/vishnusingh-12)
&nbsp;&nbsp;&nbsp;
[<img src="https://img.icons8.com/color/48/000000/linkedin.png" alt="LinkedIn" width="30" height="30">](https://www.linkedin.com/in/singh-vishnu)

