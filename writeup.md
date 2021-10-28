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
This section should detail the results of the reference experiment. It should includes training metrics and a detailed explanation of the algorithm's performances.

#### Improve on the reference
This section should highlight the different strategies you adopted to improve your model. It should contain relevant figures and details of your findings.
