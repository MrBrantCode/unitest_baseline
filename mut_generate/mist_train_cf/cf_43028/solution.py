"""
QUESTION:
Create a function named `create_emr_cluster_script` that takes six parameters: `VIRTUAL_CLUSTER_ID`, `JOB_NAME`, `EMR_ROLE_ARN`, `S3_BUCKET`, `EMR_RELEASE_LABEL`, and `EMR_MASTER_DNS_NAME`. The function should return a string representing the EMR cluster deployment script. The script should include the provided input parameters and the corresponding EMR cluster configuration, including job driver configuration and monitoring configuration overrides.
"""

def create_emr_cluster_script(VIRTUAL_CLUSTER_ID, JOB_NAME, EMR_ROLE_ARN, S3_BUCKET, EMR_RELEASE_LABEL, EMR_MASTER_DNS_NAME):
    script = f"--virtual-cluster-id {VIRTUAL_CLUSTER_ID} \\\n"
    script += f"--name {JOB_NAME} \\\n"
    script += f"--execution-role-arn {EMR_ROLE_ARN} \\\n"
    script += f"--release-label {EMR_RELEASE_LABEL} \\\n"
    script += '--job-driver \'{"sparkSubmitJobDriver": {' \
              f'"entryPoint": "s3://{S3_BUCKET}/app_code/job/hivethrift_emr.py",' \
              f'"entryPointArguments":["s3://{S3_BUCKET}","{EMR_MASTER_DNS_NAME}"],' \
              '"sparkSubmitParameters": "--conf spark.driver.cores=1 --conf spark.executor.memory=4G --conf spark.driver.memory=1G --conf spark.executor.cores=2"}}\' \\\n'
    script += '--configuration-overrides \'{"monitoringConfiguration": {' \
              f'"s3MonitoringConfiguration": {{"logUri": "s3://{S3_BUCKET}/elasticmapreduce/emr-containers"}}}}\''
    return script