rm(list = ls())
setwd("Your directory")
library(tidyverse)
library(datasauRus)
library(lubridate)

#"cable_vendor_data_with_timestamp.csv" %>% 
  read_csv() %>% View()

"cable_vendor_data_with_timestamp.csv" %>% 
  read_csv() %>% 
  pull(vendor) %>% 
  unique() 

# Plot a histogram
"cable_vendor_data_with_timestamp.csv" %>% 
  read_csv() %>%
  ggplot(aes(x = cable_length_in_cms,
             fill = vendor)) +
  geom_histogram(binwidth = 0.1) + 
  geom_vline(xintercept = 10,
             color = "red",
             linetype = 2)

"cable_vendor_data_with_timestamp.csv" %>% 
  read_csv() %>%
  mutate(year = ts %>% year()) %>%
  mutate(month = ts %>% month()) %>% 
  mutate(day = ts %>% day()) %>% 
  mutate(hour = ts %>% hour()) %>% 
  mutate(minute = ts %>% minute()) %>% 
  mutate(second = ts %>% second()) %>% 
  mutate(day_of_week_num = ts %>% wday()) %>% 
  mutate(day_of_week = ts %>% wday(label = TRUE)) %>% 
 # filter(hour != 3) %>% 
  ggplot(aes(x = cable_length_in_cms,
             fill = vendor)) +
  geom_histogram(binwidth = 0.1) + 
  geom_vline(xintercept = 10,
             color = "red",
             linetype = 2) + 
  facet_wrap( ~ hour, nrow = 6, ncol = 4)
