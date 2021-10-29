### Project overview
Goals of the project:
- Familiarize the whole object detection pipeline which includes image data analysis, data split, data augmentation, clone pre-trained model, training model and cross validation

The importance of object detection for driving car systems:
- Object detection is a crucial step for Self-driving car to understand its surrounding environment in order to make behavior planning

### Set up
Please refer to readme which includes the procedures for running this code.

### Dataset
#### Dataset analysis
Use Exploratory Data Analysis.ipynb to run dataset analysis. The results show the majority of objects in the image is vehicle. Less than 1% of images have no objects. It is good because the model will see many objects in the image and won't learn to predict no objects.
![image](https://user-images.githubusercontent.com/15081906/139235898-6db0e886-e89f-4b1f-9638-da60ef01f685.png)

![image](https://user-images.githubusercontent.com/15081906/139236474-57c03b06-20c9-4444-98be-23bc3d5f64d1.png)

#### Cross validation
Since there aren't many raw training images, I decided to create a cross-validation set to evaluate if the model is overfitting. My split is 75/15/10 for train, val and test dataset. 

### Training 
#### Reference experiment
Due to GPU memory limitation in Udacity VM, I decide to run evaluation after training process finishes. While running evaluation, I encounter the type error message. To bypass this error, the setting "metrics_set" was changed to "pascal_voc_detection_metrics". From the training curve, we can observe that validation has higher loss than training and training loss is still dropping. In addition, validation loss tends to be flat afer step 19k. Both trends indicate that the training is overfitting to the training set. 
Training graph
![image](https://user-images.githubusercontent.com/15081906/139452966-9ca4903f-1a9f-48a5-a1c7-b5d730b932c1.png)

Here are validation results at step = 19k and 20k
|Metric|19k|20k|
|---|---|---|
|mAP@0.5IOU|0.1233|0.1337|
|vehicle|0.0969|0.0986|
|pedestrian|0.1497|0.1689|
|cyclist|nan|nan|
|localization_loss|0.3694|0.3724|
|classification_loss|0.2900|0.2998|
|regularization_loss|0.1330|0.1290|
|total_loss|0.7924|0.7924|0.80133|

Validation graph
![image](https://user-images.githubusercontent.com/15081906/139453985-c134d5c5-32aa-4721-9b70-5ce3e4409e44.png)

#### Improve on the reference
This section should highlight the different strategies you adopted to improve your model. It should contain relevant figures and details of your findings.
