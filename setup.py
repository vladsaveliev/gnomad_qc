import setuptools


install_requires = []
with open("requirements.txt", "r") as requirements_file:
    for req in (line.strip() for line in requirements_file):
        if req != "hail":
            install_requires.append(req)


setuptools.setup(
    name="gnomad_qc",
    version="0.1.0",
    # packages=setuptools.find_namespace_packages(include=["gnomad.*"]),
    classifiers=[
        "Topic :: Scientific/Engineering :: Bio-Informatics",
        "Intended Audience :: Science/Research",
        "License :: OSI Approved :: MIT License",
        "Programming Language :: Python :: 3",
        "Development Status :: 4 - Beta",
    ],
    python_requires=">=3.6",
    scripts=[
        'gnomad_qc/v2/load_data/import_vcf.py',
    ]
)
