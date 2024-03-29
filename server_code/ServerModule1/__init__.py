import anvil.google.auth, anvil.google.drive, anvil.google.mail
from anvil.google.drive import app_files
import anvil.tables as tables
import anvil.tables.query as q
from anvil.tables import app_tables
import anvil.server
import requets

# This is a server module. It runs on the Anvil server,
# rather than in the user's browser.
#
# To allow anvil.server.call() to call functions here, we mark
# them with @anvil.server.callable.
# Here is an example - you can replace it with your own:
@anvil.server.callable
def add_location(Location_name,Latitude,Longtitude):
  app_tables.locations.add_row(Location_name=Location_name,Latitude=Latitude,Longtitude=Longtitude)

@anvil.server.callable
def get_ip_address():
    response = requests.get('https://api.ipify.org')
    return response.text