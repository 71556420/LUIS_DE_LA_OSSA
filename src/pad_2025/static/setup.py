from setuptools import setup, find_packages

setup(
    name="pad_2025",
    version="0.0.1",
    author="LUIS DE LA OSSA",
    author_email="fernando.delaossa@est.iudigital.edu.co",
    description="Actividad 1 - Análisis de Datos en Python",
    packages=find_packages(),
    install_requires=[
        "requests",
        "pandas",
        "matplotlib"
    ]
)
