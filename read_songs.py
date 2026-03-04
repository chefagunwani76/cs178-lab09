import boto3
from boto3.dynamodb.conditions import Attr

REGION = "us-east-1"
TABLE_NAME = "Songs"


def get_table():
    """Return a reference to the DynamoDB Songs table."""
    dynamodb = boto3.resource("dynamodb", region_name=REGION)
    return dynamodb.Table(TABLE_NAME)

def print_song(song):
    """Print a single song's details in a readable format."""
    title = song.get("Title", "Unknown Title")
    artist = song.get("Artist", "Unknown Artist")
    year = song.get("Release Year", "Unknown Release Year")
    # Ratings is a nested map in the table — handle it gracefully
    genre = song.get("Genre", "Unknown Genre")
    #rating_str = ", ".join(f"{k}: {v}" for k, v in ratings.items()) if ratings else "No ratings"
    
    print(f"  Title : {title}")
    print(f"  Artist: {artist}")
    print(f"  Year  : {year}")
    print(f"  Genre: {genre}")
    print()


def print_all_songs():
    """Scan the entire table and print each item."""
    table = get_table()
    response = table.scan()
    items = response.get("Items", [])
    
    if not items:
        print("No songs found. Make sure your DynamoDB table has data.")
        return
    
    print(f"Found {len(items)} song(s):\n")
    for song in items:
        print_song(song)

def main():
    print("===== Reading from DynamoDB =====\n")
    print_all_songs()


if __name__ == "__main__":
    main()