STYLES = {
    "sidebar": """
        QWidget {
            background-color: #f0f0f0;
            border-right: 1px solid #ccc;
        }
    """,
    "sidebar_button": """
        QPushButton {
            background-color: #ffffff;
            border: 1px solid #ddd;
            border-radius: 5px;
            padding: 10px;
            margin: 5px;
            text-align: left;
        }
        QPushButton:hover {
            background-color: #e0e0e0;
        }
        QPushButton:pressed {
            background-color: #d0d0d0;
        }
    """,
    "content": """
        QWidget {
            background-color: #ffffff;
        }
    """,
    "title": """
        QLabel {
            font-size: 18px;
            font-weight: bold;
            color: #333;
            margin-bottom: 15px;
        }
    """,
    "content_button": """
        QPushButton {
            background-color: #4a90e2;
            color: white;
            border: none;
            border-radius: 5px;
            padding: 10px 15px;
            margin: 5px;
            min-width: 200px;
            text-align: left;
        }
        QPushButton:hover {
            background-color: #3a80d2;
        }
        QPushButton:pressed {
            background-color: #2a70c2;
        }
    """,
    "settings_form": """
        QLineEdit {
            border: 1px solid #ddd;
            border-radius: 3px;
            padding: 5px;
        }
        QLabel {
            color: #555;
        }
    """
}