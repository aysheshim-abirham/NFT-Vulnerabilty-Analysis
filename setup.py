import setuptools

with open("README.md", "r") as fh:
    long_description = fh.read()

setuptools.setup(
    name="nft_ownership_detector",
    version="0.0.1",
    author="Krishna Kushal",
    author_email="krishnackushal@gmail.com",
    description="NFT Onwership Detectot",
    long_description=long_description,
    long_description_content_type="text/markdown",
    packages=[
        "nft_ownership_detector"
    ],
    classifiers=[
        "Programming Language :: Python :: 3",
        "License :: OSI Approved :: MIT License",
        "Operating System :: OS Independent",
    ],
    # ===========================================
    # The entry_points field is used to register the plugin with mythril
    #
    # Right now we register only one plugin for the "mythril.plugins" entry point,
    # note that you can add multiple plugins.
    # ===========================================
    entry_points={
        "mythril.plugins": [
            "myth_example_detector = nft_ownership_detector:NFTOwnershipDetector",
        ],
    },
    python_requires='>=3.6',
)