# Quote-Announcement-Generator

This is a Python command-line tool that simplifies the creation of quote and announcement images. It takes text and a background image (or solid color) as input and generates a visually appealing image with the text overlaid.

**Key Features:**

*   **Customizable Text:**  Control font, size, color, alignment, and wrapping.
*   **Image and Color Backgrounds:**  Use either an image or a solid color as the background.
*   **Command-Line Interface:**  Easy to use from the terminal with various options.
*   **Text Wrapping:** Automatic text wrapping to fit within the image boundaries.

**Installation:**

1.  **Clone the repository:**

    ```bash
    git clone https://github.com/Shaloom7/Quote-Announcement-Generator.git
    cd Quote-Announcement-Generator
    ```

2.  **Install dependencies:**

    ```bash
    pip install Pillow
    ```

**Usage:**

```bash
python quote_generator.py "Your Qoute Here" output_02.png -b Background.jpg
