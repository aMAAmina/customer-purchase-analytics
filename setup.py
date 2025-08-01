from setuptools import setup, find_packages

setup(
    name="pokemon_pipeline",
    version="0.1",
    description="A pipeline for preprocessing customer purchase data.",
    author="Amina Bouhamra",
    packages=find_packages(), 
    install_requires=[
        "pandas>=2.3.1,<2.4"
    ],
    entry_points={
        "console_scripts": [
            "customer_analytics=customer_analytics.cli:main",  
        ],
    },
)