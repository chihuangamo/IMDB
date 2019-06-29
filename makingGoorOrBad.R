df <- readRDS("imdb.rds")
const <- readRDS("const.rds")
movie_df <- df %>% 
  filter(titleType == "movie") %>% 
  filter(numVotes >= 10) %>% #numVote >= 10
  group_by(tconst) %>% 
  slice(1) %>% 
  filter(numVotes >= 10) %>%  
  ungroup()

const <- const %>% 
  left_join(movie_df %>% select(tconst, averageRating),
            by = "tconst")
median(const$averageRating)#6.1
hist(const$averageRating)
const <- const %>% 
  mutate(good_or_bad = ifelse(averageRating > 6.1, 1, 0))


library(tidyr)
movie <- spread(const %>% mutate(dummy=1) , nconst, dummy)
all_nconst <- const %>% count(nconst) %>% select(-n)

all_nconst <- all_nconst %>% 
  full_join(const, by = "nconst")

movie_crew <- const %>% 
  arrange(tconst) %>% 
  group_by(tconst) %>% 
  mutate(nconst_1 = lag(nconst, 1)) %>% 
  mutate(nconst_2 = lag(nconst, 2)) %>%
  mutate(nconst_3= lag(nconst, 3)) %>%
  mutate(nconst_4= lag(nconst, 4)) %>%
  mutate(nconst_5= lag(nconst, 5)) %>%
  mutate(nconst_6= lag(nconst, 6)) %>%
  mutate(nconst_7= lag(nconst, 7)) %>%
  mutate(nconst_8= lag(nconst, 8)) %>%
  mutate(nconst_9= lag(nconst, 9)) %>% 
  mutate(nconst_1 = ifelse(is.na(nconst_1), "", nconst_1),
         nconst_2 = ifelse(is.na(nconst_2), "", nconst_2),
         nconst_3 = ifelse(is.na(nconst_3), "", nconst_3),
         nconst_4 = ifelse(is.na(nconst_4), "", nconst_4),
         nconst_5 = ifelse(is.na(nconst_5), "", nconst_5),
         nconst_6 = ifelse(is.na(nconst_6), "", nconst_6),
         nconst_7 = ifelse(is.na(nconst_7), "", nconst_7),
         nconst_8 = ifelse(is.na(nconst_8), "", nconst_8),
         nconst_9 = ifelse(is.na(nconst_9), "", nconst_9)) %>% 
  unite(col = "crews",  c(nconst, nconst_1:nconst_9), sep = " ") 

movie_crew<- movie_crew %>% select(-averageRating)  
write.csv(movie_crew, "movie_good_or_bad.csv", row.names = F)
