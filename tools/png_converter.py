import os
from PIL import Image

def convert_dds_to_png_recursive():
    # os.walk yields a 3-tuple: (dirpath, dirnames, filenames)
    for root, dirs, files in os.walk('.'):
        for filename in files:
            if filename.lower().endswith('.dds'):
                # Construct the full input path
                source_path = os.path.join(root, filename)
                
                try:
                    with Image.open(source_path) as img:
                        # Construct the output path by swapping the extension
                        target_path = os.path.splitext(source_path)[0] + ".png"
                        
                        img.save(target_path, "PNG")
                        print(f"Converted: {source_path} -> {target_path}")
                except Exception as e:
                    print(f"Failed to convert {source_path}: {e}")

if __name__ == "__main__":
    convert_dds_to_png_recursive()