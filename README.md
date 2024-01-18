# RedditPolitcalSentimentAnalysis
My final year university project used a CNN model to classify Reddit comments as either left-wing or right-wing. The data was then analysed to search for trends. These trends were then displayed on a website.

The data to train the CNN model was collected by me using the scripts in the RedditDataCollection file. It accessed the API of the two UK-based political Subreddits r/labouruk and r/tories. I then manually classified the data and attempted to train the AI on it. However, as there was not enough data and I did not have enough time to manually label each comment I went with a more naive solution that involved labelling all comments of r/tories as right-wing and all comments of r/labouruk as left-wing. This helped increase the accuracy of the model but it could still only reach an accuracy of 67% due to the limited amount of data and the naive way in which I had to label it. I did continue with using the model to predict on the data and still analysed the information from the predictions. These trends were then graphed using Matplotlib and uploaded to a website to present this data.

![image](https://github.com/MPower-0/RedditPolitcalSentimentAnalysis/assets/78750387/a326d5a4-aaf2-43f0-b703-a284bf239526)
![image](https://github.com/MPower-0/RedditPolitcalSentimentAnalysis/assets/78750387/1c54344b-291e-48ec-819a-9755b711f17c)

![image](https://github.com/MPower-0/RedditPolitcalSentimentAnalysis/assets/78750387/6c1ac2ab-7a56-4c09-9a44-5be129ce3cc3)
![image](https://github.com/MPower-0/RedditPolitcalSentimentAnalysis/assets/78750387/b20eb4b2-38a3-4887-8ea5-b48d29798ff0)
![image](https://github.com/MPower-0/RedditPolitcalSentimentAnalysis/assets/78750387/f4ea73d2-897f-428d-acd2-05e7759b1289)
![image](https://github.com/MPower-0/RedditPolitcalSentimentAnalysis/assets/78750387/6356426e-21be-4fa0-b4be-5b3d20a8a679)
![image](https://github.com/MPower-0/RedditPolitcalSentimentAnalysis/assets/78750387/b56bdcd6-b66e-427e-9f2e-82af544e4df1)
![image](https://github.com/MPower-0/RedditPolitcalSentimentAnalysis/assets/78750387/08f154b4-c500-4cf5-80b4-bc23d7563ae1)

![image](https://github.com/MPower-0/RedditPolitcalSentimentAnalysis/assets/78750387/782a3df3-c662-433c-ba07-a5d3b006f6f8)
![image](https://github.com/MPower-0/RedditPolitcalSentimentAnalysis/assets/78750387/3413a866-1209-4aa9-ade7-cf97eb686e2c)
![image](https://github.com/MPower-0/RedditPolitcalSentimentAnalysis/assets/78750387/08571935-7598-44c2-8210-38c0569732a8)
