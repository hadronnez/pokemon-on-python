

class Scene:

    def __init__(self, escenario: dict):
        self.escenario = escenario
        self.quit = False

    def start(self):
        """Called when the scene is loaded to initialize/reset."""
        pass

    def handle_input(self):
        """Handle player input for this scene."""
        pass

    def update(self):
        """Update game logic for this scene."""
        pass

    def render(self):
        """Draw the scene to the screen."""
        pass

    def should_quit(self):
        """Return True if this scene wants to exit."""
        #return self.quit
        pass