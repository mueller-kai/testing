#!/usr/bin/env python3
# a static example DAG with one task to start DoL Launcher on Azure K8s cluster

import json
import os

import airflow
from airflow.contrib.operators.kubernetes_pod_operator import KubernetesPodOperator
import airflow.utils.dates
from kubernetes import client

#for Debugresaons only
from airflow.operators.bash import BashOperator

with airflow.DAG(
    dag_id='testdag',
    start_date=airflow.utils.dates.days_ago(2),
    description="Run compute jobs with normal priority",
    schedule_interval=None,
) as dag:
    
    debug_task = BashOperator(
    task_id = 'Debug_task',
    bash_command = "echo 'first task debug task has been run'"
    )
