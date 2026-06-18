Markdown

# 🛸 Autonomous Drone Simulation Project (PX4 & Gazebo)

This repository contains a fully configured autonomous drone simulation setup integrating **PX4 Autopilot** and **Gazebo**. It features a custom-designed world environment and a personalized drone model equipped with sensors for autonomous mission execution.

---

## 📋 Table of Contents
1. [Technical Requirements & Dependencies](#1-technical-requirements--dependencies)
2. [Step-by-Step Installation & Setup](#2-step-by-step-installation--setup)
3. [How to Clone and Download the Project](#3-how-to-clone-and-download-the-project)
4. [Launching the Simulation World](#4-launching-the-simulation-world)
5. [Running the Autonomous Control Script](#5-running-the-autonomous-control-script)

---

## 1. Technical Requirements & Dependencies

Before downloading and running the simulation, ensure your system meets the following specifications:
* **Operating System:** Ubuntu 22.04 LTS (Native installation is highly recommended).
* **Simulation Stack:** PX4 Autopilot (v1.14 or compatible) and Gazebo Classic.
* **Programming Language:** Python 3.x (with MAVSDK or DroneKit depending on your control script implementation).

---

## 2. Step-by-Step Installation & Setup

If you do not have the PX4 environment installed on your Ubuntu 22.04 machine, run the following commands in your terminal to set it up:

### Step 1: Clone the PX4 Autopilot Source Code
```bash
cd ~
git clone [https://github.com/PX4/PX4-Autopilot.git](https://github.com/PX4/PX4-Autopilot.git) --recursive

Step 2: Run the Official Ubuntu Setup Script

This script installs PX4, Gazebo Classic, and all necessary dependencies:
Bash

bash ./PX4-Autopilot/Tools/setup/ubuntu.sh

Note: Please restart your computer after the script finishes installing all the packages.
3. How to Clone and Download the Project

Once your environment is ready, you can pull this project repository directly onto your local machine:
Step 1: Open your terminal (Ctrl + Alt + T) and navigate to your workspace (e.g., Home directory):
Bash

cd ~

Step 2: Clone the repository to download all project files, folders, and assets:
Bash

git clone [https://github.com/abdulkreim1616-lgtm/Project2.git](https://github.com/abdulkreim1616-lgtm/Project2.git)

Step 3: Enter the project directory:
Bash

cd Project2

4. Launching the Simulation World

To load the custom world environment (external_world.sdf) along with the personalized drone design properly without any "Model Not Found" issues, follow these commands:
Step 1: Export Gazebo Model and Resource Paths

You must inform Gazebo where the custom models (model.sdf, model.config) and world directories are located. Run these commands inside the Project2 folder:
Bash

export GAZEBO_MODEL_PATH=$GAZEBO_MODEL_PATH:$(pwd)
export GAZEBO_RESOURCE_PATH=$GAZEBO_RESOURCE_PATH:$(pwd)

Step 2: Launch PX4 SITL Embedded with the Custom World

Execute the launch command to link the simulation stack with your specific world layout:
Bash

make px4_sitl gazebo-classic___empty PXL_SRC=$(pwd)/external_world.sdf

5. Running the Autonomous Control Script

To trigger the autonomous flight logic and start monitoring or directing the drone inside the newly launched simulation world:
Step 1: Open a NEW terminal tab/window and navigate to the project directory:
Bash

cd ~/Project2

Step 2: Execute the Python simulation script:
Bash

python3 city1.py
