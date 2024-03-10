from ._anvil_designer import Form1Template
from anvil import *
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
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
    results = GoogleMap.geocode(address=self.location_search.text)
    result = results[0].geometry.location
    marker = GoogleMap.Marker(position=result)
    self.MAP.add_component(marker)
    self.MAP.center =result
    self.MAP.zoom = 10
    self.MAP.visible = True
    self.Add_location.enabled=True
    self.latitude = result.lat()
    self.longtitude = result.lng()

  def Add_location_to_db(self, **event_args):
    """This method is called when the button is clicked"""
    anvil.server.call('add_location', self.location_name.text,self.latitude,self.longtitude)

  def button_1_click(self, **event_args):
    """This method is called when the button is clicked"""
    open_form('Form2')
    

