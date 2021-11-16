# Contextual Reasoning in Visual Dialog


### Images and Annotations
Please download the images from GQA and CLEVR, for the annotations of GQA-VD and CLEVR-VD, Please click [here]()

### Dataset Generation Code
1. Download Glove pretrained word vectors
2. Download the Scene Graphs From CLEVR and GQA
3. Preprocess the pretrained word vectors and scene graphs with 
```
python preprocess.py --scene <scenegraph> --embed <wordembedding>
```
4. Generate the sampled contexts with 
```
python context.py --compound <compoundlist> --visual <preprocessed>
```
5. Question Engine
```
python question_engine.py --context <contexts> --template <templateList>
```

### Model Test on the Dataset
To run our model on the CLEVR-VD and GQA-VD
```
python NDM.py --data <CLEVR-VD_dir>
```
