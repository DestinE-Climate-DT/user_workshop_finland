# Getting started with Climate DT data

## 1. Creating your environment
### 1.1 Using mamba or conda

To create a working python environment use the environment.yml file with mamba or conda by following these steps. If you use conda, replace the `mamba` with `conda`.
1. Create the environment, this may take a while, by running:
```shell
mamba env create -f environment.yml
```
Add `-p <path-to-your-environment-folder>` if your environment should be somewhere specific. To change the environment name add `-n <name>`. The default name is `climatedt_workshop`.

2. Activate the environment.
```shell
mamba activate climatedt_workshop
```
or 
```shell
mamba activate <path-to-your-environment-folder>
```
3. Install a jupyter kernel to run jupyter notebooks
```shell
python3 -m ipykernel install --name climatedt_workshop --user
```

### 1.2 Using pip
TODO

## 2. Setting up the DESP authentication

```shell
cd /yourpathto/finnish_user_workshop/
wget https://raw.githubusercontent.com/destination-earth-digital-twins/polytope-examples/refs/heads/main/desp-authentication.py
```