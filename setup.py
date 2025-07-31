from setuptools import setup, find_packages

setup(
    name="arxiv_rag",
    version="0.1",
    packages=find_packages(),
    package_dir={'': '.'},
    install_requires=[
        'arxiv',
        'PyPDF2',
        'sentence-transformers',
        'faiss-cpu',
        'transformers',
        'torch',
        'langchain'
    ],
)