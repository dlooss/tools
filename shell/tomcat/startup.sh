#!/bin/bash
source ./setenv.sh

runState=`ps -ef | grep ${TOMCAT_HOME} | grep -v grep | wc -l`
if [ "$runState" -ne "0" ]; then 
    sh ./shutdown.sh
fi

sh ${TOMCAT_HOME}/bin/startup.sh
while ((runState==0))
do
    sleep 10s
    runState=`ps -ef | grep ${TOMCAT_HOME} | grep -v grep | wc -l`    
done
