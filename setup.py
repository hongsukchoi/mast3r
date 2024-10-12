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
        'scikit-learn==1.2.2',
        'roma==0.4.0',
        'gradio==3.34.0',
        'matplotlib==3.7.1',
        'tqdm==4.65.0',
        'opencv-python==4.7.0.72',
        'scipy==1.10.1',
        'einops==0.6.0',
        'trimesh==3.21.5',
        'tensorboard==2.13.0',
        'pyglet==1.5.27',
        'huggingface-hub[torch]==0.22.1',
    ],
    extras_require={
        'all': [
            
        ],
    },
)