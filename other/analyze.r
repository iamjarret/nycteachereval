#analyze.r
#
#This code first extracts the data from the SQL table
#assumes the table is organized using SQLite
#
#Next the code prints plots scatter plots of value add scores
#against each of the demographic variables plus additional
#interaction variables.
#

library("DBI")
library("RSQLite")
drv <- dbDriver("SQLite")
db <- dbConnect(drv, "Teacher")
print(dbListTables(db))
#I learned that this natural join is not doing what I thought it was doing...
SQLcmd <-"select dbn, name, first_name, last_name, va_0910_eng, va_0910_math, va_0809_eng, va_0809_math, va_0708_eng, va_0708_math, va_0607_eng, va_0607_math,freelunch, sped, ell, asian, black, hisp, white, male, female from teachers_teachers join teachers_school on teachers_teachers.dbn_id = teachers_school.dbn"
data<-dbGetQuery(db,SQLcmd)

#plots all scatter plots
plot(data[5:21])

#there are value add scores that are over 100!


#The free lunch vs. va_0910_eng relationship seems to be interesting
plot(lm(va_0910_eng~freelunch, data=data))

#1017, 813, and 623 are huge positive outliers

#############################################################################
#
#	(2) Test if obvious relationships exist between va and demographic data
#
#############################################################################

 
m0910 <- lm(va_0910_math ~ black + hisp + ell + freelunch + female, data=data)
#result, cannot reject hypothesis that all coefficients are not significantly
#different than zero
m0809 <- lm(va_0809_math ~ black + hisp + ell + freelunch + female, data=data)


m0708 <- lm(va_0708_math ~ black + hisp + ell + freelunch + female, data=data)
m0607 <- lm(va_0607_math ~ black + hisp + ell + freelunch + female, data=data)



e0910 <- lm(va_0910_eng ~ black + hisp + ell + freelunch + female, data=data)
#result, reject the hypothesis that all coefficients are not significantly
#different than zero
summary(e0910)
#HISP variable is very signficant
e0910_hisp <- lm(va_0910_eng ~ hisp, data=data)
#distribution is nonnormal but in a good way




