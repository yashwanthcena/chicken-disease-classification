import setuptools

with open("README.md","r",encoding="utf-8") as f:
    long_description =f.read()


__version__ ="0.0.0"

REPO_NAME= "chicken-disease-classification"
AUTHOR_USER_NAME = "yashwanthcena"
SRC_REPO ="CnnClassifier"
AUTHOR_EMAIL ="yashwanthmadugula25@gmail.com"

setuptools.setup(
    name=SRC_REPO,
    version=__version__,
    author=AUTHOR_USER_NAME,
    author_email=AUTHOR_EMAIL,
    description="A small Python Package for CNN app",
    long_description=long_description,
    #long_description_content= "text/markdown",
    url=f"https://github.com/{AUTHOR_USER_NAME}/{REPO_NAME}",
    package_dir={"":"src"},
    packages=setuptools.find_packages(where="src")
)
