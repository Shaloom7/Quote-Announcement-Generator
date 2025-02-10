from PIL import Image, ImageDraw, ImageFont
import argparse
import textwrap
import os

DEFAULT_FONT_PATH = "arial.ttf"  

def create_quote_image(
    quote, background_image_path, output_path, font_path=None, font_size=36,
    text_color=(255, 255, 255), bg_color=None, wrap_width=40,
    horizontal_alignment="center", vertical_alignment="center",
    padding=20
):
    """
    Generates an image with text overlaid on a background image.
    """
    print(f"Quote: {quote}")  
    print(f"Background image path: {background_image_path}")  
    print(f"Output path: {output_path}")  

    try:
        if bg_color:
            img = Image.new("RGB", (800, 600), bg_color) 
            print("Using solid background color")  
        else:
            img = Image.open(background_image_path)
            print("Background image opened successfully")  
    except FileNotFoundError:
        print(f"Error: Background image not found at {background_image_path}")
        return
    except Exception as e:
        print(f"Error opening image: {e}")
        return

    draw = ImageDraw.Draw(img)
    
    # Font Handling
    try:
        if font_path:
            font = ImageFont.truetype(font_path, size=font_size)
            print(f"Using font from path: {font_path}") 
        else:
            try:
                font = ImageFont.truetype("Arial.ttf", size=font_size)
            except IOError:
                try:
                    font = ImageFont.truetype("arial.ttf", size=font_size)
                except IOError:
                    print("Warning: Arial font not found, using default PIL font.")
                    font = ImageFont.load_default()
    except IOError:
        print(f"Error: Font not found at {font_path}, using default PIL font.")
        font = ImageFont.load_default()
    except Exception as e:
        print(f"Error loading font: {e}")
        return

    print("Font loaded successfully")  
    
    # Text Wrapping
    wrapped_lines = textwrap.wrap(quote, width=wrap_width)
    print(f"Wrapped lines: {wrapped_lines}")  
    
    # Text Positioning
    total_text_height = sum(draw.textbbox((0, 0), line, font=font)[3] for line in wrapped_lines)
    
    if vertical_alignment == "top":
        y_text = padding
    elif vertical_alignment == "bottom":
        y_text = img.height - total_text_height - padding
    else:  
        y_text = (img.height - total_text_height) / 2
    
    for line in wrapped_lines:
        left, top, right, bottom = draw.textbbox((0, 0), line, font=font)
        text_width = right - left
        text_height = bottom - top
        
        if horizontal_alignment == "left":
            x_text = padding
        elif horizontal_alignment == "right":
            x_text = img.width - text_width - padding
        else:  
            x_text = (img.width - text_width) / 2
        
        draw.text((x_text, y_text), line, font=font, fill=text_color)
        y_text += text_height
    
    print("Text drawn on image")  
    img.save(output_path)
    print(f"Image saved to {output_path}")


def main():
    parser = argparse.ArgumentParser(description="Generate an image with text on a background.")
    parser.add_argument("quote", help="The quote or announcement text.")
    parser.add_argument("output", help="Output file path (e.g., output.png)")
    parser.add_argument("-b", "--background", help="Path to the background image.", required=False)
    parser.add_argument("-f", "--font", help="Path to the font file (.ttf).", required=False)
    parser.add_argument("-s", "--size", type=int, default=36, help="Font size.")
    parser.add_argument("-tc", "--textcolor", default="255,255,255", help="Text color in R,G,B format (e.g., 255,0,0 for red).")
    parser.add_argument("-bc", "--bgcolor", help="Background color in R,G,B format (e.g., 0,0,0 for black).")
    parser.add_argument("-w", "--wrap", type=int, default=40, help="Maximum characters per line.")
    parser.add_argument("-ha", "--halign", choices=["left", "center", "right"], default="center", help="Horizontal text alignment.")
    parser.add_argument("-va", "--valign", choices=["top", "center", "bottom"], default="center", help="Vertical text alignment.")
    parser.add_argument("-p", "--padding", type=int, default=20, help="Padding around the text in pixels.")
    args = parser.parse_args()
    
    try:
        text_color = tuple(map(int, args.textcolor.split(",")))
        if len(text_color) != 3:
            raise ValueError
    except ValueError:
        print("Error: Invalid text color format. Use R,G,B (e.g., 255,0,0).")
        return
    
    bg_color = None
    if args.bgcolor:
        try:
            bg_color = tuple(map(int, args.bgcolor.split(",")))
            if len(bg_color) != 3:
                raise ValueError
        except ValueError:
            print("Error: Invalid background color format. Use R,G,B (e.g., 0,0,0).")
            return
    
    if not args.background and not args.bgcolor:
        print("Error: Either --background or --bgcolor must be provided.")
        return
    
    create_quote_image(
        args.quote,
        args.background,
        args.output,
        args.font,
        args.size,
        text_color,
        bg_color,
        args.wrap,
        args.halign,
        args.valign,
        args.padding
    )

if __name__ == "__main__":
    main()
