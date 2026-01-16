import asyncio
import sys
import os
from motor.motor_asyncio import AsyncIOMotorClient
from dotenv import load_dotenv

# Load environment variables from .env file
load_dotenv()

# Global configuration pulled from environment variables
MONGO_URI = os.getenv("MONGO_URI")
DB_NAME = os.getenv("DB_NAME")
COLLECTION_NAME = os.getenv("COLLECTION_NAME")
TARGET_FIELD = os.getenv("TARGET_FIELD")
NEW_VALUE = os.getenv("NEW_VALUE")

async def run_migration():
    """
    Connects to MongoDB and adds a new field to all documents 
    where that field does not already exist.
    """
    
    # Check if all required environment variables are present
    required_config = [MONGO_URI, DB_NAME, COLLECTION_NAME, TARGET_FIELD, NEW_VALUE]
    if any(setting is None for setting in required_config):
        print("Error: Missing configuration. Please check your .env file.")
        return

    client = AsyncIOMotorClient(MONGO_URI)
    db = client[DB_NAME]
    collection = db[COLLECTION_NAME]

    print(f"Connecting to database: {DB_NAME}")
    print(f"Targeting collection: {COLLECTION_NAME}")

    try:
        # Filter for documents missing the specific field
        query = {TARGET_FIELD: {"$exists": False}}
        cursor = collection.find(query)
        
        count = 0
        async for document in cursor:
            # Update document by setting the new field and value
            await collection.update_one(
                {"_id": document["_id"]}, 
                {"$set": {TARGET_FIELD: NEW_VALUE}}
            )
            count += 1
            print(f"Updated record ID: {document['_id']}")

        print(f"Migration complete. Total records updated: {count}")

    except Exception as error:
        print(f"An error occurred during migration: {error}")
    finally:
        client.close()
        print("Database connection closed.")

if __name__ == "__main__":
    # Ensure compatibility with Windows event loop for Motor/Asyncio
    if sys.platform == 'win32':
        asyncio.set_event_loop_policy(asyncio.WindowsSelectorEventLoopPolicy())
    
    asyncio.run(run_migration())