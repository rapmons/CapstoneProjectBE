# Sử dụng image base chứa Python
FROM python:3.10.12

# Set the working directory in the container
WORKDIR /app

# Copy the requirements file to the working directory
COPY requirements.txt .

# Install the required packages
RUN pip install -r requirements.txt

# Copy the rest of the application code to the working directory
COPY . .

# Expose the port on which the Django application will run
EXPOSE 8000

# Set environment variables
ENV DJANGO_SETTINGS_MODULE=EnglishAppBE.settings
ENV PYTHONUNBUFFERED=1

# Run migrations
RUN python manage.py migrate

# Start the Django development server
CMD ["python", "manage.py", "runserver", "0.0.0.0:8000"]
