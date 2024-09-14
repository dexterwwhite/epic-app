from app import createApp

app = createApp()

if __name__ == "__main__":
    # Use app.config['DEBUG'] to get the debug setting
    app.run(debug=app.config['DEBUG'])