# SuperMart
WIth the Internet Booom and Social Media as well as the Pandemic, the growth of online shopping practices have just gone up, and which customer does not like items to be personalized and make them feel at home? Similarity search and recommendation systems have shown us how the big tech firms make global impact and control the world.
So for every unique customer, we need to have well curated and peronalized list of products ready, because if the company does no invest in it, the customer will just move to someone who understands them better

-Here segmentation of users based on RFM modelling has been performed and Personalized recommendations based on Collaborative filtering is implemented 

-Cold Start problem: when the system does not have any history of buying trends and faces a new customer, it should still be appealing, to tackle it the system recommends Popular products and based on the actions performed thereafter, the similar and curated products are shown
 
 # Report
 
 CLAAT: https://codelabs-preview.appspot.com/?file_id=1Sw4fG-F6BLDCx5oMwuYoyhWEHMqgGy9IXSjnGi7SklY#0
 
# Dashboard

https://datastudio.google.com/u/0/reporting/8fe1e49e-78be-4b1b-b2b5-94ad5d9db854/page/UIhtB
https://datastudio.google.com/u/0/reporting/8fe1e49e-78be-4b1b-b2b5-94ad5d9db854/page/ypstB
![image](https://user-images.githubusercontent.com/49743328/113927956-27a98900-97bc-11eb-9d80-06853d7dac37.png)
![image](https://user-images.githubusercontent.com/49743328/113927989-309a5a80-97bc-11eb-92e7-440f8e2565ca.png)

# Approach

Performed EDA and analyzed customer behavior trends to better understand our customer's data
Segmented the customers using RFM Modelling based on their purchasing history. Also, calculated the CLV to understand the importance of each customer.
Provided personalised recommendations to users by predicting their ratings based on collaborative filtering
Excecuted 4 collaborative models and compared its evaluation metrics to chose the model most ideal model for our prediction
For new users recommend products based on popularity
The users have an option to search for products and get a list of products similar to their search
Created an interactive dashboard to analyze the sales based on customer segments.

# Customer Segmentation

We cannot treat every customer with the same importance.They will find another option which understands them better.
Each customer has a different profile and we need to tailor our recommendations based on their profiles.
In order to better understand our customers we segment our customers based on their RFM values.
By using the RFM score we segment our customers into Top,Lost and Regular customers

# Recommendation

A recommender system predicts the rating value of a user-item combination with an assumption that the training data available indicates a user’s preference for other items.
We use the user-item Interaction Data, such as ratings and apply various modelling techniques that uses collaborative filtering to predict user’s preference.
Executed 4 collaborative modelling techniques :

-FastAI

-Alternating Least Square (ALS)

-Simple Algorithm for Recommendation (SAR)

-Surprise Singular Value Decomposition (SVD)

Compared the evaluation metrics and chose SVD as most ideal for our dataset
Based on the predicted ratings we recommended top-k items to a particular user.
For new users as we do not have their preferences we recommend most popular products.
We check for products which are most purchased and are highly rated to recommend those for new users
Search
Users can find the products they are looking for using the Search feature
The search feature also lists the products similar to the items being searched
Used text processing to find similar products.
Created a Document Term Matrix using TF-IDF to extract vectors
Using cosine similarity we calculated proximity between strings
Based on similarity values we created product groups
