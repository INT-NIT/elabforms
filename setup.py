from setuptools import setup, find_packages
import os

with open(os.path.join(os.path.dirname(__file__), "VERSION")) as version_file:
    version = version_file.read().strip()

with open('requirements.txt') as f:
    requires = f.read().splitlines()

with open('README.md') as f:
    long_description = f.read()

setup(
    name="elabforms",
    version=version,
    packages=find_packages(where="elabforms"),
    #package_dir={"": "."},
    package_data={
        "": ["*.json", "*.csv", "*.zip"],
    },
    data_files=[('elabforms', ['VERSION', 'README.md', 'requirements.txt'])],
    author=" Fatai Idrissou, Sylvain Takerkart",
    description="A set of tools to create and manage standardized forms for eLabFTW",
    long_description_content_type="text/markdown",
    long_description=long_description,
    license='MIT',
    install_requires=requires,
    include_package_data=True,
    python_requires='>=3.8',
    extras_require={
        'test': ['pytest', 'flake8'],  # Added flake8 for code style checking
    },
    entry_points={
        "console_scripts": [
            "eform=elabforms.cli:main"
        ],
    },
)
