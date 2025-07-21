from .SceneManager import SceneManager

class GameManager:

    def __init__(self, config: dict):

        self.running = True
        self.config = config
        self.scene_manager = SceneManager()
    
        pass

    def initialize(self):
        """Initialize game resources, settings, etc."""
        pass

    def run(self):
        """Main game loop.
        while self.running:
            self.scene_manager.handle_input()
            self.scene_manager.update()
            self.scene_manager.render()

            if self.scene_manager.should_quit():
                self.running = False
        """
        pass

    def quit(self):
        """Clean up resources and quit the game.
        self.running = False
        """ 
        pass