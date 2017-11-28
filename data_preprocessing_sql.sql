Precipitation - PRCP
Air Temperature - TMAX
Wind - AWND

/* To create fire_selected table from existing table which has selected features for year 2006 to 2015 */
CREATE TABLE fires_selected_10 AS SELECT OBJECTID,FIRE_YEAR,strftime('%m/%d/%Y', DISCOVERY_DATE) as DISCOVERY_DATE,STAT_CAUSE_DESCR,strftime('%m/%d/%Y', CONT_DATE) as CONT_DATE,FIRE_SIZE,round(LATITUDE,1) as LATITUDE,round(LONGITUDE,1) as LONGITUDE,STATE,COUNTY FROM fires where FIRE_YEAR IN ('2006','2007','2008','2009','2010','2011','2012','2014','2015')

select count(*) from fires_selected_10  --output 758734

/*Import weather data excel files. We have already formatted date in excel to custom format of mm/dd/yyyy */

/* Creating weather table from one of the tables created from excel */
CREATE TABLE weather AS
SELECT * FROM Data_2010_1orig

select count(*) from weather

/* To combine insert data of all the tables into one table */
INSERT into weather select * from Data_2009_1
INSERT into weather select * from Data_2009_2
INSERT into weather select * from Data_2009_3

select count(*) from weather

/* Duplicate data into another table for pre-processing. This table will contains non-null values for AWND, PRCP, TMAX */
CREATE TABLE weatherNN10 AS
SELECT * FROM weather

/*Analyzing which column has more null values */
Select count(*)from weatherNN10 where AWND != "" and PRCP != "" and TMAX != ""

/* To remove records from table where column value is null for AWND, PRCP, TMAX
Data having null values = 3477314
Rows in database after removal of null values = 287337 
*/

DELETE from weatherNN10 where  AWND == "" or PRCP == "" or TMAX == ""
select count(*) from weatherNN10 -- 287337

/*Created combined table with Latitude rounded to 1 */
CREATE TABLE combined10yr_R1 AS SELECT 
w.STATION, round(w.LATITUDE,1) as LATITUDE,round(w.LONGITUDE,1) as LONGITUDE, w.ELEVATION, w.DATE, w. AWND, w.PRCP, w.TMAX, 
OBJECTID,FIRE_YEAR, STAT_CAUSE_DESCR, CONT_DATE,FIRE_SIZE, STATE,COUNTY,
CASE WHEN  OBJECTID IS NULL THEN 'N' ELSE 'Y' END Fire
FROM weatherNN10 w LEFT JOIN fires_selected_10 f on f.LATITUDE=round(w.LATITUDE,1) and f.LONGITUDE=round(w.LONGITUDE,1) and f.DISCOVERY_DATE=w.DATE

select count(*) from combined10yr_R1
--output 287523
select count(*) from combined10yr_R1 where Fire == 'Y'
--output 2820

/*Created combined table with LAtitude rounded to 2 */
CREATE TABLE combined10yr_R2 AS SELECT 
w.STATION, round(w.LATITUDE,0) as LATITUDE,round(w.LONGITUDE,0) as LONGITUDE, w.ELEVATION, w.DATE, w. AWND, w.PRCP, w.TMAX, 
OBJECTID,FIRE_YEAR, STAT_CAUSE_DESCR, CONT_DATE,FIRE_SIZE, STATE,COUNTY,
CASE WHEN  OBJECTID IS NULL THEN 'N' ELSE 'Y' END Fire
FROM weatherNN10 w LEFT JOIN fires_selected_10 f on round(f.LATITUDE,0)=round(w.LATITUDE,0) and round(f.LONGITUDE,0)=round(w.LONGITUDE,0) and f.DISCOVERY_DATE=w.DATE

select count(*) from combined10yr_R2
--output 287337
select count(*) from combined10yr_R2 where Fire == 'Y'
--output 10

drop table combined10yr_R2

/* final tables to be used is combined10yr_R1 
weatherNN10
fires_selected_10 */
CREATE TABLE Analysis_All3 AS
SELECT LATITUDE, LONGITUDE, ELEVATION, AWND, PRCP, TMAX, Fire FROM combined10yr_R1

/* query to select test case for evaluating algorithm */
select * from Analysis_All3 where fire == "Y" and latitude != 40.5 and longitude != -122.3 and prcp != "0" and awnd != "0" order by prcp

/* Creating table containing all null values for resting*/
CREATE TABLE combined10yr_null AS SELECT 
round(w.LATITUDE,1) as LATITUDE,round(w.LONGITUDE,1) as LONGITUDE, w.ELEVATION, w.DATE, w. AWND, w.PRCP, w.TMAX, 
CASE WHEN  OBJECTID IS NULL THEN 'N' ELSE 'Y' END Fire
FROM weather w LEFT JOIN fires_selected_10 f on f.LATITUDE=round(w.LATITUDE,1) and f.LONGITUDE=round(w.LONGITUDE,1) and f.DISCOVERY_DATE=w.DATE

select count(*) from combined10yr_null
--output 3479612
select count(*) from combined10yr_null where Fire == 'Y'
--output 30388
select count(*) from combined10yr_null where Fire == 'Y' and AWND != "" and PRCP != "" and TMAX != ""
