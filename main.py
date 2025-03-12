import os

# Get the current working directory
current_directory = os.getcwd()

import code
import sys
import os

def start_console():
    # Save the current console state
    old_stdout = sys.stdout
    old_stdin = sys.stdin
    
    # Welcome message
    print("Starting Interactive Python Console...")
    print("Use Ctrl+D (Unix) or Ctrl+Z (Windows) to exit")
    print(os.getcwd())
    
    # Create variables that will be available in the interactive console
    variables = globals().copy()
    variables.update(locals())
    
    # Start the interactive console
    try:
        code.interact(local=variables, banner="")
    finally:
        # Restore the console state
        sys.stdout = old_stdout
        sys.stdin = old_stdin

# Run the interactive console
start_console()

import pygame

pygame.init()
screen = pygame.display.set_mode((640, 480))
done = False

# load the fonts
font = pygame.font.SysFont("Times new Roman", 36)
# Render the text in new surface
text = font.render("My first Game Screen", True, (158, 16, 16))

while not done:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            done = True

    screen.fill((255, 255, 255))

    # We will discuss blit() in the next topic
    screen.blit(text, (320 - text.get_width() // 2, 240 - text.get_height() // 2))
    pygame.draw.rect(screen, (28, 171, 226), pygame.Rect(30, 30, 60, 60))
    pygame.display.flip()


# Create HTML content
html_content = f"""
<!DOCTYPE html>
<html lang="en">
  <head>
    <meta charset="utf-8" />
    <meta name="viewport" content="width=device-width, initial-scale=1" />
    <title>local modules</title>
    <!-- linking to PyScript assets -->
    <link rel="stylesheet" href="https://pyscript.net/releases/2023.03.1/pyscript.css" />
    <script defer src="https://pyscript.net/releases/2023.03.1/pyscript.js"></script>
  </head>
  <body>
      <py-config>
        "packages" = ["pandas","numpy","matplotlib"]
      </py-config>
<div id="mydiv"></div>       
     <py-script>       
  from pyscript import display
  display("hello")
  print("hello")
</py-script>
  </body>
</html>

"""

# Write the HTML content to a file
with open("index.html", "w") as file:
    file.write(html_content)

print("HTML file created successfully.")
