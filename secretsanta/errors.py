class SecretSantaError(Exception):
    """Base class for exceptions in Secret Santa program."""
    pass

class FileLoadError(SecretSantaError):
    """Exception raised when there is an error loading a file."""
    def __init__(self, message="Error loading file."):
        self.message = message
        super().__init__(self.message)

class AssignmentError(SecretSantaError):
    """Exception raised when assignment fails."""
    def __init__(self, message="Unable to complete Secret Santa assignments."):
        self.message = message
        super().__init__(self.message)
