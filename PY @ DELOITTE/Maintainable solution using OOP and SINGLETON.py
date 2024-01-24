class ConfigurationManager:
  _instance = None

  def __new__(cls):
      if not cls._instance:
          cls._instance = super(ConfigurationManager, cls).__new__(cls)
          # Initialize configuration settings here
          cls._instance.config = {}
      return cls._instance

  def get_config(self, key):
      return self.config.get(key)

  def set_config(self, key, value):
      self.config[key] = value

# Example usage:

# Create instances of ConfigurationManager
config_manager1 = ConfigurationManager()
config_manager2 = ConfigurationManager()

# Both instances refer to the same object (Singleton)
print(config_manager1 is config_manager2)  # Output: True

# Set and get configuration settings
config_manager1.set_config('language', 'Python')
print(config_manager2.get_config('language'))  # Output: Python
