# Contextual Reasoning in Visual Dialog


### Images and Annotations
Please download the images from GQA and CLEVR, for the annotations, Please generate them with the following instructions.
### Dataset Generation Code
1. Download Glove pretrained word vectors
2. Download the Scene Graphs From CLEVR
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
### GQA-VD Data Samples
[1 Dialog (10QA) Per Image]
https://drive.google.com/file/d/1GR9NTGMQ7V_7tCayy2kMFNcoWsS-t-16/view?usp=drive_link

[2 Dialogs (10QA) Per Image]
https://drive.google.com/file/d/1gletyyUzkdVoqkrkZmBzTb4hpKMoVheb/view?usp=drive_link

### Model Test on the Dataset
To run our model on the CLEVR-VD and GQA-VD
```
python train.py --data <CLEVR-VD_dir>
```
