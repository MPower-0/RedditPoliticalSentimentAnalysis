# RedditPoliticalSentimentAnalysis
My final year university project used a CNN model to classify Reddit comments as either left-wing or right-wing. The data was then analysed to search for trends. These trends were then displayed on a website.

The data to train the CNN model was collected by me using the scripts in the RedditDataCollection file. It accessed the API of the two UK-based political Subreddits r/labouruk and r/tories. I then manually classified the data and attempted to train the AI on it. However, as there was not enough data and I did not have enough time to manually label each comment I went with a more naive solution that involved labelling all comments of r/tories as right-wing and all comments of r/labouruk as left-wing. This helped increase the accuracy of the model but it could still only reach an accuracy of 67% due to the limited amount of data and the naive way in which I had to label it. I did continue with using the model to predict on the data and still analysed the information from the predictions. These trends were then graphed using Matplotlib and uploaded to a website to present this data.

![image](https://github.com/MPower-0/RedditPoliticalSentimentAnalysis/assets/78750387/6c1be402-4757-4acb-acb4-54431a63273e)

![image](https://github.com/MPower-0/RedditPoliticalSentimentAnalysis/assets/78750387/7629a5da-06df-4234-98da-a57e631a4b67)

![image](https://github.com/MPower-0/RedditPoliticalSentimentAnalysis/assets/78750387/fabdf576-4cb5-4f6f-83e0-6b798687f71b)
![image](https://github.com/MPower-0/RedditPoliticalSentimentAnalysis/assets/78750387/5c834eed-2a02-44e6-b4bb-1f359128448e)
![image](https://github.com/MPower-0/RedditPoliticalSentimentAnalysis/assets/78750387/90a522ec-8c62-4d5a-8e57-c09dcf277464)
![image](https://github.com/MPower-0/RedditPoliticalSentimentAnalysis/assets/78750387/c44b5134-6996-4ee0-ad38-e016cf3280d0)
![image](https://github.com/MPower-0/RedditPoliticalSentimentAnalysis/assets/78750387/37341eeb-4567-4da9-8e01-171dd33b35a1)

![image](https://github.com/MPower-0/RedditPoliticalSentimentAnalysis/assets/78750387/cb75f7f2-b204-4abc-801b-217c2f5cc06f)
![image](https://github.com/MPower-0/RedditPoliticalSentimentAnalysis/assets/78750387/ba4f54ca-a41a-4e9f-b790-48884543d942)
![image](https://github.com/MPower-0/RedditPoliticalSentimentAnalysis/assets/78750387/e1c4ce00-17e0-4be4-8cd1-ee6c7a2f0e50)
