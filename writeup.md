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
![image](https://user-images.githubusercontent.com/15081906/139461715-f43f0835-bc0f-44f2-b17b-545dcf789ed6.png)

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
![image](https://user-images.githubusercontent.com/15081906/139461836-442f5371-4788-43fa-bb6b-98703160e47b.png)

#### Improve on the reference
Since typical image augmentations, which had been proven to be effective, are random brightness, and contrast adjustments, I decide to include them into final augmentation pipeline. However, I am not sure if other augmentation method is also helpful, so I decide to test one random augmentation that is random hue adjustment. From the graph below we can observe that random hue adjustment causes a huge training outlier at around step 1k. Therefore, I drop the random hue adjustment from final image augmentation pipeline.

Training graph of reference + random hue augmentation with default parameter setting
![image](https://user-images.githubusercontent.com/15081906/139461556-482f7d89-ffe3-4603-9d07-d528e71cf7d6.png)

Then, to test if random brightness and contrast adjustments create reasonable image for training, I use notebook "Explore augmentations.ipynb" to test those two adjustments. 
After comfirming both adjustments result in reasonable images, I ran the training again. The following graph is the result.
![image](https://user-images.githubusercontent.com/15081906/139514948-e175ff85-d005-4e59-83ca-1a0a77a9234d.png)

From above graph, it is interesting that with additional two random adjustments the training performance is just similar to reference. I suspect that having good reference training result is just pure luck. Therefore, I ran the reference training again. The following graph shows bad results from reference2 that supports the assumption.
![image](https://user-images.githubusercontent.com/15081906/139513812-d7afb175-36dd-4237-a6f5-3813b7ea370a.png)




