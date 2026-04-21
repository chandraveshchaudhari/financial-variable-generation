from pathlib import Path

from setuptools import find_packages, setup


BASE_DIR = Path(__file__).parent.resolve()
README_PATH = BASE_DIR / "README.md"


setup(
    name="financial-variable-generation",
    version="0.1.0",
    description="Generate financial ratios and derived fundamental indicators from statement data.",
    long_description=README_PATH.read_text(encoding="utf-8"),
    long_description_content_type="text/markdown",
    url="https://github.com/chandraveshchaudhari/financial-variable-generation",
    author="Chandravesh Chaudhari",
    author_email="chandraveshchaudhari@gmail.com",
    license="MIT",
    project_urls={
        "Source": "https://github.com/chandraveshchaudhari/financial-variable-generation",
        "Issues": "https://github.com/chandraveshchaudhari/financial-variable-generation/issues",
    },
    classifiers=[
        "Development Status :: 4 - Beta",
        "Intended Audience :: Developers",
        "Intended Audience :: Financial and Insurance Industry",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
        "Programming Language :: Python :: 3",
        "Programming Language :: Python :: 3 :: Only",
        "Programming Language :: Python :: 3.9",
        "Programming Language :: Python :: 3.10",
        "Programming Language :: Python :: 3.11",
        "Programming Language :: Python :: 3.12",
        "Topic :: Office/Business :: Financial",
        "Topic :: Scientific/Engineering :: Information Analysis",
    ],
    keywords="finance, fundamental-analysis, financial-ratios, accounting, python",
    package_dir={"": "src"},
    packages=find_packages(where="src"),
    python_requires=">=3.9",
    include_package_data=True,
)

