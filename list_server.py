#if len(sys.argv) != 2:
 #   print("Usage: python script.py <server_name>")
  #  sys.exit(1)

# Get the server name from the command-line argument
server_name = sys.argv[0]

# Use the server name in the AdminConfig.list command
Server = AdminConfig.list("Server", server_name)
print("Server:", Server[0:7])
