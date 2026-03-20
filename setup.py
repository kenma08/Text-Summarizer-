import setuptools

with open("README.md", "r", encoding="utf-8") as fh:
    long_description = fh.read()


__version__ = "0.0.0"

Repo_name= "Text-Summarizer-"
Author_user_name= "kennma08"
SRC_Repo= "textSummarizer"
Author_Email= "officialprakhargupta08@gmail.com"


setuptools.setup(
    name= SRC_Repo,
    version= __version__,
    author= Author_user_name,
    author_email= Author_Email,
    description= "A small package for text summarization",
    long_description= long_description,
    long_description_content_type= "text/markdown",
    url= f"https://github.com/{Author_user_name}/{Repo_name}",
    project_urls= {
        "Bug Tracker": f"https://github.com/{Author_user_name}/{Repo_name}/issues",
    },
    package_dir= {"": "src"},
    packages= setuptools.find_packages(where= "src"),
)  