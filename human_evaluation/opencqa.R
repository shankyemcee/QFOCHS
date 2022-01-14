####################################################
data_1 <- read.csv("./results/run2/new1-0-99.csv")
data_2 <- read.csv("./results/run2/new2-0-99.csv")
data_3 <- read.csv("./results/run2/new3-0-99.csv")

combine_vector <- function(a, b, c) {
  result <- c()
  for (x in a) {
    result = c(result, x)
  }
  for (x in b) {
    result = c(result, x)
  }
  for (x in c) {
    result = c(result, x)
  }
  result
}

factual_1 <- combine_vector(c(data_1["factual1"]), c(data_1["factual2"]), c(data_1["factual3"]))
factual_2 <- combine_vector(c(data_2["factual1"]), c(data_2["factual2"]), c(data_2["factual3"]))
factual_3 <- combine_vector(c(data_3["factual1"]), c(data_3["factual2"]), c(data_3["factual3"]))
re_1 <- combine_vector(c(data_1["relevant1"]), c(data_1["relevant2"]), c(data_1["relevant3"]))
re_2 <- combine_vector(c(data_2["relevant1"]), c(data_2["relevant2"]), c(data_2["relevant3"]))
re_3 <- combine_vector(c(data_3["relevant1"]), c(data_3["relevant2"]), c(data_3["relevant3"]))
fl_1 <- combine_vector(c(data_1["fluent1"]), c(data_1["fluent2"]), c(data_1["fluent3"]))
fl_2 <- combine_vector(c(data_2["fluent1"]), c(data_2["fluent2"]), c(data_2["fluent3"]))
fl_3 <- combine_vector(c(data_3["fluent1"]), c(data_3["fluent2"]), c(data_3["fluent3"]))


factual <- combine_vector(factual_1, factual_2, factual_3)
re <- combine_vector(re_1, re_2, re_3)
fl <- combine_vector(fl_1, fl_2, fl_3)

types <- rep(c("A", "B", "C"), rep(300, 3))

kruskal.test(factual, types)
kruskal.test(re, types)
kruskal.test(fl, types)




