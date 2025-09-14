from http_client import fetch_data


def run() -> None:
    """Run the consumer application."""
    try:
        # Fetch some sample data from a public API
        data = fetch_data("https://jsonplaceholder.typicode.com/posts/1")
        print(f"Fetched data: {data}")
        
        # Extract and display specific fields
        title = data.get("title", "No title")
        body = data.get("body", "No body")
        
        print(f"Title: {title}")
        print(f"Body: {body}")
        
    except Exception as e:
        print(f"Error fetching data: {e}")


if __name__ == "__main__":
    run()