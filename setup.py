from setuptools import setup

def get_install_requires():
    return [
        "numpy",
        "tensorflow==2.3.0",
        "tensorflow-hub",

        ]

setup(
    name='accurate_detector',
    version='1.0',
    install_requires=get_install_requires(),
    packages=['accurate_detector'],
)
