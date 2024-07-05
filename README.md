## Student Performance Indicator

A machine learning project to predict student performance based on various features.

## Introduction
This project understands how the students performance (test score) is affected by other variables such as Gender, Ethnicity, Parental level of education, lunch and test preparation course.

## Features
- Predicts student performance
- Analyzes various factors affecting performance
- Provides actionable insights for educators

### Life Cycle Of the Project

1) Understanding the problem statement
2) Data Collection
3) Data checks to perform
4) Exploratory data analysis
5) Data Pre-processing
6) Model Training
7) Choosing Best model

### Images - 
![Dataset](images/data_head)

#### Dataset Information

1) Gender : Sex of students -> (male/female)
2) race/ethnicity - ethnicity of students -> (Group A, B, C, D, E)
3) Parental level of education : Parents final Education
4) lunch : having lunch before test (standard or free/reduced)
5) test preparation course : Complete or not complete before test
6) math score 
7) reading score
8) writing score

![Data_Info](images/data_info)

### Distribution of the average score
![Distribution_of_avg_score](images/avg_score_dist)
From the above graph we can see that female students have performed well than male students.

### Distribution of average score w.r.t lunch type
![Dist_with_lunch](images/lunch)
Insights - Standard lunch helps perform well in exams. 

### Distribution of average score w.r.t parental level of education
![Dist_with_parental_education](images/par_ed)
Insights - In general parent's education dont help students perform well in exam.

### Maximum scores of students  in all subjects.
![max_score](images/max_scores)

### Multivariate analysis
![multivariate_analysis](images/multi)

### Feature wise analysis - 
#### Distribution of gender
![gender_dist](images/gender)

#### Distribution of race/ethnicity
![dist_race](images/ethnicity)

#### Distribution of lunch
![dist_lunch](images/dist_lunch)

![test_prep](images/test_prep)

## Outliers
![outliers](images/outliers)



## Conclusion - 

1) Students performance is related with lunch, race, parental level education
2) Females lead in pass percentage and also are top scorers. 
3) Students performance is not much related with test preparation course. 
4) Finishing preparation course is beneficial. 


Model is built with approximate accuracy of 88%.

## Web app 
![Web_app](images/web_app)