# Copyright Amazon.com, Inc. or its affiliates. All Rights Reserved. SPDX-License-Identifier: MIT-0

import setuptools


with open("README.md") as fp:
    long_description = fp.read()


setuptools.setup(
    name="graviton",
    version="0.0.1",

    description="An empty CDK Python app",
    long_description=long_description,
    long_description_content_type="text/markdown",

    author="author",

    package_dir={"": "graviton2"},
    packages=setuptools.find_packages(where="graviton2"),

    install_requires=[
        "aws-cdk.core==2.500.0",
        "aws-cdk.aws-eks==2.500.0",
        "aws-cdk.aws-ec2==2.500.0",
        "aws-cdk.aws-cloudtrail==2.500.0",
        "aws-cdk.aws-codebuild==2.500.0",
        "aws-cdk.aws-codecommit==2.500.0",
        "aws-cdk.aws-codepipeline==2.500.0",
        "aws-cdk.aws-codepipeline-actions==2.500.0",
        "aws-cdk.aws-ec2==2.500.0",
        "aws-cdk.aws-ecr==1.160.0",
        "aws-cdk.aws-ecs==1.160.0",
        "aws-cdk.aws-eks==1.160.0",
        "aws-cdk.aws-elasticloadbalancingv2==2.500.0",
        "aws-cdk.aws-elasticsearch==2.500.0",
        "aws-cdk.aws-emr==2.500.0",
        "aws-cdk.aws-events==2.500.0",
        "aws-cdk.aws-events-targets==2.500.0",
        "aws-cdk.aws-iam==2.500.0",
        "aws-cdk.aws-lambda==2.500.0",
        "aws-cdk.aws-lambda-python==2.500.0",
        "aws-cdk.aws-rds==2.500.0",
        "aws-cdk.aws-ssm==2.500.0",
        "boto3",
        "awscli",

        # Packages specifically required for the Elasticsearch module
        "elasticsearch",
        "requests",
        "requests-aws4auth",
        "Faker",
    ],

    python_requires=">=3.6",

    classifiers=[
        "Development Status :: 4 - Beta",

        "Intended Audience :: Developers",

        "License :: OSI Approved :: Apache Software License",

        "Programming Language :: JavaScript",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.6",
        "Programming Language :: Python :: 3.7",
        "Programming Language :: Python :: 3.8",

        "Topic :: Software Development :: Code Generators",
        "Topic :: Utilities",

        "Typing :: Typed",
    ],
)
