#Reading File in data frame MyData
#score file contains information about splits and classifier and F-score
MyData <- read.csv(file="D:\\SJSU_courses\\256_Large_Scale_Analytics\\project\\score.csv", header=TRUE, sep=",")
str(MyData)

library(ggplot2)
library(dplyr)
library(stringr)

df <- MyData
df <- df %>% 
  mutate(FScore = FScore-0.9)

str(df)

df1 <- df %>% 
  group_by(Classifier) %>%
  summarise(Mean_FScore = mean(FScore))

str(df1)

ggplot(data=df, aes(x = Test_data_split, y =FScore  , group = Classifier, fill = Classifier)) + geom_bar(position="dodge",stat="identity")

ggplot(data=df1, aes(x = Classifier, y =Mean_FScore  ,  fill = Classifier)) + geom_bar(position="dodge",stat="identity") 

#score file contains information about number of folds and classifier and Cross Validation score
crossData <- read.csv(file="D:\\SJSU_courses\\256_Large_Scale_Analytics\\project\\cross1.csv", header=TRUE, sep=",")
str(crossData)

dfc <- crossData
dfc <- dfc %>% 
  mutate(Cross_validation_score = Cross_validation_score-0.9)

ggplot(data=dfc, aes(x = No_of_folds, y =Cross_validation_score  , group = Classifier, fill = Classifier)) + geom_bar(position="dodge",stat="identity")
