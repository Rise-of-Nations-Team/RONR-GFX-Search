import re

def transform_sprites(input_text):
    # Regex to capture the name and texture path within SpriteType blocks
    pattern = re.compile(
        r'SpriteType\s*=\s*\{.*?name\s*=\s*"(.*?)".*?texturefile\s*=\s*"(.*?)".*?\}',
        re.DOTALL
    )
    
    matches = pattern.findall(input_text)
    output = []

    for name, path in matches:
        # Swap .dds extension for .png
        png_path = path.replace('.dds', '.png')
        
        html_block = f"""						<div
							data-clipboard-text="{name}"
							data-search-text="{name}"
							title="{name}"
							class="icon dlc-base"
						>
							<img
								src="{png_path}"
								loading="lazy"
								alt="{name}"
							/>
						</div>"""
        output.append(html_block)
    
    return "\n".join(output)

# Example usage for file handling:
if __name__ == "__main__":
    # Replace 'input.txt' and 'output.html' with your actual filenames
    try:
        with open('RON_goals.gfx', 'r', encoding='utf-8') as f:
            content = f.read()
            
        result = transform_sprites(content)
        
        with open('output.html', 'w', encoding='utf-8') as f:
            f.write(result)
            
        print("Transformation complete. Check output.html")
    except FileNotFoundError:
        print("Input file not found.")