# Project Name

Brief description of your project.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Contributing](#contributing)
- [License](#license)

## Installation

The project can be cloned or downloaded. The required python packages for this project are ```simpy, numpy, matplot, mpi4py``` etc. One way to install the required package is via pip commands as shown: 

```% pip install simpy``` <br>
```% pip install numpy```<br>
```% pip install matplot```<br>
```% pip install mpi4py```<br>

## Usage

This repository provides a variety of example implementations of a quantum cloud. The examples include quantum clouds with different setups. 
<br>
```QCloudSim - Homogeneous-devices.ipynb``` demonstates an example QCloudSim with homogeneous quantum devices where all the resources are declared identical. The settings are simpler than hetrogeneous quantum devices. The setup includes a broker, a job generator and a QCloud. A broker is responsible for assigning the incoming jobs to resources with FIFO scheduling algorithm.<br>

```QCloudSim - Hetrogeneous.ipynb``` demonstates an example QCloudSim with hetrogeneous quantum devices micmicing some of the IBM quantum devices. The setup includes a broker, a job generator and a QCloud. A broker is responsible for assigning the incoming jobs to resources with random assignment scheduling algorithm and rotational scheduling algorithm. The runtime of the simulation is limited by ```SIM_TIME```. <br>

```QCloudSim - IBM - Machines.ipynb``` is similar to ```QCloudSim - Hetrogeneous.ipynb```. It demonstrates an example of QCloudSim with heterogeneous quantum devices, mimicking some of the IBM quantum devices. The setup includes a broker, a job generator, and a QCloud. A broker is responsible for assigning incoming jobs to resources using random assignment scheduling algorithms and rotational scheduling algorithms. Maintenance and calibration are integrated into this setup to mimic the synthetic quantum cloud. The runtime of the simulation is limited by SIM_TIME.

```QCloudSim - SC2024.ipynb``` demonstrates the usage of existing QCloud and Broker provided by QCloudSim package. The runtime of the simulation is limited by the number of jobs being processed. The core script of this file is identical to ```SC2024.py``` that is used to generate contents for SC2024 conference. <br>
