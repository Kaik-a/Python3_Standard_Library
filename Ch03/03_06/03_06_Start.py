# Tempfile Module
import tempfile

# Create a temporary file
tmp = tempfile.TemporaryFile()

# Write to a temporary file
tmp.write(b'save this special number: 5678309')
tmp.seek(0)

# Read the temporary file
print(tmp.read())

# Close the temporary file
tmp.close()