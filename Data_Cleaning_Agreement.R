library(ggplot2)
library(cowplot)
library(tidyverse)
library(stringr)
library(vcd)
library(asbio)

grid_data <- read.csv("E:/Grassland Mapping Files/to sort/FINAL_PIXEL_DATAFILE.csv")

grid_data <- grid_data[,1:8]
head(grid_data)

ggplot(grid_data, aes(Expert)) +
  geom_bar()

ggplot(grid_data, aes(ESA)) +
  geom_bar()

ggplot(grid_data, aes(Esri)) +
  geom_bar()

ggplot(grid_data, aes(DW)) +
  geom_bar()


############## Only use points that Experts classified as Grassland
unique(grid_data$Expert)
OnlyExpertGL <- subset(grid_data, Expert %in% c("1","2","3","4","5","6","7"))

plot_esa <- ggplot(OnlyExpertGL, aes(ESA)) +
  geom_bar()
plot_esa

plot_esri <- ggplot(OnlyExpertGL, aes(Esri)) +
  geom_bar()
plot_esri

plot_dw <- ggplot(OnlyExpertGL, aes(DW)) +
  geom_bar()
plot_dw

plot_grid(plot_esa,plot_esri,plot_dw)


head(OnlyExpertGL)

############################################################################
# Clean up
unique(grid_data$Expert)

grid_data_clean <-  grid_data
grid_data_clean[grid_data_clean == 'a'] <- "A"
grid_data_clean[grid_data_clean == 'f'] <- "F"
grid_data_clean[grid_data_clean == 'c'] <- "C"
grid_data_clean[grid_data_clean == 'a'] <- "A"
grid_data_clean[grid_data_clean == 'Q'] <- "O"
grid_data_clean[grid_data_clean == 's'] <- "S"
grid_data_clean[grid_data_clean == 'u'] <- "U"
grid_data_clean[grid_data_clean == 'wt'] <- "WT"
grid_data_clean[grid_data_clean == 'Wt'] <- "WT"
grid_data_clean[grid_data_clean == 'w'] <- "W"
grid_data_clean[grid_data_clean == 'b'] <- "B"
grid_data_clean[grid_data_clean == 'W\tF'] <- "WT"
grid_data_clean[grid_data_clean == 'W\tT'] <- "WT"
grid_data_clean[grid_data_clean == 'W\tT'] <- "WT"
grid_data_clean[grid_data_clean == 'O\t1'] <- "O"
grid_data_clean[grid_data_clean == 'O\t2'] <- "O"
grid_data_clean[grid_data_clean == 'o'] <- "O"
grid_data_clean[grid_data_clean == 'D'] <- "U"
grid_data_clean[grid_data_clean == ' \tw'] <- "W"

write.csv(grid_data_clean, "E:/Grassland Mapping Files/R outputs/FINAL_PIXEL_DATAFILE_CLEAN.csv", row.names = FALSE)

grid_data_clean <- read.csv("E:/Grassland Mapping Files/R outputs/FINAL_PIXEL_DATAFILE_CLEAN.csv")

unique(grid_data_clean$Expert)
table(grid_data_clean$Expert)
table(grid_data$ESA)
table(grid_data$Esri)
table(grid_data$DW)
plot_grid_data_clean <- ggplot(grid_data_clean, aes(Expert)) +
  geom_bar()
plot_grid_data_clean

ESAsub <- subset(grid_data_clean, ESA %in% c("30"))

plotESAsub <- ggplot(ESAsub, aes(Expert))+
  geom_bar()
plotESAsub

table(ESAsub$Expert)


###################################################################################
#Check if all grids are here/for any overlap etc.
siteValues <- table(grid_data$Location_Name)
siteValues

siteValues <- as.data.frame(siteValues)
siteValues

#write.csv(siteValues, "E:/Grassland Mapping Files/R outputs/MismatchTest.csv", row.names = FALSE)

nonSingleSites <- subset(siteValues, Freq > 100)
nonSingleSites

###################################################################################
#Calculate the grassland agreement for each grid
###################################################################################

simplified <- as.data.frame(grid_data_clean)
simplified
simplified$Expert[simplified$Expert == '1'] <- "30"
simplified$Expert[simplified$Expert == '2'] <- "30"
simplified$Expert[simplified$Expert == '3'] <- "30"
simplified$Expert[simplified$Expert == '4'] <- "30"
simplified$Expert[simplified$Expert == '5'] <- "30"
simplified$Expert[simplified$Expert == '6'] <- "30"
simplified$Expert[simplified$Expert == '7'] <- "30"

#ESA is already at a value of 30

simplified$Esri[simplified$Esri == '3'] <- "30"

simplified$DW[simplified$DW == '2']<-"30"

table(simplified$Expert)

ggplot(simplified, aes(Expert)) +
  geom_bar()

ggplot(simplified, aes(ESA)) +
  geom_bar()

ggplot(simplified, aes(Esri)) +
  geom_bar()

ggplot(simplified, aes(DW)) +
  geom_bar()

table(simplified$Expert)
table(simplified$ESA)
table(simplified$Esri)
table(simplified$DW)

#confusion matrix values for ESA dataset
simplified$ESAEQ <- simplified$Expert=="30" & simplified$ESA=="30"
simplified$ESRIEQ <- simplified$Expert=="30" & simplified$Esri=="30"
simplified$DWEQ <- simplified$Expert=="30" & simplified$DW=="30"
simplified$TWOEQ <- simplified$ESAEQ == "TRUE" & simplified$ESRIEQ == "TRUE" | simplified$ESAEQ == "TRUE" & simplified$DWEQ == "TRUE" | simplified$ESRIEQ == "TRUE" & simplified$DWEQ == "TRUE"
simplified$ALLEQ <- simplified$ESAEQ == "TRUE" & simplified$ESRIEQ == "TRUE" & simplified$DWEQ =="TRUE"

simplified
table(simplified$ESAEQ)
table(simplified$ESRIEQ)
table(simplified$DWEQ)
table(simplified$TWOEQ)
table(simplified$ALLEQ)

superSimple <- as.data.frame(simplified)

superSimple$Expert[superSimple$Expert != "30"] <- "100"
superSimple$ESA[superSimple$ESA != "30"] <- "100"
superSimple$Esri[superSimple$Esri != "30"] <- "100"
superSimple$DW[superSimple$DW != "30"] <- "100"

ESA_Kappa <- Kappa(superSimple$Expert, superSimple$ESA)
ESRI_Kappa <-Kappa(superSimple$Expert, superSimple$Esri)
DW_Kappa <- Kappa(superSimple$Expert, superSimple$DW)
ESA_Kappa
ESRI_Kappa
DW_Kappa
Kappa
##################################################################################
#Visualize the geographical data
##################################################################################

theme_set(
  theme_minimal() +
    theme(legend.position = "right")
)

locations <- read.csv("E:/Grassland Mapping Files/to sort/Grids_Updated.csv") #only the provided sites

all_locations <- read.csv("E:/Grassland Mapping Files/to sort/SitePointInfoUpdated.csv")
all_locations

plotted <- ggplot(locations, aes(y=Latitude, x=Longitude)) +
      geom_point()
plotted
submitted <- subset(locations, Site.submitted %in% c("TRUE"))
submitted
test2 <- ggplot(submitted, aes(y=Latitude, x=Longitude)) +
  geom_point()
test2

countryTot <- table(submitted$Country)
countryTot <- as.data.frame(countryTot)
countryTot

##################################################################################
#sort through the data by individual site
##################################################################################
superSimple
names(superSimple) <- c("AlpID","Expert","ESA","Esri","DW","Site_name","Name1","Name","ESAEQ","ESRIEQ","DWEQ","TWOEQ","ALLEQ")
grouped_data_site <- superSimple %>% group_by(Site_name)
grouped_data_site
per_site <- group_split(grouped_data_site)
per_site[[1]]

names(nonSingleSites) <- c("Name", "Num")
nonSingleSites

#per_site_Over100 <- merge(per_site, nonSingleSites, by= intersect(names(per_site), names(nonSingleSites$Name)))
#per_site_Over100

##################################################################################
#Calculations for each site
##################################################################################
i = 0
test <- list()
test2 <- list()
test3 <- list()
agreementESA <- list()
agreementEsri <- list()
agreementDW <- list()
Names <- list()
kappaListESA <- list()
kappaListEsri <- list()
kappaListDW <- list()

for (group in 1:3873){
  print(group)
  test[[group]] <- (Kappa(per_site[[group]][["Expert"]], per_site[[group]][["ESA"]]))
}
for (group in 1:3873){
  print(group)
  test2[[group]] <- (Kappa(per_site[[group]][["Expert"]], per_site[[group]][["Esri"]]))
}
for (group in 1:3873){
  print(group)
  test3[[group]] <- (Kappa(per_site[[group]][["Expert"]], per_site[[group]][["DW"]]))
}
for (group in 1:3873){
  agreementESA[[group]] <- test[[group]][["ttl_agreement"]]
}
for (group in 1:3873){
  kappaListESA[[group]] <- unique(test[[group]][["khat"]])
}
for (group in 1:3873){
  agreementEsri[[group]] <- test2[[group]][["ttl_agreement"]]
}
for (group in 1:3873){
  kappaListEsri[[group]] <- unique(test2[[group]][["khat"]])
}
for (group in 1:3873){
  agreementDW[[group]] <- test3[[group]][["ttl_agreement"]]
}
for (group in 1:3873){
  kappaListDW[[group]] <- unique(test3[[group]][["khat"]])
}
for (group in 1:3873){
  Names[[group]] <- unique(per_site[[group]][["Site_name"]])
}

nameTotAgree <- data.frame(unlist(Names),unlist(agreementESA), unlist(agreementEsri),unlist(agreementDW), unlist(kappaListESA),unlist(kappaListEsri),unlist(kappaListDW))
names(nameTotAgree) <- c("Name", "ESAagree","ESRIagree","DWagree","ESAkappa","ESRIkappa","DWkappa")
nameTotAgree

overall <- merge(all_locations, nameTotAgree, by= "Name")

overall

write.csv(overall, "E:/Grassland Mapping Files/R outputs/Testing.csv", row.names = FALSE)

Names <- as.data.frame(Names)
Names

write.csv(nameTotAgree, "E:/Grassland Mapping Files/R outputs/NametestingFinal.csv", row.names = FALSE)

write.csv(all_locations, "E:/Grassland Mapping Files/R outputs/Nametesting2Final.csv", row.names = FALSE)

##################################################################################
#For each location
##################################################################################
superSimple
grouped_data_location <- superSimple %>% group_by(Name)
grouped_data_location
per_location <- group_split(grouped_data_location)

#Create dataset with agreement/kappa for each location (averge the grid values by name)
LocTest <- list()
LocNames <- list()
LocAgreementESA <- list()
LocKappaListESA <- list()
LocAgreementESRI <- list()
LocKappaListESRI <- list()
LocAgreementDW <- list()
LocKappaListDW <- list()


for (group in 1:528){
  LocTest[[group]] <- (Kappa(per_location[[group]][["Expert"]], per_location[[group]][["ESA"]]))
}
for (group in 1:528){
  LocNames[[group]] <- unique(per_location[[group]][["Name"]])
}
for (group in 1:528){
  LocAgreementESA[[group]] <- LocTest[[group]][["ttl_agreement"]]
  #i need to fix NAN -> 100 in this list
}
for (group in 1:528){
  LocKappaListESA[[group]] <- unique(LocTest[[group]][["khat"]])
}
for (group in 1:528){
  LocTest[[group]] <- (Kappa(per_location[[group]][["Expert"]], per_location[[group]][["Esri"]]))
}
for (group in 1:528){
  LocAgreementESRI[[group]] <- LocTest[[group]][["ttl_agreement"]]
  #i need to fix NAN -> 100 in this list
}
for (group in 1:528){
  LocKappaListESRI[[group]] <- unique(LocTest[[group]][["khat"]])
}
for (group in 1:528){
  LocTest[[group]] <- (Kappa(per_location[[group]][["Expert"]], per_location[[group]][["DW"]]))
}
for (group in 1:528){
  LocAgreementDW[[group]] <- LocTest[[group]][["ttl_agreement"]]
  #i need to fix NAN -> 100 in this list
}
for (group in 1:528){
  LocKappaListDW[[group]] <- unique(LocTest[[group]][["khat"]])
}

LocTotAgree <- data.frame(unlist(LocNames),unlist(LocAgreementESA),unlist(LocAgreementESRI),unlist(LocAgreementDW),unlist(LocKappaListESA), unlist(LocKappaListESRI),unlist(LocKappaListDW))
names(LocTotAgree) <- c("Site.Name", "ESAagree","ESRIagree","DWagree","ESAkappa","ESRIkappa","DWkappa")

names(locations) <- c("Site.Name", "Lat", "Lon","Country","Site.Submitted","Processed","Grid.Num")

LocTotAgree
LocOverall <- merge(locations, LocTotAgree, by="Site.Name")

LocOverall
write.csv(LocOverall, "E:/Grassland Mapping Files/R outputs/LocationAccuracies.csv", row.names = FALSE)
