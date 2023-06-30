# DevneyaUnchained

[![Streamlit App](https://static.streamlit.io/badges/streamlit_badge_black_white.svg)](https://devneyaunchained.streamlit.app/)


**DevneyaUnchained** is a web application that makes web development with Streamlit more convenient. The app authorizes the user via GitHub OAuth and requests the **OPEN_AI** token. Once the necessary information is provided, the user can create an empty project and deploy it. At this stage, the user can write a coding request to the LLM model and deploy the generated code directly to the deployed project.

## Table of Contents

- [Installation](#installation)
- [Usage](#usage)
- [Configuration](#configuration)
- [Project Structure](#project-structure)
- [License](#license)

## Installation

Here are the instructions for launching DevneyaUnchained web application locally:

1. Install all dependencies to your environment:

   ``` shell
   $ pip install -r requirements.txt
```
 

2. Locally launch the streamlit localhost by using the following command:
 
 ``` python
 $ streamlit run app.py
  ```

## Usage
**DevneyaUnchained** can be used to create any type of Streamlit app. For instance, Dashboard for data analysis with a wide variety data visualisation. Usecases can be found on Streamlit website.

## Configuration
**DevneyaUnchained** uses GitHub OAuth app for the authentication process. If the app is run locally, you need to include the **CLIENT_ID** and **CLIENT_SECRET** in the environment.

## Project Structure
The project structure is as follows:

```
DevneyaUnchained
├── CONTRIBUTOR_LICENSE_AGREEMENT
├── LICENSE
├── LICENSE-AGPL
├── LICENSE-APACHE
├── README.md
├── app.py
├── requirements.txt
├── src
│   ├── auth.py
│   ├── buttons.py
│   ├── codefile.py
│   ├── connection.py
│   ├── layout.py
│   ├── prompt.py
│   └── window_slide.py
└── test
    ├── test_auth.py
    └── test_prompt.py
```
The application is launched from app.py, and all the functionality is located in the src directory. The front-end part is located in buttons.py, layout.py, and window_slide.py.



## License
This project is licensed under the ***Apache License, Version 2.0***.



