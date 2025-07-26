from setuptools import setup, find_packages

with open("requirements.txt") as f:
    requirements = f.read().splitlines()

setup (
    name="MLOPS-HotelReservation",
    version="0.1",
    author="Sanket Maheshwari",
    packages=find_packages(),
    install_requires=requirements,
    description="A project for MLOps in hotel reservation systems",
)


