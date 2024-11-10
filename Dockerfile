# FROM amazonlinux:2
FROM public.ecr.aws/lambda/python:3.10

# RUN yum install -y python3-pip python3-devel gcc libxslt-devel libxml2-devel
# RUN pip3 install lxml -t /opt/python/


# Copy function code
COPY src/ ${LAMBDA_TASK_ROOT}/src/
COPY packages/ ${LAMBDA_TASK_ROOT}/packages/
COPY nltk_data/ ${LAMBDA_TASK_ROOT}/nltk_data/
COPY AWS_lambda.py ${LAMBDA_TASK_ROOT}/

# Install dependencies
COPY requirements.txt ./
RUN pip install -r requirements.txt
RUN pip install lxml_html_clean

# ENTRYPOINT [ "/usr/local/bin/python", "-m", "AWS_lambda" ]

# Set the CMD to your handler (could be AWS_lambda.lambda_handler)
CMD ["AWS_lambda.lambda_handler"]
# CMD [echo, "Hello World from container"]

# CMD ["bash"]