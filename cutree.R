setwd("/Users/diana/Github/GeneClustering")
library(WGCNA)
library(sqldf)

options(stringsAsFactors=F)

dat0=read.table("genes.csv",header=TRUE,sep=",",quote="",dec=".",row.names=1,colClasses=c("id"="character"))
dat0<-subset(dat0,dat0$std > 0.7)

datExpr=t(dat0)
class(datExpr)<-"numeric"

ADJ = adjacency(datExpr,power=6)

dissTOM=TOMdist(ADJ)
# build tree
hc <- hclust(as.dist(dissTOM),method="average")

# static cut tree
# Memb <- cutree(hc, k=10)

# dynamic cut tree
dt = cutreeDynamic(hc,distM=dissTOM, deepSplit=4)
df<-data.frame(
  Gene=c(row.names(dat0)),
  Cluster=c(dt)
)
write.table(df,file="clusters.csv",sep=",",row.names=FALSE)
