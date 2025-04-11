# University of Oklahoma 7nm Finfet Neuron Research Project 🚀

Welcome to the GitHub repository for the **University of Oklahoma 7nm Finfet Neuron Research Project**.  
Please note that this project adheres to the **MIT License**. All public exposure of files related to this work must include proper citations to the original poster. Any citations to this repository should reference:  
**Logan Larsh - University of Oklahoma - Inquire Labs**.

---

## Table of Contents 📚

1. [Software Configuration](#software-configuration)
2. [Installation Steps](#installation-steps)
    - [Step 1: Xschem Setup](#step-1-xschem-setup)
    - [Step 2: NGSpice Installation](#step-2-ngspice-installation)
    - [Step 3: Enabling BSIM-CMG3](#step-3-enabling-bsim-cmg3)
    - [Step 4: Python Environment Setup](#step-4-python-environment-setup)
3. [The XSchem Environment](#the-xschem-environment)
4. [Running Simulations & Measuring Data](#running-simulations--measuring-data)
5. [Contact Information](#contact-information)

---

## Software Configuration 🛠️

This repository requires the following software tools:

- **Xschem** (schematic capture)
- **NGSpice** (circuit simulation)
- **BSIM-CMG3** (transistor model)
- **Python (Anaconda/Miniconda)** (data processing and plotting)

---

## Installation Steps ⚙️

### Step 1: Xschem Setup 🖥️

#### **Requirements:**
- **C89 compiler**
- **awk** (compatible with mawk or gawk)
- **Tcl/Tk** (tested with versions 8.4, 8.5, & 8.6)
- **Xlib, Xpm**
- **bison**
- **flex**
- *(Optional)*: **cairo** (for enhanced text rendering)
- *(Optional)*: **xcb**
- *(Optional)*: **xrender**

#### **Compilation:**
```bash
./configure && make
```
For additional options, run:
```bash
./configure --help
```

#### **Running from Source:**
```bash
cd src && ./xschem
```

#### **Installation:**
You can install via:
```bash
make install
```
Or, specify an installation directory:
```bash
make install DESTDIR=/tmp/packaging
```

---

### Step 2: NGSpice Installation 🔌

Install **NGSpice** by following the instructions on the official NGSpice website. There are no special dependencies required for installation.

---

### Step 3: Enabling BSIM-CMG3 🔄

To enable BSIM-CMG3 in your NGSpice environment, update the configuration files in your local NGSpice install directory:

- Locate the NGSpice configuration file.
- Modify the file to switch the BSIM-CMG setting (flip the true/false status) as required.

---

### Step 4: Python Environment Setup 🐍

Ensure you have a working Python environment on your local machine. It is recommended to install **Miniconda** or **Anaconda** so you can run the provided Python scripts to process and plot simulation data.

---

## The XSchem Environment 🎨

The Xschem environment is designed for effective schematic development and spice simulations. It supports simulation of circuits with up to **114 variables** using NGSpice BSIM-CMG integration.

### Key Components:

1. **Layout Environment:**
   - Provides a unified interface to connect all schematic symbols.
   - **Tip:** Make sure all connections terminate in the middle of the red pads on each transistor.

2. **Finfet Model:**
   - The Finfet model is derived from the Arizona State University ASAP PDK.
   - Spice files have been modified for compatibility with NGSpice.
   - **Important:** Ensure that the associated spice files are located in the NGSpice local run directory.

3. **Spice Symbols:**
   - In Xschem, spice commands are output on the local UI relative to the circuit layout.
   - Access the "commands" symbol through the “place part” tool.
   - **Note:** Most relevant circuit components can be found in the `ngspice` directory within the parts tool.

---

## Running Simulations & Measuring Data 📊

1. **Starting Simulations:**
   - Use the example schematics provided to familiarize yourself with the workflow.
   - Confirm that the spice file and Finfet symbol are correctly placed in their respective directories.
   - In Xschem, click **Netlist** and then **Simulate** to automatically start the simulation.
   - **Important:** It is recommended to run the behavioral schematic first as more complex simulations may take several days.

2. **Data Output:**
   - After a behavioral simulation (e.g., for a configuration like "say-besrour"), a circuit sample text file will be generated on your desktop.
   - You may need to modify the output directory in the spice command symbol.

3. **Data Analysis:**
   - Use the accompanying behavioral Python script to decompose and plot the simulation data.

---

## Contact Information 📧

For any questions or further assistance, please contact:

**Logan Larsh**  
University of Oklahoma - Inquire Labs  
Email: [logan.c.larsh-1@ou.edu](mailto:logan.c.larsh-1@ou.edu)

---

Thank you for participating in the Neuronal Finfet Research Project! 😊 Enjoy exploring and simulating the advanced FinFET neuron models.
