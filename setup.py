import setuptools

import countersign

setuptools.setup(
    name="countersign",
    version=countersign.__version__,
    license='MIT',
    packages=setuptools.find_packages(exclude=('tests',)),
    author="Justin Sexton",
    author_email="justinsexton.dev@gmail.com",
    description="Lightweight API that helps consumers generate random passwords and phrases.",
    url="https://github.com/JSextonn/countersign.git",
    keywords=[
        'password',
        'password-generator',
        'library'
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ]
)
