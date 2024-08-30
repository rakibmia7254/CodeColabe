  CodeColabe README

CodeColabe
==========

**CodeColabe** is a live code-sharing platform built with Django and Django Channels. It allows users to collaboratively edit code in real-time, using a simple and intuitive interface powered by CodeMirror. No login or authentication is required, making it easy to jump right into coding.

Features
--------

*   **Real-time Collaboration**: Multiple users can edit code simultaneously, with changes reflected instantly.
*   **CodeMirror Integration**: Syntax highlighting and code editing with the powerful CodeMirror editor.
*   **No Authentication Required**: Join or create workspaces without needing to log in.

Getting Started
---------------

### Prerequisites

Before you begin, ensure you have the following installed:

*   Python 3.8+
*   Django 4.x
*   Django Channels 4.x
*   Uvicorn

### Installation

1.  **Clone the repository**:
    
        git clone https://github.com/yourusername/CodeColabe.git
        cd CodeColabe
    
2.  **Create a virtual environment and activate it**:
    
        python -m venv env
        source env/bin/activate  # On Windows use `env\Scripts\activate`
    
3.  **Install the dependencies**:
    
        pip install -r requirements.txt
    
4.  **Apply migrations**:
    
        python manage.py migrate
    

### Running the Server

To start the CodeColabe server, use Uvicorn:

    uvicorn livecodeshare.asgi:application --host 0.0.0.0 --port 8000

Navigate to `http://localhost:8000/<workspace_name>/` to start coding live in your workspace.

### Usage

*   Simply open a browser and navigate to `http://localhost:8000/your_workspace_name/` to start a new workspace or join an existing one.
*   Any code changes made by you or others will be instantly reflected across all connected clients.

Project Structure
-----------------

    CodeColabe/
    ├── core/
    │   ├── consumers.py
    │   ├── routing.py
    │   ├── urls.py    
    │   └── views.py  
    │
    ├── code_colabe/
    │   ├── asgi.py   
    │   ├── settings.py
    │   ├── urls.py   
    │   └── wsgi.py   
    ├── templates
    │   ├── index.html 
    │   └──editor.html
    │
    └── manage.py

Contributing
------------

Contributions are welcome! Please fork the repository and submit a pull request to contribute to CodeColabe.

License
-------

This project is licensed under the MIT License. See the [LICENSE](LICENSE) file for details.

Acknowledgments
---------------

*   [Django](https://www.djangoproject.com/) - The web framework used
*   [Django Channels](https://channels.readthedocs.io/en/stable/) - For WebSocket support
*   [CodeMirror](https://codemirror.net/) - The code editor integrated into the platform