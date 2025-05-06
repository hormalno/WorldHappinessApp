from setuptools import setup, find_packages

setup(
    name="world_happiness_app",
    version="0.1",
    packages=find_packages(where="src"),
    package_dir={"": "src"},
    install_requires=[
        "streamlit>=1.45.0",
        "pandas>=2.2.3",
        "numpy>=2.2.5",
        "matplotlib>=3.10.1",
        "seaborn>=0.13.2",
        "scipy>=1.15.2"
    ],
    entry_points={
        'console_scripts': [
            'world_happiness_app = world_happiness_app.main:main',
        ],
    },
    # Additional metadata
    author="Yasen Ivanov",
    author_email="yasen.ivanov@ipsos.com",
    description="A Streamlit app using pandas and matplotlib",
    url="https://https://github.com/hormalno/WorldHappinessApp",
)