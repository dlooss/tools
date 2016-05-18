#!/bin/bash
source ./env.sh

runState=`ps -ef | grep ${TOMCAT_HOME} | grep -v grep | wc -l`

if [ "$runState" -ne "0" ]; then
    sh ${TOMCAT_HOME}/bin/shutdown.sh
fi

i=0
while ((runState!=0))
do
    sleep 10s
    ((i++))
    if [ "$i" -gt "18" ]; then
   		kill -9 `ps -ef | grep ${TOMCAT_HOME} | grep -v grep | awk '{print $2}'`
   		sleep 5s
    fi
    runState=`ps -ef | grep ${TOMCAT_HOME} | grep -v grep | wc -l`
done
