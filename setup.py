import os
import setuptools
with open ("README.md", "r", encoding= "utf-8") as f:
    long_description = f.read()
    
__version__= "0.0.0"     

REPO_NAME = "Text-Summarizer"
AUTHOR_USER_NAME ="AditiSatsangi"
SRC_REPO = "textSummarizer"
AUTHOR_EMAIL = "aditisatsangi@gmail.com"

setuptools.setup(
    name= SRC_REPO,
    version = __version__,
    author= AUTHOR_USER_NAME,
    author_email= AUTHOR_EMAIL,
    description="A small python paackaaeg for NLP app",
    long_descrption= "text/markdown",
    url= f"https://github.com/AditiSatsangi/Text-Summarizer/issues",
    project_urls={
        "Bug Tracker": f"https://github.com/AditiSatsangi/Text-Summarizer/issues",
        },
    package_dir= {"": "src"},
    packages= setuptools.find_packages(where= "src")
    
    
)