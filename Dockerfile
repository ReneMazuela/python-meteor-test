FROM meteor/galaxy-python:3.13.0

WORKDIR /app
COPY . .

# Install dependencies
RUN pip install --no-cache-dir -r requirements.txt

# REQUIRED BY GalaxyCloud
RUN python -m pip install --upgrade build && python -m build

# Run your app
CMD ["python", "-m", "flaskapp.app"]
