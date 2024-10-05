from setuptools import setup, find_packages

with open("README.md", "r") as f:
    page_description = f.read()

with open("requirements.txt") as f:
    requirements = f.read().splitlines()
setup(
    name="package_image",
    version="0.0.1",
    author="Maciel",
    author_email="oliveira_soares_330_@_gmail_.com",
    description="image processing package using skimage",
    long_description=page_description,
    long_description_content_type="text/markdown",
    url="https://github.com/soares1972/processamento-de-imagem.git"
    packages=find_packages(),
    install_requires=requirements,
    python_requires='>=3.12',
)