Team: Guirong Luo, Ilesh Sharda, Ruixi Wang, Xinming Yang, Xin Zhao
# Group-Formation
Use AI models to create well-balanced student groups for different projects

6 reasons for opposite personalities work well together. Matt Duczeminski states that:
- They can complement each other
- They encourage each other
- They compensate for each other’s weaknesses
- They can realize greatness in those unlike themselves
- They can experience more
- They can be comfortable being themselves 

## Data Simulation

Advantages:							
- Students’ info is confidential
  - Avoid privacy issue
- Large dataset 
  - Improve performance of deep learning models
- Flexible
  - Adjustable threshold for different needs

![image](https://user-images.githubusercontent.com/73065775/177408793-e1e21da7-f394-4520-ba9f-bf5b69fed61f.png)

- We simulated 1 million student records based on statistical facts of the U.S. population:
- The table shows that we created 5 features and 11 interpersonal skills for 1 million students. 
  - It includes gender, race, a binary of international status variable, technical skill, reading score
  - 11 interpersonal skills

Gender:
We simulate 50% male and 50% female students by default. If the user of our model has a gender inequality distributed class, he/she can customize the percentage of male students, satisfying different needs.

Reading_score:
The reading score is followed by a skew-normal distribution. Users can use students self-evaluation scores as students’ reading scores for our model.

Race:
The race is simulated with the probability that followed by the U.S. race population percentage.

International_stu:
International_stu is a binary variable that represents a student is an international student or U.S. domestic student. The initial percentage of international students among the total sample set is 6% [8]. Similarly, users can personalize the percentage according to the reality.

Techncial_skill:
- Techncial_skill is a binary variable that can meet users’ expectations. 
- For example, if a user expects students to know fundamental python skills when assigning to the project group, he/she can use this variable to represent the required skill. 
- The entire dataset has a 20% of students who have target skills by default. The percentage can be customized with the function input.


![image](https://user-images.githubusercontent.com/73065775/177409186-c67f24f8-fa80-42bf-8d1d-0652a5d9d688.png)

CareerLeader® website: https://www.careerleader.com/             

Interpersonal skills:

Career Leader is a professional company that is committed to help students make better career choices and decisions. Report contains personalized results in Interests, Motivators, Skills, Career Match, CultureMatch™, and Things to Be Alert For.

When students take the self-assessment, we expect 11 scores of interpersonal skills follow by normal distribution for each student.

We simulate our dataset based on this statistics fact

![image](https://user-images.githubusercontent.com/73065775/177409741-b5d92560-93fd-486f-884d-1c11dc6d81b7.png)

## Methodology

- The classic K-Means algorithm clusters data by separating samples in N groups of equal variance, minimizing a criterion known as the inertia or within-cluster sum-of-squares.
- The nonlinear neural networks breaks the linearity by using a bunch of activation functions.
- The autoencoder deep learning model has autoencoders to learn abstract features in an unsupervised way.

![image](https://user-images.githubusercontent.com/73065775/177410069-50680334-da06-4906-a9ca-d8fe3492ef50.png)

## Model Result

The business goal is to form well-balanced groups with students from each cluster, we have 5 models to accomplish the goal:
- K-Means - Baseline model to compare model performance
- NonlinearNN - Model includes full dataset
- Autoencoder1 - Model includes full dataset
- Autoencoder2 - Model includes  11 interpersonal skills
- Autoencoder3 - Model includes Gender, international student, reading score, and technical skill

![image](https://user-images.githubusercontent.com/73065775/177410530-e84f09ee-abb7-4a34-9bea-71425ef4b06b.png)

To meet professors or users need, they should pick a model based on their criteria:
- If professor consider all factors for group formation:
  - nonlinear neural network model.
- If professor consider race factor is important
  - autoencoder model 1.
- If professor consider interpersonal skills are critical
  - autoencoder model 2.
- If professor looks for groups that at least one student has required skill, at least one female, one male, and one international student
  - autoencoder model 3.

## Model Implementation

![image](https://user-images.githubusercontent.com/73065775/177410866-190a0d3d-9ed6-40ab-8ce4-69b18401f677.png)


## Business Impacts

- A reasonable, realistic and intelligent technique for professors, instructors to group students. It permits instructors to select the set of students to form groups with homogeneous backgrounds or heterogeneous, diversified for different assignments.
- The attributes of the dataset could be up-to-date as long as users input the most recent collected students’ information. And the number of clusters could also be modified with needs. The succeeding visualizations section would aid in obtaining the properties of each group.
- The application may be beneficial not only limited to the formation of student groups but also to the formation of project teams in enterprises.






