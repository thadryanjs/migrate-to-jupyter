library(tidyverse)

print("Hello")

mtcars %>%
    ggplot(., aes(mpg, disp)) +
           geom_point()

mtcars %>%
    ggplot(., aes(mpg, disp)) +
        geom_line()
