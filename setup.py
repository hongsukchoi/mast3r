from setuptools import setup, find_packages

print('Found packages:', find_packages())
setup(
    description='MASt3R as a package',
    name='mastrrr',
    version='0.0',    
    packages=find_packages(),
    install_requires=[
        'torch==2.0.1',
        'torchvision==0.15.2',
        'scikit-learn',
        'roma',
        'gradio==4.44.1',
        'matplotlib',
        'tqdm',
        'opencv-python',
        'scipy',
        'einops',
        'trimesh',
        'tensorboard',
        'pyglet<2',
        'huggingface-hub[torch]>=0.22',
    ],
    extras_require={
        'all': [
            'dust3r @ git+https://github.com/naver/dust3r.git'
        ],
    },
)