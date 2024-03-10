from ._anvil_designer import Form1Template
from anvil import *
import anvil.google.auth, anvil.google.drive
from anvil.google.drive import app_files
import anvil.server

class Form1(Form1Template):
  def __init__(self, **properties):
    # Set Form properties and Data Bindings.
    self.init_components(**properties)

    # Any code you write here will run before the form opens.

  def enable_search_box(self, **event_args):
    """This method is called when the text in this text box is edited"""
    self.search_button.enabled = self.location_name.text != "" and self.location_search.text != ""

  def search_button_click(self, **event_args):
    """This method is called when the button is clicked"""
    

