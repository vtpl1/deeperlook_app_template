# Deeperlook Application Template

## Installation
### Pre-Requisite
- [Docker](https://www.docker.com/)
- CPU only algorithms:
    - Base docker image `docker pull vtpl/deeperlook_base:cpu`
- GPU based algotithms:
    - [Nvidia container runtime](https://github.com/NVIDIA/nvidia-container-runtime) for GPU based algorithms
    - Base docker image `docker pull vtpl/deeperlook_base:gpu`
- FPGA based algorithms [Xylinx](https://github.com/Xilinx/Vitis-AI.git)

### Setting Environment
- Clone the template repository.
```
git clone https://github.com/vtpl1/deeperlook_app_template.git
```

### Open in VS code and develop
The VS code has required devcontainer ready for development of GPU based algorithms
![Development](https://github.com/vtpl1/deeperlook_app_template/blob/main/images/development.gif)


## Run the developed appication in development environment
Run the developed algorithm using the following command

``` Python
vtpl --job 250 file:///workspaces/deeperlook_app_template/videos/crowd.mp4
```

## Deploy the development application in production environment
### Create a wheel file using the following command:

``` Python
python3 setup.py bdist_wheel
```

### Upload the wheel using the DeeperLook application uploader
![Deploy](https://github.com/vtpl1/deeperlook_app_template/blob/main/images/deploy.gif)

### Use the application in production
![Result](https://github.com/vtpl1/deeperlook_app_template/blob/main/images/result.gif)

## License
[MIT License](https://github.com/vtpl1/deeperlook_app_template/blob/main/LICENSE)