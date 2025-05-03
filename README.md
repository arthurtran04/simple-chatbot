# Image Captioning Application using BLIP model

## Introduction

This repository showcases an innovative **Image Captioning Application** powered by the **BLIP model** (Bootstrapping Language-Image Pre-training). Built entirely in **Python**, this project demonstrates the fascinating intersection of computer vision and natural language processing by automatically generating descriptive captions for images. Perfect for those interested in exploring multimodal AI applications!

## Table of Contents

- [Introduction](#introduction)
- [Prerequirements](#prerequirements)
- [Project Structure](#project-structure)
- [Model](#model)
- [Features](#features)
- [Installation](#installation)
- [Usage](#usage)
- [License](#license)

## Prerequirements

- ![Python 3.9](https://img.shields.io/badge/Python-3.9-blue) or above: [Download here](https://python.org/downloads)

## Project Structure

```
Image-Captioning-App/
├── test/
│   ├── test.py
│   └── ronaldo.jpg
├── .gitignore
├── image_captioning_app.py
├── requirements.txt
├── LICENSE
└── README.md
```

## Model

- [Salesforce/blip-image-captioning-base](https://huggingface.co/Salesforce/blip-image-captioning-base)

## Features

- Image Captioning Application using BLIP model from Hugging Face's Transformers
- Using Gradio UI

## Installation

To install this project, open your Terminal and follow these steps:

1. Clone the repository:

    ```bash
    git clone https://github.com/arthurtran04/Image-Captioning-App.git
    ```

2. Change the directory to `Image-Captioning-App`:

    ```bash
    cd "$(find . -type d -name "Image-Captioning-App")"
    ```

3. Create a Python virtual environment `venv` and install the required dependencies:

    ```bash
    python -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

## Usage

To start the application, run the `image_captioning_app.py` file:

   ```bash
   python image_captioning_app.py
   ```
This application will run locally at `http://127.0.0.1:7860`:

<img width="600rem" alt="Terminal" src="https://github.com/user-attachments/assets/67f66624-ba28-4c98-98f6-dc39f4da8c8c"/>

The UI:

<img width="600rem" alt="Webpage" src="https://github.com/user-attachments/assets/1fd98fa5-1901-434a-93af-5f1b96c4cf8f"/>

Upload your photo in the left box and click **Submit** button, the application will generate the image caption in the right box:

<img width="600rem" alt="Example" src="https://github.com/user-attachments/assets/b80dc8d4-c005-49c7-b11c-7cec7f209d6f"/>

To stop the application, use `Ctrl + C` in the Terminal

## License

This project is licensed under the MIT License. See the LICENSE file for more details.
